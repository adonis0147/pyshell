import sys

from pyshell.pyshell.context import Context
from pyshell.pyshell.executor import Executor
from pyshell.pyshell.shell import InteractiveShell


def main() -> int:
    context = Context()
    if sys.stdin.isatty():
        return InteractiveShell(context, "material").run()
    else:
        return Executor(context).run()
