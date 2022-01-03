# Copyright (c) 2017-2022 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""
Logging utilities used in `dazl`.

This is an internal API and not meant to be used directly outside of dazl; symbols declared in this
file may change at any time.
"""

from functools import partial
import logging
import sys
from time import time
from typing import Type, cast

__all__ = ["LOG", "VERBOSE", "configure"]

# A custom logging level below "DEBUG". This is used within dazl for messages that are rarely
# important enough to be printed, even within tests, but still occasionally have value when
# debugging particular blocks of code.
VERBOSE = 5
logging.addLevelName(VERBOSE, "VERBOSE")

# If a custom logger type was set before dazl was loaded, respect it by using it as our logger's
# base class.
# noinspection PyTypeChecker
Logger = logging.getLoggerClass()  # type: Type[logging.Logger]


class ExtendedLogger(Logger):  # type: ignore
    """
    A logger with additional utility logging functions used within dazl.
    """

    def verbose(self, msg, *args, **kwargs):
        """
        Log a message with level ``VERBOSE`` on this logger.
        """
        self.log(VERBOSE, msg, *args, **kwargs)

    def verbose_timed(self, msg, *args, **kwargs) -> "TimedLogMessageContext":
        """
        Log a message with level ``VERBOSE`` on the logger, additionally annotating the log message
        with the time it took to complete the block.
        """
        return TimedLogMessageContext(self, VERBOSE, msg, args, kwargs)

    def debug_timed(self, msg, *args, **kwargs) -> "TimedLogMessageContext":
        """
        Log a message with level ``DEBUG`` on the logger, additionally annotating the log message
        with the time it took to complete the block.
        """
        return TimedLogMessageContext(self, logging.DEBUG, msg, args, kwargs)

    def info_timed(self, msg, *args, **kwargs) -> "TimedLogMessageContext":
        """
        Log a message with level ``INFO`` on the logger, additionally annotating the log message
        with the time it took to complete the block.
        """
        return TimedLogMessageContext(self, logging.INFO, msg, args, kwargs)


# Create our Logger with our special type that has all of our goodies.
logging.setLoggerClass(ExtendedLogger)
LOG = cast(ExtendedLogger, logging.getLogger("dazl"))

# There is a chance that someone instantiated a logger using our name already. If that's the case,
# then it is too late to specify the actual class instance used and `LOG` will not have the
# functions declared on it that we expect. So make sure that we specifically add methods to _our_
# logger.
#
# An alternate implementation would have been to simply assign our custom logging functions directly
# to an instance logger without playing games with `logger.setLoggerClass`; but we don't, because
# mypy/IDEs won't understand what is going on; we'd be using "reflection" instead of giving
# mypy/IDEs a simple class (ExtendedLogger) to key off of.
for field in dir(ExtendedLogger):
    if not field.startswith("__") and not hasattr(LOG, field):
        setattr(LOG, field, partial(getattr(ExtendedLogger, field), LOG))

# This is essentially a runtime assertion that our logging functions have been defined properly.
LOG.verbose("dazl logging has been loaded.")

# Restore the original Logger type.
logging.setLoggerClass(Logger)


class TimedLogMessageContext:
    """
    A simple ContextManager that logs a message at the specified logging level, additionally with
    timing information. If an exception is thrown in the block, that exception is instead logged.
    """

    __slots__ = "logger", "log_level", "msg", "args", "kwargs", "start"

    def __init__(self, logger, log_level, msg, args, kwargs):
        self.logger = logger
        self.log_level = log_level
        self.msg = msg
        self.args = args
        self.kwargs = kwargs
        self.start = None

    def __enter__(self):
        self.start = time()

    def __exit__(self, exc_type, exc_val, exc_tb):
        elapsed_ms = (time() - self.start) * 1000.0
        if exc_type is not None:
            self.logger.exception(
                self.msg + " (%0.2f ms)",
                *self.args,
                elapsed_ms,
                exc_info=(exc_type, exc_val, exc_tb),
                **self.kwargs
            )
        else:
            self.logger.log(
                self.log_level, self.msg + " (%0.2f ms)", *self.args, elapsed_ms, **self.kwargs
            )


did_configure = False


def configure(level=logging.INFO):
    """
    Set up a default logger format and stream handler with sensible defaults.
    """
    root = logging.getLogger()
    global did_configure
    if not did_configure:
        did_configure = True
    else:
        root.warning("configure being called more than once!")
        return

    logging.captureWarnings(True)

    root.setLevel(level)
    stream_handler = logging.StreamHandler(sys.stdout)
    formatter = logging.Formatter("[%(levelname)7s] %(asctime)s | %(name)-7s | %(message)s")
    stream_handler.setFormatter(formatter)
    root.addHandler(stream_handler)
