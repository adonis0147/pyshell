import os
import sys
from io import StringIO

from pyshell.pyshell.context import Context
from pyshell.pyshell.interpreter import Interpreter


class Executor:

    def __init__(self, context: Context):
        self._context = context

    def run(self) -> int:
        interpreter = Interpreter(self._context)
        while True:
            try:
                stderr = StringIO()
                interpreter.read_and_execute(self._get_line, stderr)

                if stderr.getvalue() != "":
                    raise RuntimeError(stderr.getvalue())
            except EOFError:
                break
            except RuntimeError as e:
                print(e, file=sys.stderr)
                return os.EX_SOFTWARE
        return os.EX_OK

    def _get_line(self, first_line) -> str:
        line = sys.stdin.readline()

        if first_line and line == "":
            raise EOFError

        return line
