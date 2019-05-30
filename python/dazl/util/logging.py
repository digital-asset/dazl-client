# Copyright (c) 2019 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""
Utilities for working with the built-in `logging` module.
"""
import logging
import threading
from typing import cast

from ..util.io import StdoutStreamWrapper

VERBOSE = 5

LOG_LOCK = threading.Lock()
_default_logger_init = False


def setup_default_logger(level=logging.INFO):
    """
    Sets up a default logger with sensible defaults.
    """
    root = logging.getLogger()
    global _default_logger_init
    if not _default_logger_init:
        _default_logger_init = True
    else:
        root.warning('setup_default_logger being called more than once!')
        return

    logging.captureWarnings(True)

    root.setLevel(level)
    stream_handler = logging.StreamHandler(StdoutStreamWrapper())
    formatter = logging.Formatter("[%(levelname)7s] %(asctime)s | %(name)-7s | %(message)s")
    stream_handler.setFormatter(formatter)
    root.addHandler(stream_handler)


def log_verbose(logger: 'logging.Logger', msg, *args, **kwargs) -> None:
    return logger.log(5, msg, *args, **kwargs)


class _LoggerWithVerbose:
    def verbose(self, msg, *args, **kwargs) -> None:
        logger = cast(logging.Logger, self)
        return log_verbose(logger, msg, *args, **kwargs)


class LoggerWithVerbose(logging.Logger, _LoggerWithVerbose):
    pass


logging.addLevelName(VERBOSE, 'VERBOSE')
