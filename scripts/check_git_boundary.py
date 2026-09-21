#!/usr/bin/env python3
"""Check Git objects, never working-tree copies, before commit/push and in CI."""
import argparse
from pathlib import PurePosixPath
import re
import subprocess
import sys

MAX_BYTES = 1024 * 1024
TEXT_SUFFIXES = {'.md', '.bib', '.py', '.yml', '.yaml', '.json', '.toml', '.sh', '.ps1'}
SPECIAL_NAMES = {'.gitignore', '.gitattributes', '.editorconfig', 'LICENSE'}
HOOK_PATHS = {'.githooks/pre-commit', '.githooks/pre-push', '.githooks/run-check'}
LOCAL_DIRS = {'zotero', 'zoteroprofile', 'cache', 'data', 'models', 'checkpoints',
              'outputs', 'traces', 'exports', 'inbox', 'work', '.venv', 'venv',
              'node_modules', '.dsh', '.codex', '.claude'}
SIGNATURES = (b'%PDF-', b'SQLite format 3', b'PK\x03\x04', b'\x1f\x8b',
              b'7z\xbc\xaf\x27\x1c', b'\x89PNG', b'\xff\xd8\xff', b'MZ')
SECRET = re.compile(rb'-----BEGIN (?:[A-Z0-9]+ )*PRIVATE KEY-----|'
                    rb'\bgh[pousr]_[A-Za-z0-9]{30,}\b|'
                    rb'\bgithub_pat_[A-Za-z0-9_]{30,}\b')


def git(*args):
    return subprocess.check_output(['git', *args], stderr=subprocess.PIPE)


def entries(tree=None):
    if tree is None:
        records = git('ls-files', '--stage', '-z')
    else:
        records = git('ls-tree', '-r', '-z', tree)
    for record in records.split(b'\0'):
        if not record:
            continue
        meta, path = record.split(b'\t', 1)
        fields = meta.decode('ascii').split()
        if tree is None:
            mode, oid, stage = fields
            if stage != '0':
                raise ValueError('Resolve index conflicts before checking.')
        else:
            mode, kind, oid = fields
        yield mode, oid, path.decode('utf-8')


def path_error(path, mode):
    p = PurePosixPath(path)
    if mode not in {'100644', '100755'}:
        return 'symlinks and submodules are not allowed'
    if any(part.lower() in LOCAL_DIRS for part in p.parts[:-1]):
        return 'local-only directory'
    if p.name.lower().startswith('.env') or p.name.lower() in {
        'credentials.json', 'secrets.json', 'logins.json', 'prefs.js', 'user.js'
    }:
        return 'credential or application configuration file'
    if path in HOOK_PATHS or p.name in SPECIAL_NAMES:
        return None
    if p.suffix.lower() not in TEXT_SUFFIXES:
        return 'file type is outside the text-source allowlist'
    return None


def check(trees):
    seen = set()
    errors = []
    for tree in trees:
        for mode, oid, path in entries(tree):
            key = (mode, oid, path)
            if key in seen:
                continue
            seen.add(key)
            reason = path_error(path, mode)
            if not reason:
                size = int(git('cat-file', '-s', oid))
                if size > MAX_BYTES:
                    reason = 'exceeds the 1 MiB per-file limit'
                else:
                    data = git('cat-file', 'blob', oid)
                    if data.startswith(b'version https://git-lfs.github.com/spec/v1'):
                        reason = 'Git LFS pointers are not allowed'
                    elif any(data.lstrip().startswith(sig) for sig in SIGNATURES):
                        reason = 'raw/binary file signature (even if renamed)'
                    elif b'\0' in data:
                        reason = 'binary content'
                    elif SECRET.search(data):
                        reason = 'possible credential; content omitted'
                    else:
                        try:
                            data.decode('utf-8-sig')
                        except UnicodeDecodeError:
                            reason = 'not UTF-8 text'
            if reason:
                errors.append(f'{path!r}: {reason}')
    if errors:
        print('Git boundary rejected:\n' + '\n'.join(sorted(set(errors))), file=sys.stderr)
        print('Keep raw material outside this repository. Do not bypass hooks.', file=sys.stderr)
        return 1
    print(f'Git boundary passed: {len(seen)} unique file versions checked.')
    return 0


def revision_trees(base, head):
    # Scan every introduced snapshot: adding then deleting a PDF still leaks it.
    if base and set(base) != {'0'}:
        git('cat-file', '-e', base + '^{commit}')
        revisions = git('rev-list', head, '^' + base)
    else:
        revisions = git('rev-list', head)
    return [head, *revisions.decode('ascii').split()]


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument('--staged', action='store_true')
    mode.add_argument('--tree')
    mode.add_argument('--history', metavar='HEAD')
    mode.add_argument('--range', nargs=2, metavar=('BASE', 'HEAD'))
    mode.add_argument('--pre-push', action='store_true')
    args = parser.parse_args(argv)
    try:
        if args.staged:
            trees = [None]
        elif args.tree:
            trees = [args.tree]
        elif args.history:
            trees = revision_trees(None, args.history)
        elif args.range:
            trees = revision_trees(*args.range)
        else:
            trees = []
            for line in sys.stdin:
                local_ref, local_oid, remote_ref, remote_oid = line.split()
                if set(local_oid) != {'0'}:
                    trees.extend(revision_trees(remote_oid, local_oid))
        return check(trees)
    except (subprocess.CalledProcessError, ValueError, UnicodeError) as exc:
        # Do not dump file contents or credentials from subprocess output.
        print(f'Boundary check could not complete ({type(exc).__name__}). '
              'Check Git history, fetch the remote base, and retry.', file=sys.stderr)
        return 1


if __name__ == '__main__':
    sys.exit(main())
