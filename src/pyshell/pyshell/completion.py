import re
import rlcompleter
from typing import Iterable

from prompt_toolkit.completion import CompleteEvent, Completer, Completion
from prompt_toolkit.document import Document

from pyshell.pyshell.context import Context


class InterpreterCompleter(Completer):
    style = {
        "completion-menu": "bg:#e6db74",
        "completion-menu.completion": "bg:#e6db74 #272a30",
        "completion-menu.completion.current": "bg:#272a30 #fd971f bold",
    }

    def __init__(self, context: Context):
        self._context = context
        self._rlcompleter = rlcompleter.Completer(self._context)

    def get_completions(
        self, document: Document, complete_event: CompleteEvent
    ) -> Iterable[Completion]:
        text = document.text_before_cursor

        if text.endswith(" "):
            return

        word = document.get_word_before_cursor(WORD=True)

        if word.endswith("."):
            found = re.search(r"[\w_][\w\d_\.]*$", word)
            if found:
                word = found.group(0)
            matches = self._rlcompleter.attr_matches(word)
        else:
            matches = list(
                filter(
                    lambda key: not key.startswith("__") and key.startswith(word),
                    self._context.keys(),
                )
            )

        for match in matches:
            yield Completion(match.rstrip("()"), start_position=-len(word))
