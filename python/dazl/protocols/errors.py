# Copyright (c) 2017-2022 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
from ..prim import DazlError

__all__ = [
    "ConnectionTimeoutError",
    "UserTerminateRequest",
    "StreamError",
    "ProtocolWarning",
    "CallbackReturnWarning",
]


class ConnectionTimeoutError(DazlError):
    """
    Raised when a connection failed to be established before the connection timeout elapsed.
    """


class UserTerminateRequest(DazlError):
    """
    Raised when the user has initiated a request to terminate the application.
    """


class StreamError:
    """
    An error that arises when trying to read from a query stream.
    """


class ProtocolWarning(Warning):
    """
    Warnings that are raised when dazl detects incompatibilities between the Ledger API server-side
    implementation and dazl.
    """
