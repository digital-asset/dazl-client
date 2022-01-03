# Copyright (c) 2017-2022 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import os
from threading import current_thread, main_thread
from typing import Optional

from ..util.enum import OrderedEnum


class RunLevel(OrderedEnum):
    """
    The possible running modes for an :class:`Invoker`. Invokers generally progress from
    lower-numbered run levels to higher-numbered run levels.
    """

    RUN_FOREVER = 0
    RUN_UNTIL_IDLE = 1
    TERMINATE_GRACEFULLY = 2
    TERMINATE_IMMEDIATELY = 3
    STOPPED = 4


def validate_install_signal_handlers(user_install_signal_handlers: "Optional[bool]" = None) -> bool:
    if user_install_signal_handlers is None:
        # The default behavior for signal handling is to suppress if we are already running in a
        # background thread or we are being run within unit tests.
        return "PYTEST_CURRENT_TEST" not in os.environ and current_thread() is main_thread()

    if user_install_signal_handlers and current_thread() is not main_thread():
        # The user WANTS signal handlers, but we know the registration call will fail
        raise RuntimeError("cannot install signal handlers when not on the main thread")

    return user_install_signal_handlers
