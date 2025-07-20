import inspect

import pyshell.pyshell.commands as commands


class CommandManager:

    def __init__(self, interpreter):
        self._commands = {}

        for _, cls in inspect.getmembers(commands, inspect.isclass):
            if issubclass(cls, commands.command.Command):
                command = cls(interpreter)
                self._commands[cls.name] = command
                interpreter().context[cls.name] = command

    @property
    def commands(self):
        return self._commands

    def get_command(self, name, default=None):
        return self._commands.get(name, default)
