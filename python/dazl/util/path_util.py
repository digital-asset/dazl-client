# Copyright (c) 2017-2022 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
from os import PathLike, fspath
from pathlib import Path
from typing import Union
import warnings

__all__ = ["pathify"]


def pathify(path: "Union[str, Path, PathLike]") -> Path:
    """
    Convert an object that could be a :class:`Path` into a :class:`Path`.
    """
    warnings.warn("pathify is deprecated; use os.fspath instead", DeprecationWarning, stacklevel=2)
    return Path(fspath(path))
