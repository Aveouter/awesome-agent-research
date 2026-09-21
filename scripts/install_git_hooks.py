"""Install this checkout's boundary hooks and remember a working Python runtime."""
from pathlib import Path
import subprocess
import sys

root = Path(__file__).resolve().parent.parent
hooks = (root / '.githooks').as_posix()
existing = subprocess.run(['git', 'config', '--get', 'core.hooksPath'],
                          cwd=root, capture_output=True, text=True).stdout.strip()
if existing and existing != hooks:
    sys.exit('Existing core.hooksPath found. Integrate its hooks manually; not overwritten.')
subprocess.run(['git', 'config', '--local', 'paperBoundary.python',
                Path(sys.executable).as_posix()], cwd=root, check=True)
subprocess.run(['git', 'config', '--local', 'core.hooksPath', hooks], cwd=root, check=True)
print(f'Installed pre-commit and pre-push hooks: {hooks}')
print('This path is shared by linked worktrees; keep this checkout available.')
