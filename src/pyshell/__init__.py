import os
import sys

from pyshell.pyshell.context import Context
from pyshell.pyshell.shell import InteractiveShell


def main() -> int:
    if sys.stdin.isatty():
        return InteractiveShell().run(Context())
    else:
        return os.EX_OK
