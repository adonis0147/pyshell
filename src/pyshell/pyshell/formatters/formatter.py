import textwrap
from typing import Any, Iterable, Optional

import tabulate


class Formatter:

    def __init__(self, widths: Optional[Iterable[int]] = None):
        self._widths = widths

    def format(self, data: Iterable[Iterable[Any]], *args, **kwargs) -> str:
        preserve_whitespace = tabulate.PRESERVE_WHITESPACE
        if self._widths is not None:
            tabulate.PRESERVE_WHITESPACE = True
            data = self._transform_row(data)

        text = tabulate.tabulate(data, *args, **kwargs)

        tabulate.PRESERVE_WHITESPACE = preserve_whitespace
        return text

    def _transform_row(self, data: Iterable[Iterable[Any]]) -> Iterable[Iterable[Any]]:
        for row in data:
            yield self._transform_column(row)

    def _transform_column(self, row: Iterable[Any]) -> Iterable[Any]:
        assert self._widths
        for column, width in zip(row, self._widths):
            yield self._fit_width(column, width)

    def _fit_width(self, text: str, width: int) -> str:
        return "\n".join(
            map(lambda line: line.ljust(width), textwrap.wrap(str(text), width=width))
        )
