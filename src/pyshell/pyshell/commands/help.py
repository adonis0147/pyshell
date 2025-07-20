from .command import Command


class Help(Command):
    name = "help"
    description = "Show the usage of a command"

    def __call__(self, command=None):
        if not isinstance(command, Command):
            command = self.interpreter.command_manager.get_command(command, self)

        if not isinstance(command, Help):
            print(command.__class__.help())
        else:
            usage = """
Usage: help command


Commands:
"""
            for name, command in self.interpreter.command_manager.commands.items():
                usage += f"{name}           {command.description}\n"
            print(usage)
