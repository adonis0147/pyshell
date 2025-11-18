from .command import Command


class Exit(Command):
    name = "exit"
    description = "Exit"

    @staticmethod
    def help():
        return """
Usage: exit
"""

    def __call__(self):
        exit()
