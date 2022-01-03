# Copyright (c) 2017-2022 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""
Utilities for dealing with the file system.
"""

from io import BufferedIOBase
from pathlib import Path
import socket
from typing import BinaryIO, Optional, Union, overload


@overload
def get_bytes(_: None) -> None:
    ...


@overload
def get_bytes(_: "Union[bytes, str, Path, BinaryIO]") -> bytes:
    ...


def get_bytes(src):
    """
    Read the contents of a file as ``bytes``. If ``src`` is ``None``, then ``None`` is returned
    instead.
    """
    if src is None:
        return None
    elif isinstance(src, str):
        with open(src, "rb") as f:
            return f.read()
    elif isinstance(src, bytes):
        return src
    elif isinstance(src, Path):
        return src.read_bytes()
    elif isinstance(src, BufferedIOBase):
        return src.read(-1)
    else:
        raise ValueError("src must be a string path, a Path, or a BytesIO")


def read_file_bytes(file_path: Optional[str]) -> Optional[bytes]:
    if file_path is not None:
        with open(file_path, "rb") as f:
            return f.read()
    else:
        return None


def find_free_port() -> int:
    sock = socket.socket()
    try:
        sock.bind(("", 0))
        return sock.getsockname()[1]
    finally:
        sock.close()


def is_port_alive(port: int) -> bool:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        result = sock.connect_ex(("127.0.0.1", port))
        return result == 0
    finally:
        sock.close()


def find_nearest_ancestor(file_name: str, relative_to: Union[str, Path]) -> "Optional[Path]":
    """
    Return a path to a file that has the specified file name, or ``None`` if no ancestor could be
    found.

    :param file_name: The name of the file to search for.
    :param relative_to: The directory at which to begin the search.
    :return: A :class:`Path` that matches the specified file name.
    """
    if relative_to is None:
        raise ValueError("A relative_to path is required")

    relative_to = Path(relative_to)
    if relative_to.is_file():
        relative_to = relative_to.parent

    while True:
        candidate = relative_to / file_name
        if candidate.exists():
            return candidate
        else:
            new_relative_to = relative_to.parent
            if relative_to == new_relative_to:
                # We can't walk up the tree any more, so we couldn't find the file we were looking for
                return None
            else:
                relative_to = new_relative_to
