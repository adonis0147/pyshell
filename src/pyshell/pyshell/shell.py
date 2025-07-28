import os
from pathlib import Path

from prompt_toolkit import PromptSession
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory
from prompt_toolkit.completion import FuzzyCompleter
from prompt_toolkit.history import FileHistory
from prompt_toolkit.lexers import PygmentsLexer
from prompt_toolkit.shortcuts import CompleteStyle
from prompt_toolkit.styles.pygments import style_from_pygments_cls
from pygments.lexers import PythonLexer
from pygments.styles import get_style_by_name

import pyshell.pyshell.key_bindings as key_bindings
from pyshell.pyshell.completion import InterpreterCompleter
from pyshell.pyshell.context import Context
from pyshell.pyshell.interpreter import Interpreter


class InteractiveShell:
    # https://patorjk.com/software/taag/#p=display&f=Slant&t=PyShell
    welcome: str = r"""
    ____        _____ __         ____
   / __ \__  __/ ___// /_  ___  / / /
  / /_/ / / / /\__ \/ __ \/ _ \/ / /
 / ____/ /_/ /___/ / / / /  __/ / /
/_/    \__, //____/_/ /_/\___/_/_/
      /____/
"""

    def __init__(self, context: Context, style: str = "monokai"):
        self._context = context

        prompt_style = style_from_pygments_cls(get_style_by_name(style))
        prompt_style.style_rules.extend(InterpreterCompleter.style.items())

        self._session: PromptSession = PromptSession(
            style=prompt_style,
            lexer=PygmentsLexer(PythonLexer),
            key_bindings=key_bindings.bindings,
            auto_suggest=AutoSuggestFromHistory(),
            history=FileHistory(Path.home() / ".pyshell_history"),
            completer=FuzzyCompleter(InterpreterCompleter(self._context)),
            complete_style=CompleteStyle.MULTI_COLUMN,
        )

    def run(self) -> int:
        print(InteractiveShell.welcome)

        interpreter = Interpreter(self._context)
        while True:
            try:
                interpreter.read_and_execute(
                    lambda first_line: self._session.prompt(
                        "pyshell> " if first_line else "       > "
                    )
                )
            except KeyboardInterrupt:
                continue
            except EOFError:
                break

        print("GoodBye!")
        return os.EX_OK
