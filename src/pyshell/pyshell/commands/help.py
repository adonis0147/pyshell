from tabulate import tabulate

from .command import Command


class Help(Command):
    name = "help"
    description = "Show the usage"

    def __call__(self, command=None):
        if not isinstance(command, Command):
            command = self.interpreter.command_manager.get_command(command, self)

        if not isinstance(command, Help):
            print(command.__class__.help())
        else:
            usage = """
Usage: help command


Commands:"""
            print(usage)
            commands = []
            for name, command in self.command_manager.commands.items():
                commands.append([name, "", "", "", "", command.__class__.description])
            print(tabulate(commands, headers=[], tablefmt="plain"))
