from .command import Command


class Help(Command):
    @staticmethod
    def help():
        return """
"""

    def __call__(self, name: str | None = None):
        command = self.interpreter.command_manager.get_command(name, self)
        print(command.__class__.help())
