from .command import Command


class Hello(Command):

    def __init__(self, name):
        super().__init__(name)

    def __call__(self):
        print("Hello, world!")
