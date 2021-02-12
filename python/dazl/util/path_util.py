# Copyright (c) 2017-2021 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from os import PathLike
from pathlib import Path
from typing import Union


def pathify(path: "Union[str, Path, PathLike]") -> Path:
    """
    Convert an object that could be a :class:`Path` into a :class:`Path`.
    """
    if isinstance(path, Path):
        return path
    elif isinstance(path, PathLike):
        return Path(path)
    else:
        raise ValueError(f"path must be a str or Path (got {path!r} instead)")
