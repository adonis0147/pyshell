class Command:

    def __init__(self, interpreter):
        self._interpreter = interpreter

    @staticmethod
    def help():
        raise NotImplementedError

    def __call__(self, *args, **kwargs):
        raise NotImplementedError

    @property
    def interpreter(self):
        return self._interpreter()

    @property
    def command_manager(self):
        return self.interpreter.command_manager

    @property
    def context(self):
        return self.interpreter.context
