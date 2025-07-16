import os
import sys

from .pyshell.shell import InteractiveShell


def main() -> int:
    if sys.stdin.isatty():
        return InteractiveShell().run()
    else:
        return os.EX_OK
