from pyshell.pyshell.commands import commands_meta


class CommandManager:

    def __init__(self, interpreter):
        self._commands = {}

        for name, cls in commands_meta:
            command = cls(name, interpreter)
            self._commands[name] = command
            interpreter().context[name] = command

    @property
    def commands(self):
        return self._commands

    def get_command(self, name, default=None):
        return self._commands.get(name, default)
