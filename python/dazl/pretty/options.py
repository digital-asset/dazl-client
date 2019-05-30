# Copyright (c) 2019 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""
This module contains pretty-print/formatting utilities.
"""

from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class PrettyOptions:
    """
    Display options for pretty-printing DAML ASTs.

    Instance attributes:

    .. attribute:: PrettyOptions.column_width

        The maximum number of columns to use when rendering text, or ``None`` if lines should not
        wrap.

    .. attribute:: PrettyOptions.show_hidden_types

        ``True`` to render built-in DAML types defined in ``DA.Internal`` or ``GHC`` and specially
        generated names.

    .. attribute:: PrettyOptions.format

        A string that identifies the target language to render.
    """

    column_width: Optional[int] = None
    show_hidden_types: bool = False
    format: str = 'daml'
