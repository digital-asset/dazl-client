# Copyright (c) 2017-2022 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""
Utilities for working with the built-in `logging` module.

This module will be removed soon!
"""
import logging
import warnings

from .._logging import VERBOSE, configure

__all__ = ["VERBOSE", "setup_default_logger"]


def setup_default_logger(level=logging.INFO):
    """
    Sets up a default logger with sensible defaults.

    This function is deprecated, and there is no replacement; you should instead configure your own
    logging output as suitable for your needs (``logging.basicConfig()`` may suffice).
    """
    warnings.warn("dazl.setup_default_logger is deprecated", DeprecationWarning, stacklevel=2)
    configure(level)
