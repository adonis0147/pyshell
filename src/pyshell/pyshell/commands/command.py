from typing import TYPE_CHECKING, Optional
from weakref import ReferenceType

from pyshell.pyshell.context import Context

if TYPE_CHECKING:
    from pyshell.pyshell.command_manager import CommandManager
    from pyshell.pyshell.interpreter import Interpreter


class Command:

    def __init__(self, interpreter: ReferenceType[Interpreter]):
        self._interpreter = interpreter

    @staticmethod
    def help():
        raise NotImplementedError

    def __call__(self, *args, **kwargs):
        raise NotImplementedError

    @property
    def name(self):
        return self.__class__.name

    @property
    def interpreter(self) -> Optional[Interpreter]:
        return self._interpreter()

    @property
    def command_manager(self) -> CommandManager:
        assert self.interpreter
        return self.interpreter.command_manager

    @property
    def context(self) -> Context:
        assert self.interpreter
        return self.interpreter.context
