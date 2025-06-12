# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from datetime import timedelta
import sys
from typing import Collection, Literal, Optional, TypedDict

from ..prim import Parties, Party, TimeDeltaLike, to_timedelta
from .auth import TokenOrTokenProvider, get_token, parse_token

if sys.version_info >= (3, 11):
    from typing import Self, assert_never
else:
    from typing_extensions import Self, assert_never

__all__ = [
    "CallParameters",
    "ReadCallParameters",
    "WriteCallParameters",
    "AnyCallParameters",
    "CallContext",
    "CachedParameters",
    "ConnectionParameters",
]


class CallParameters(TypedDict):
    token: Optional[TokenOrTokenProvider]
    timeout: Optional[TimeDeltaLike]


class ReadCallParameters(CallParameters):
    read_as: Optional[Parties]
    user_id: Optional[str]


class WriteCallParameters(ReadCallParameters):
    workflow_id: Optional[str]
    command_id: Optional[str]
    act_as: Optional[Parties]
    application_name: Optional[str]


class AnyCallParameters(TypedDict, total=False):
    """
    AnyCallParameters is the superset of all possible arguments that can be specified at
    call time.

    Currently, this is equivalent to WriteCallParameters, but we define a new type to
    clarify the intent of code.
    """

    token: Optional[TokenOrTokenProvider]
    timeout: Optional[TimeDeltaLike]
    read_as: Optional[Parties]
    user_id: Optional[str]
    workflow_id: Optional[str]
    command_id: Optional[str]
    act_as: Optional[Parties]
    application_name: Optional[str]


class CachedParameters(TypedDict):
    """
    Parameters that are cached between successive calls. The fields of this type are
    _similar_, but not exactly the same as :class:`AnyCallParameters` and
    :class:`ConnectionParameters`.
    """

    read_as: Optional[Collection[Party]]
    act_as: Optional[Collection[Party]]
    ledger_id: Optional[str]
    user_id_or_application_name: Optional[str]
    token: Optional[str]


class ConnectionParameters(TypedDict):
    """
    Parameters that are supplied at connection construction time.
    """

    read_as: Optional[Collection[Party]]
    act_as: Optional[Collection[Party]]
    ledger_id: Optional[str]
    user_id_or_application_name: Optional[str]
    token: Optional[TokenOrTokenProvider]
    timeout: Optional[timedelta]


class CallContext:
    """
    Contextual information as it relates to a single logical Ledger API call.
    """

    @classmethod
    def compute(
        cls,
        call: AnyCallParameters,
        cache: Optional[CachedParameters],
        connection: ConnectionParameters,
    ) -> Self:
        """
        Compute the values that should be effective for a logical Ledger API call, based on what
        was supplied at call time, previously cached values, or at connection time.

        Data is consulted in the following priority:
         * values supplied at _call_ time always win
            * mutually related fields (read-as/act-as/token/user-id/application-name) must be
              consistent if multiple are specified
         * values that come from the cache come next, but only if the token (as computed from
           either the current call's ``token`` or the current connection's ``token`` value) is
           the same token as the previous call; otherwise, the cache is ignored
         * values that come from the connection level
         * a handful of values (``timeout``, ``application_name``) are defaulted here if not
           specified elsewhere.

        :param call:
        :param cache:
        :param connection:
        :return:
        """
        # compute the effective token for this call
        token = get_token(call.get("token"))
        token_level: Literal["call", "connection"] = "call"
        if token is None:
            token = get_token(connection.get("token"))
            token_level = "connection"

        # depending on whether read_as/act_as/ledger_id/user_id/application_name are specified,
        # the token itself also participates in defaulting values
        parsed_token = parse_token(token) if token is not None else None

        # if we were supplied a cache, but it differs from the token that we computed,
        # then throw away the cache because we can't use any of its values
        if cache is not None and cache.get("token") != token:
            cache = None

        ledger_id = connection.get("ledger_id")
        if ledger_id is None and parsed_token is not None and parsed_token.token_version == 1:
            # Daml v1 tokens happen to have ledger ID stored in them, so the token can be used
            # to identify the Ledger ID
            ledger_id = parsed_token.ledger_id

        user_id_or_application_name: Optional[str] = None

        read_as = call.get("read_as")
        if read_as is None and cache is not None:
            read_as = cache.get("read_as")
        if read_as is None:
            read_as = connection.get("read_as")

        act_as = call.get("act_as")
        if act_as is None and cache is not None:
            act_as = cache.get("act_as")
        if act_as is None:
            act_as = connection.get("act_as")

        if read_as is None and act_as is None:
            # if we can't find a read-as/act-as at the call site, in our cache, or at the
            # connection level, maybe the token supplies the information we need
            if parsed_token is not None and parsed_token.token_version == 1:
                read_as = parsed_token.read_as
                act_as = parsed_token.act_as

        # In Daml 2, application_name became overloaded to _also_ mean user_id.
        # Prefer that people use user_id, as that's going to be the standard in Daml 3.
        call_user_id = call.get("user_id")
        if call_user_id is not None:
            if call.get("application_name") is not None:
                raise ValueError("cannot specify user_id and application_name at the same time")
            user_id_or_application_name = call_user_id
        if user_id_or_application_name is None and cache is not None:
            user_id_or_application_name = cache.get("user_id_or_application_name")
        if user_id_or_application_name is None:
            user_id_or_application_name = connection.get("user_id_or_application_name")
        if user_id_or_application_name is None and parsed_token is not None:
            # as a last resort, if we can't find a user_id/application_id at any level,
            # try to extract it from the token
            match parsed_token.token_version:
                case 1:
                    user_id_or_application_name = parsed_token.application_name
                case 2:
                    user_id_or_application_name = parsed_token.user_id
                case _:
                    assert_never(parsed_token.token_version)

        # compute the effective timeout for this call
        call_timeout = call.get("timeout")
        if call_timeout is not None:
            timeout = to_timedelta(call_timeout)
        else:
            connection_timeout = connection.get("timeout")
            if connection_timeout is not None:
                timeout = to_timedelta(connection_timeout)
            else:
                timeout = timedelta(seconds=30)

        return cls(
            workflow_id=call.get("workflow_id"),
            command_id=call.get("command_id"),
            read_as=read_as,
            act_as=act_as,
            ledger_id=ledger_id,
            user_id_or_application_name=user_id_or_application_name,
            token=token,
            timeout=timeout,
        )

    def __init__(
        self,
        workflow_id,
        command_id,
        read_as,
        act_as,
        ledger_id,
        user_id_or_application_name,
        token,
        timeout,
    ) -> None:
        self.workflow_id = workflow_id
        self.command_id = command_id
        self.read_as = read_as
        self.act_as = act_as
        self.ledger_id = ledger_id
        self.user_id_or_application_name = user_id_or_application_name
        self.token = token
        self.timeout = timeout

    @property
    def timeout_seconds(self) -> float:
        """
        Return the effective timeout for this call, in seconds.
        """
        return self.timeout.total_seconds()

    def get_cache(self) -> CachedParameters:
        """
        Return a :class:`CachedParameters` of values that might save us time in a subsequent
        call to the Ledger API.
        """
        return {
            "read_as": self.read_as,
            "act_as": self.act_as,
            "ledger_id": self.ledger_id,
            "user_id_or_application_name": self.user_id_or_application_name,
            "token": self.token,
        }
