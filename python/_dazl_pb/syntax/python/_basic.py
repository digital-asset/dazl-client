# Copyright (c) 2017-2022 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from io import StringIO
from typing import Iterable

__all__ = ["all_decl"]


def all_decl(__names: "Iterable[str]") -> str:
    if __names:
        with StringIO() as buf:
            buf.write("__all__ = [\n")
            for name in __names:
                buf.write(f'    "{name}",\n')
            buf.write("]\n")

            return buf.getvalue()
    else:
        return "__all__ = []  # type: ignore\n"
