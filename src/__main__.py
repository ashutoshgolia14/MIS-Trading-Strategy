"""
Entry point for running the application as:
    python -m src

This file intentionally avoids changing existing import paths by
exposing the 'src' directory as a top-level import root.
"""

import sys
from pathlib import Path

def _expose_src_on_path():
    # Ensure <project_root>/src is on sys.path so imports like
    # 'from app...' continue to work unchanged.
    this_file = Path(__file__).resolve()
    src_dir = this_file.parent
    if str(src_dir) not in sys.path:
        sys.path.insert(0, str(src_dir))

def main():
    _expose_src_on_path()

    # Import here after sys.path adjustment
    from app.bootstrap import bootstrap
    bootstrap()

if __name__ == "__main__":
    main()
