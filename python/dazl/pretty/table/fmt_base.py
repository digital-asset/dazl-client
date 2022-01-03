# Copyright (c) 2017-2022 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from .model import Formatter

__all__ = ["DEFAULT_FORMATTER_NAME", "get_formatter"]

DEFAULT_FORMATTER_NAME = "pretty"


def get_formatter(fmt) -> "Formatter":
    """
    Return a formatter of the specified name.
    """
    if fmt is None:
        fmt = DEFAULT_FORMATTER_NAME

    if fmt == "json":
        from .fmt_json import JsonFormatter

        return JsonFormatter()
    elif fmt == "pretty":
        from .fmt_pretty import PrettyFormatter

        return PrettyFormatter()
    else:
        raise ValueError("unknown format: {}".format(fmt))
