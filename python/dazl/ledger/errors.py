# Copyright (c) 2017-2021 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

__all__ = ["CallbackReturnWarning", "ProtocolWarning"]


class CallbackReturnWarning(Warning):
    """
    Raised when a user callback on a stream returns a value. These objects have no meaning and are
    ignored by dazl.

    This warning is raised primarily because older versions of dazl interpreted returning commands
    from a callback as a request to send commands to the underlying ledger, and this is not
    supported in newer APIs.
    """


class ProtocolWarning(Warning):
    """
    Warnings that are raised when dazl detects incompatibilities between the Ledger API server-side
    implementation and dazl.
    """
