class Command:

    def __init__(self, name: str, interpreter):
        self._name = name
        self._interpreter = interpreter

    @property
    def name(self):
        return self._name

    @property
    def interpreter(self):
        return self._interpreter()

    @staticmethod
    def help():
        raise NotImplementedError

    def __call__(self, *args, **kwargs):
        raise NotImplementedError
