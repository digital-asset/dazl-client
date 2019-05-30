# Copyright (c) 2019 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from pathlib import Path
from typing import Union


def pathify(path: Union[str, Path]) -> Path:
    """
    Convert an object that could be a :class:`Path` into a :class:`Path`.

    :param path:
    :return:
    """
    if isinstance(path, Path):
        return path
    elif isinstance(path, str):
        return Path(path)
    else:
        raise ValueError(f'path must be a str or Path (got {path!r} instead)')
