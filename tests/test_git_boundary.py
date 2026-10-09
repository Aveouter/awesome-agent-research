"""Exercise real staged blobs and commit histories in disposable repositories."""
from pathlib import Path
import os
import subprocess
import sys
import tempfile
import unittest

CHECKER = Path(__file__).resolve().parents[1] / 'scripts/check_git_boundary.py'


class BoundaryTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.env = dict(os.environ, GIT_CONFIG_NOSYSTEM='1', GIT_CONFIG_GLOBAL=os.devnull)
        self.git('init', '-q')
        self.git('config', 'user.name', 'Boundary Test')
        self.git('config', 'user.email', 'boundary@example.invalid')
        self.git('config', 'core.hooksPath', '.disabled-hooks')

    def git(self, *args, input=None):
        return subprocess.check_output(['git', *args], cwd=self.root, env=self.env, input=input)

    def stage(self, path, data=b'# Research note\n'):
        target = self.root / path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(data)
        self.git('add', '-f', '--', path)

    def check(self, *args, stdin=None):
        return subprocess.run([sys.executable, str(CHECKER), *args], cwd=self.root,
                              env=self.env, input=stdin, capture_output=True, text=True)

    def test_notes_bibliography_and_support_code_allowed(self):
        for path in ('notes/paper.md', 'references/library.bib', 'scripts/check.py',
                     '.github/workflows/validate.yml', '.githooks/pre-commit'):
            self.stage(path)
        self.assertEqual(self.check('--staged').returncode, 0)

    def test_forbidden_files_and_local_directories(self):
        for path in ('paper.PDF', 'Zotero/record.md', 'copy.sqlite', 'backup.zip',
                     '.env', 'exports/fulltext.md', 'work/paper.md', 'image.png'):
            with self.subTest(path=path):
                self.stage(path)
                self.assertNotEqual(self.check('--staged').returncode, 0)
                self.git('rm', '--cached', '--', path)

    def test_renamed_pdf_and_database(self):
        for content in (b'%PDF-1.7\n', b'SQLite format 3\0'):
            self.stage('notes/disguised.md', content)
            self.assertNotEqual(self.check('--staged').returncode, 0)

    def test_checks_index_not_unstaged_fix(self):
        self.stage('notes/paper.md', b'%PDF-1.7\n')
        (self.root / 'notes/paper.md').write_text('# clean working copy')
        self.assertNotEqual(self.check('--staged').returncode, 0)

    def test_size_binary_and_credentials(self):
        samples = [b'x' * (1024 * 1024 + 1), b'abc\0def', b'\xff\xfe',
                   b'version https://git-lfs.github.com/spec/v1\noid sha256:fake',
                   b'ghp_' + b'a' * 36,
                   b'-----BEGIN ' + b'PRIVATE KEY-----']
        for content in samples:
            self.stage('notes/paper.md', content)
            result = self.check('--staged')
            self.assertNotEqual(result.returncode, 0)
            self.assertNotIn(content.decode('utf-8', errors='replace'), result.stderr)

    def test_deleted_pdf_still_blocked_in_history_and_push(self):
        self.stage('note.md')
        self.git('commit', '-qm', 'base')
        base = self.git('rev-parse', 'HEAD').decode().strip()
        self.stage('leak.pdf')
        self.git('commit', '-qm', 'accidental file')
        self.git('rm', 'leak.pdf')
        self.git('commit', '-qm', 'remove file')
        head = self.git('rev-parse', 'HEAD').decode().strip()
        self.assertEqual(self.check('--tree', 'HEAD').returncode, 0)
        self.assertNotEqual(self.check('--range', base, head).returncode, 0)
        for remote in (base, '0' * 40):
            stdin = f'refs/heads/test {head} refs/heads/test {remote}\n'
            self.assertNotEqual(self.check('--pre-push', stdin=stdin).returncode, 0)

    def test_symlink_rejected(self):
        oid = self.git('hash-object', '-w', '--stdin', input=b'D:/paper/Zotero').decode().strip()
        self.git('update-index', '--add', '--cacheinfo', f'120000,{oid},external.md')
        self.assertNotEqual(self.check('--staged').returncode, 0)

    def test_missing_base_fails_closed(self):
        self.stage('note.md')
        self.git('commit', '-qm', 'base')
        self.assertNotEqual(self.check('--range', '1' * 40, 'HEAD').returncode, 0)

    def test_clean_new_branch_and_deletion_push(self):
        self.stage('note.md')
        self.git('commit', '-qm', 'base')
        head = self.git('rev-parse', 'HEAD').decode().strip()
        new = f'refs/heads/test {head} refs/heads/test {"0" * 40}\n'
        deleted = f'(delete) {"0" * 40} refs/heads/test {head}\n'
        self.assertEqual(self.check('--pre-push', stdin=new).returncode, 0)
        self.assertEqual(self.check('--pre-push', stdin=deleted).returncode, 0)

    def test_actual_hooks_block_commit_and_push(self):
        hooks = CHECKER.parent.parent / '.githooks'
        self.git('config', 'core.hooksPath', hooks.as_posix())
        self.git('config', 'paperBoundary.python', Path(sys.executable).as_posix())
        self.stage('note.md')
        self.git('commit', '-qm', 'allowed')
        self.stage('bad.pdf')
        blocked = subprocess.run(['git', 'commit', '-qm', 'blocked'], cwd=self.root,
                                 env=self.env, capture_output=True)
        self.assertNotEqual(blocked.returncode, 0)
        # Simulate an imported commit made outside the protected workflow.
        self.git('-c', 'core.hooksPath=.disabled-hooks', 'commit', '-qm', 'imported')
        remote = self.root / 'remote.git'
        self.git('init', '--bare', '-q', str(remote))
        pushed = subprocess.run(['git', 'push', str(remote), 'HEAD:refs/heads/test'],
                                cwd=self.root, env=self.env, capture_output=True)
        self.assertNotEqual(pushed.returncode, 0)
        self.assertIn(b'Git boundary rejected', pushed.stderr)


if __name__ == '__main__':
    unittest.main()
