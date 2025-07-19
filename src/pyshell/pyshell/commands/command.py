class Command:

    def __init__(self, name: str, interpreter, description: str):
        self._name = name
        self._interpreter = interpreter
        self._description = description

    @staticmethod
    def help():
        raise NotImplementedError

    def __call__(self, *args, **kwargs):
        raise NotImplementedError

    @property
    def name(self):
        return self._name

    @property
    def interpreter(self):
        return self._interpreter()

    @property
    def description(self):
        return self._description
