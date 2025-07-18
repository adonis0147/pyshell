import weakref
from code import InteractiveInterpreter

from prompt_toolkit import PromptSession

from pyshell.pyshell.command_manager import CommandManager
from pyshell.pyshell.context import Context


class Interpreter:

    def __init__(self):
        self._context = Context()
        self._interpreter = InteractiveInterpreter(self._context)
        self._command_manager = CommandManager(weakref.ref(self))

    def read_and_execute(self, session: PromptSession, prompt: str, more_prompt: str):
        command = None
        lines: list[str] = []
        while True:
            first_line = len(lines) == 0
            line = session.prompt(prompt if first_line else more_prompt)

            if first_line:
                index = line.find(" ")
                if index < 0:
                    index = len(line)

                command = self._command_manager.get_command(line[:index])
                if command is not None:
                    start = index + 1
                    line = line[start:]
                code = self._interpreter.compile(line)

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

        self._interpreter.runsource(source)

    @property
    def context(self):
        return self._context

    @property
    def interpreter(self):
        return self._interpreter

    @property
    def command_manager(self):
        return self._command_manager
