# Copyright (c) 2019 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""
Utilities for dealing with the file system.
"""

import socket
import sys
from io import TextIOBase, SEEK_SET
from types import TracebackType
from typing import TextIO, Optional, Type, Iterator, Iterable, List


def read_file_bytes(file_path: Optional[str]) -> Optional[bytes]:
    """
    Read the contents of a file as ``bytes``. If ``file_path`` is ``None``, then ``None`` is
    returned instead.
    """
    if file_path is not None:
        with open(file_path, 'rb') as f:
            return f.read()
    else:
        return None


def find_free_port() -> int:
    sock = socket.socket()
    try:
        sock.bind(('', 0))
        return sock.getsockname()[1]
    finally:
        sock.close()


def is_port_alive(port: int) -> bool:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        result = sock.connect_ex(('127.0.0.1', port))
        return result == 0
    finally:
        sock.close()


class LoggingStream(TextIOBase):
    """
    A text "stream" that actually redirects to the specified logger at the specified log level.
    """
    def __init__(self, logger, log_level):
        self.logger = logger
        self.log_level = log_level
        self._buf = None  # type: Optional[str]

    def __enter__(self) -> 'LoggingStream':
        """
        Does nothing; LoggingStreams are not closeable.
        """
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Does nothing; LoggingStreams are not closeable.
        """

    @property
    def buffer(self):
        return None

    def closed(self) -> bool:
        return False

    def close(self) -> None:
        """
        Does nothing; LoggingStreams are not closeable.
        """

    def write(self, text: str) -> int:
        # weed out empty or None strings
        if not text:
            return 0

        lines = str.splitlines(text)
        trail = None if text.endswith('\n') else lines.pop()
        if lines:
            # if there is at least one line that we are definitely writing out, then grab the rest
            # of our buffer and prepend it to the first line
            if self._buf is not None:
                prefix = self._buf
                lines[0] = prefix + lines[0]
                self._buf = None

        if trail is not None:
            # if there is trailing text that we are not supposed to write, either append it to our
            # buffer in progress or create a new buffer specifically for that text
            if self._buf is not None:
                self._buf += trail
            else:
                self._buf = trail

        for line in lines:
            # now actually log the lines we were supposed to log
            self.logger.log(self.log_level, line)

        return len(text)

    def writelines(self, lines: Iterable[str]) -> None:
        for line in lines:
            if self._buf is not None:
                line = self._buf + line
                self._buf = None
            self.logger.log(self.log_level, line)


class StdoutStreamWrapper(TextIO):
    """
    Wrapper for ``sys.stdout`` that can cope with it being reassigned at will (like the ``unittest``
    module does). This allows for log output to be more usefully associated with tests.
    """

    def __enter__(self) -> TextIO:
        return sys.stdout.__enter__()

    @property
    def buffer(self):
        return sys.stdout.buffer

    def closed(self):
        return sys.stdout.closed

    def close(self) -> None:
        return sys.stdout.close()

    @property
    def name(self):
        return sys.stdout.name

    @property
    def encoding(self):
        return sys.stdout.encoding

    @property
    def errors(self):
        return sys.stdout.errors

    @property
    def mode(self):
        return sys.stdout.mode

    @property
    def newlines(self):
        return sys.stdout.newlines

    @property
    def line_buffering(self):
        return sys.stdout.line_buffering

    def fileno(self) -> int:
        return sys.stdout.fileno()

    def flush(self) -> None:
        sys.stdout.flush()

    def isatty(self) -> bool:
        return sys.stdout.isatty()

    def read(self, size: int = -1) -> str:
        return sys.stdout.read(size)

    def readable(self) -> bool:
        return sys.stdout.readable()

    def readline(self, limit: int = -1) -> str:
        return sys.stdout.readline(limit)

    def readlines(self, hint: int = -1) -> List[str]:
        return sys.stdout.readlines(hint)

    def seek(self, offset: int, whence: int = SEEK_SET) -> int:
        return sys.stdout.seek(offset, whence)

    def seekable(self) -> bool:
        return sys.stdout.seekable()

    def tell(self) -> int:
        return sys.stdout.tell()

    def truncate(self, size: Optional[int] = None) -> int:
        return sys.stdout.truncate(size)

    def writable(self) -> bool:
        return sys.stdout.writable()

    def write(self, s: str) -> int:
        return sys.stdout.write(s)

    def writelines(self, lines: Iterable[str]) -> None:
        return sys.stdout.writelines(lines)

    def __next__(self) -> str:
        return next(sys.stdout)

    def __iter__(self) -> Iterator[str]:
        return iter(sys.stdout)

    def __exit__(self, t: Optional[Type[BaseException]], value: Optional[BaseException],
                 traceback: Optional[TracebackType]) -> bool:
        return sys.stdout.__exit__(t, value, traceback)
