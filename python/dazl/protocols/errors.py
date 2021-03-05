# Copyright (c) 2017-2021 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
from ..prim import DazlError

__all__ = ["ConnectionTimeoutError", "UserTerminateRequest"]


class ConnectionTimeoutError(DazlError):
    """
    Raised when a connection failed to be established before the connection timeout elapsed.
    """


class UserTerminateRequest(DazlError):
    """
    Raised when the user has initiated a request to terminate the application.
    """
