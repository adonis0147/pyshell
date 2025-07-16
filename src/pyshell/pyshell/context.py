from .utils import singleton


@singleton
class Context(dict):
    pass
