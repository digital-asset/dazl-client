# Copyright (c) 2017-2022 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from typing import Collection, Union

from ..prim import DazlError, DazlWarning, Party

__all__ = ["ConfigurationError", "DazlPartyMissingError", "UnknownTemplateWarning"]


class ConfigurationError(DazlError):
    """
    Raised when a configuration error prevents a client from being started.

    .. attribute:: ConfigurationError.reasons

        A collection of reasons for a failure.
    """

    reasons: Collection[str]

    def __init__(self, reasons: Union[None, str, Collection[str]]):
        if reasons is None:
            self.reasons = []
        elif isinstance(reasons, str):
            self.reasons = [reasons]
        else:
            self.reasons = reasons


class DazlPartyMissingError(DazlError):
    """
    Error raised when a party or some information about a party is requested, and that party is not
    found.
    """

    def __init__(self, party: "Party"):
        super().__init__(f"party {party!r} does not have a defined client")
        self.party = party


class UnknownTemplateWarning(DazlWarning):
    """
    Raised when trying to do something with a template name that is unknown.
    """
