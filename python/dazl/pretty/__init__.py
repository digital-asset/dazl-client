# Copyright (c) 2017-2022 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""
:mod:`dazl.pretty` package
==========================

This module contains utilities for pretty-printing various types in dazl.

.. automodule:: dazl.pretty.render_daml
.. automodule:: dazl.pretty.util
"""

from typing import TYPE_CHECKING, Optional, Type

from ..damlast.protocols import SymbolLookup
from ._render_base import PrettyPrintBase, pretty_print_syntax  # type: ignore
from .options import PrettyOptions
from .render_csharp import CSharpPrettyPrint  # type: ignore
from .render_daml import DEFAULT_PRINTER as DAML_PRETTY_PRINTER, DamlPrettyPrinter  # type: ignore
from .render_python import PythonPrettyPrint  # type: ignore
from .util import maybe_parentheses

if TYPE_CHECKING:
    from .pygments_daml_lexer import DAMLLexer as _DAMLLexer_TYPE


__all__ = ["get_pretty_printer", "DAMLLexer", "ALL_PRINTER_TYPES", "PrettyOptions"]


def _import_daml_lexer() -> "Optional[Type[_DAMLLexer_TYPE]]":
    # pygments isn't absolutely required, but if it's loaded, also provide our lexer
    try:
        from .pygments_daml_lexer import DAMLLexer

        return DAMLLexer
    except ImportError:
        return None


DAMLLexer = _import_daml_lexer()


ALL_PRINTER_TYPES = [CSharpPrettyPrint, DamlPrettyPrinter, PythonPrettyPrint]  # type: ignore


# noinspection PyShadowingBuiltins,PyShadowingNames
def get_pretty_printer(
    format: str, options: "PrettyOptions", lookup: "SymbolLookup"
) -> "Optional[PrettyPrintBase]":
    for printer in ALL_PRINTER_TYPES:
        if printer.syntax.startswith(format):
            return printer(lookup, options)
    return None
