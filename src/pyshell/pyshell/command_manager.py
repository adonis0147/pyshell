import inspect

import pyshell.pyshell.commands as commands
from pyshell.pyshell.commands.command import Command


class CommandManager:

    def __init__(self, interpreter):
        self._commands = {}

        for _, cls in inspect.getmembers(commands, inspect.isclass):
            if issubclass(cls, Command):
                command = cls(interpreter)
                self._commands[cls.name] = command
                interpreter().context[cls.name] = command

    @property
    def commands(self) -> dict[str, Command]:
        return self._commands

    def get_command(self, name, default=None):
        return self._commands.get(name, default)
