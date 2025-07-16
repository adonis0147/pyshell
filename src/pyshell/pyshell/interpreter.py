from code import InteractiveInterpreter

from prompt_toolkit import PromptSession

from .command_manager import CommandManager


class Interpreter:

    def __init__(self):
        self._interpreter = InteractiveInterpreter()
        self._command_manager = CommandManager(self._interpreter)

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
