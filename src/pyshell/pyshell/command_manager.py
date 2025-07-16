from .commands import commands_meta


class CommandManager:

    def __init__(self, interpreter):
        self._commands = {}

        for name, cls in commands_meta:
            command = cls(name)
            self._commands[name] = command
            interpreter.locals[name] = command

    @property
    def commands(self):
        return self._commands

    def get_command(self, name):
        return self._commands.get(name, None)
