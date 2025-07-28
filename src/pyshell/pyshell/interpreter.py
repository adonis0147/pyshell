import weakref
from code import InteractiveInterpreter
from contextlib import redirect_stderr
from io import StringIO
from typing import Callable, Optional

from pyshell.pyshell.command_manager import CommandManager
from pyshell.pyshell.context import Context


class Interpreter:

    def __init__(self, context: Context):
        self._context = context
        self._interpreter = InteractiveInterpreter(self._context)
        self._command_manager = CommandManager(weakref.ref(self))

    def read_and_execute(
        self, line_provider: Callable[[bool], str], stderr: Optional[StringIO] = None
    ):
        command = None
        lines: list[str] = []
        while True:
            first_line = len(lines) == 0
            line = line_provider(first_line)

            if first_line:
                index = line.find(" ")
                if index < 0:
                    index = len(line)

                command = self._command_manager.get_command(line[:index])
                if command is not None:
                    start = index + 1
                    line = line[start:]

                try:
                    code = self._interpreter.compile(line)
                except Exception:
                    self.showtraceback(stderr)
                    return

            lines.append(line)
            if code:
                break

            if line.strip() == "":
                lines[-1] = ""
                break

        if command is not None:
            source = f"{command.name}({'\n'.join(lines)})"
        else:
            source = "\n".join(lines)

        self.runsource(source, stderr)

    def showtraceback(self, stderr: Optional[StringIO]):
        if stderr is not None:
            with redirect_stderr(stderr):
                self._interpreter.showtraceback()
        else:
            self._interpreter.showtraceback()

    def runsource(self, source: str, stderr: Optional[StringIO]):
        if stderr is not None:
            with redirect_stderr(stderr):
                self._interpreter.runsource(source)
        else:
            self._interpreter.runsource(source)

    @property
    def context(self) -> Context:
        return self._context

    @property
    def interpreter(self) -> InteractiveInterpreter:
        return self._interpreter

    @property
    def command_manager(self) -> CommandManager:
        return self._command_manager
