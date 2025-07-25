import os
from pathlib import Path

from prompt_toolkit import PromptSession
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory
from prompt_toolkit.history import FileHistory
from prompt_toolkit.lexers import PygmentsLexer
from prompt_toolkit.styles.pygments import style_from_pygments_cls
from pygments.lexers import PythonLexer
from pygments.styles import get_style_by_name

import pyshell.pyshell.key_bindings as key_bindings
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

    def __init__(self, style: str = "monokai"):
        prompt_style = style_from_pygments_cls(get_style_by_name(style))

        self.session: PromptSession = PromptSession(
            style=prompt_style,
            lexer=PygmentsLexer(PythonLexer),
            auto_suggest=AutoSuggestFromHistory(),
            key_bindings=key_bindings.bindings,
            history=FileHistory(Path.home() / ".pyshell_history"),
        )
        pass

    def run(self, context: Context) -> int:
        print(InteractiveShell.welcome)

        interpreter = Interpreter(context)
        while True:
            try:
                interpreter.read_and_execute(self.session, "pyshell> ", "       > ")
            except KeyboardInterrupt:
                continue
            except EOFError:
                break

        print("GoodBye!")
        return os.EX_OK
