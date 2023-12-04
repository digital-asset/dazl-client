# Copyright (c) 2017-2024 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

import logging

__all__ = ["Formatter", "initialize"]

grey = "\x1b[38;20m"
yellow = "\x1b[33;20m"
red = "\x1b[31;20m"
bold_red = "\x1b[31;1m"
reset = "\x1b[0m"
format = "%(asctime)s.%(msecs)03d %(levelname)s (%(filename)s:%(lineno)d) %(message)s "


class Formatter(logging.Formatter):
    FORMATS = {
        logging.DEBUG: grey + format + reset,
        logging.INFO: grey + format + reset,
        logging.WARNING: yellow + format + reset,
        logging.ERROR: red + format + reset,
        logging.CRITICAL: bold_red + format + reset,
    }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt, datefmt=self.datefmt)
        return formatter.format(record)


def initialize(log_level: str) -> logging.Logger:
    numeric_level = getattr(logging, log_level.upper(), None)
    if not isinstance(numeric_level, int):
        raise ValueError("Invalid log level: %s" % log_level)

    logger = logging.getLogger("_dazl")
    logger.setLevel(log_level.upper())

    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)

    # this is not a long-running process, so save space and only output the time without the date
    ch.setFormatter(Formatter(datefmt="%H:%M:%S"))

    logger.addHandler(ch)
    return logger
