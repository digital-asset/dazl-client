# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

import sys
from typing import Callable, Collection, Optional, TypedDict, TypeVar

from grpc import aio

from .. import ActAs, CommandMeta, ReadAs
from ... import Party
from ..._gen.com.daml.ledger.api import v1 as lapipb
from ..._gen.com.daml.ledger.api.v1 import admin as lapiadminpb
from .._call import CallContext as CallContextBase
from ..auth import parse_token
from .codec_aio import Codec

if sys.version_info >= (3, 11):
    from typing import assert_never
else:
    from typing_extensions import assert_never

__all__ = ["CallContext"]

T = TypeVar("T")


class GrpcKwargs(TypedDict, total=False):
    """
    Keyword arguments that should accompany a
    """

    timeout: float
    metadata: aio.Metadata


class CallContext(CallContextBase):
    """
    Contextual information as it relates to a single logical Ledger API call.
    """

    channel: Optional[aio.Channel]

    async def get_read_as(self) -> Collection[Party]:
        """
        Return all the parties that the current call is reading as.
        """
        meta = await self.command_meta()
        p = set[Party]()
        if meta.read_as is not None:
            p.update(meta.read_as)
        if meta.act_as is not None:
            p.update(meta.act_as)
        return sorted(p)

    async def get_ledger_id(self) -> str:
        if self.ledger_id is None:
            stub = self.grpc_stub(lapipb.LedgerIdentityServiceStub)
            response = await stub.GetLedgerIdentity(
                lapipb.GetLedgerIdentityRequest(), **self.grpc_kwargs
            )
            self.ledger_id = response.ledger_id

        return self.ledger_id

    async def command_meta(self) -> CommandMeta:
        """
        Return an overall :class:`CommandMeta` for the effective values of this call.
        """
        if self.read_as is None and self.act_as is None:
            if self.token:
                parsed_token = parse_token(self.token)
                if parsed_token.token_version == 1:
                    self.read_as = parsed_token.read_as
                    self.act_as = parsed_token.act_as
                    if parsed_token.ledger_id is not None:
                        self.ledger_id = parsed_token.ledger_id
                    if self.user_id_or_application_name is not None:
                        self.user_id_or_application_name = parsed_token.application_name

                elif parsed_token.token_version == 2:
                    if self.user_id_or_application_name is None:
                        self.user_id_or_application_name = parsed_token.user_id
                    elif self.user_id_or_application_name != parsed_token.user_id:
                        raise ValueError("")

                    stub = self.grpc_stub(lapiadminpb.UserManagementServiceStub)
                    request = lapiadminpb.ListUserRightsRequest(
                        user_id=self.user_id_or_application_name
                    )
                    response = await stub.ListUserRights(request, **self.grpc_kwargs)

                    read_as = set()
                    act_as = set()
                    for pb in response.rights:
                        right = Codec.decode_right(pb)
                        if isinstance(right, ActAs):
                            act_as.add(right.party)
                        elif isinstance(right, ReadAs):
                            read_as.add(right.party)
                    self.read_as = sorted(read_as)
                    self.act_as = sorted(act_as)
                else:
                    assert_never(parsed_token.token_version)

            elif self.user_id_or_application_name:
                # no token; this could be because the ledger is unauthed, or
                # perhaps there is an authenticating proxy between us and the ledger
                stub = self.grpc_stub(lapiadminpb.UserManagementServiceStub)
                request = lapiadminpb.ListUserRightsRequest(
                    user_id=self.user_id_or_application_name
                )
                response = await stub.ListUserRights(request, **self.grpc_kwargs)

                read_as = set()
                act_as = set()
                for pb in response.rights:
                    right = Codec.decode_right(pb)
                    if isinstance(right, ActAs):
                        act_as.add(right.party)
                    elif isinstance(right, ReadAs):
                        read_as.add(right.party)
                self.read_as = sorted(read_as)
                self.act_as = sorted(act_as)

            else:
                # if absolutely no identifying information at all has been supplied, there
                # simply isn't anything more that can be done
                raise ValueError(
                    "either read_as/act_as, application_name, user_id, or a token must be specified"
                )

        if self.user_id_or_application_name is None:
            # TODO: avoid double-parsing the token if we can
            if self.token is not None:
                parsed_token = parse_token(self.token)
                if parsed_token.token_version == 2:
                    self.user_id_or_application_name = parsed_token.user_id

        if self.user_id_or_application_name is None:
            # if, after all of that, we still can't default the user id, use dazl's
            # old default value
            self.user_id_or_application_name = "DAZL-Client"

        return CommandMeta(
            workflow_id=self.workflow_id,
            command_id=self.command_id,
            read_as=self.read_as,
            act_as=self.act_as,
            user_id=self.user_id_or_application_name,
        )

    def grpc_stub(self, grpc_service: Callable[[aio.Channel], T], /) -> T:
        """
        Create an async stub for the specified type.
        """
        # this really only exists because IntelliJ doesn't handle these typing rules without a
        # little bit of help; mypy correctly validates these types.
        channel = getattr(self, "channel", None)
        if channel is None:
            # an unset channel is really a coding error
            raise Exception("a channel must be set on a CallContext before use")

        return grpc_service(channel)

    @property
    def grpc_kwargs(self) -> GrpcKwargs:
        """
        Generate keyword arguments that should accompany a gRPC Ledger API call.
        """
        kwargs = GrpcKwargs()
        kwargs["timeout"] = self.timeout_seconds
        if self.token:
            kwargs["metadata"] = aio.Metadata(("authorization", f"Bearer {self.token}"))
        return kwargs


class Cache:
    pass
