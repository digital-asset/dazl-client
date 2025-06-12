# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from collections.abc import Sequence as Seq
from os import PathLike
import sys
from typing import AsyncContextManager, BinaryIO, Callable, Literal, Optional, Sequence, overload

from ..ledger.aio import Connection
from ..prim import Parties, Party

if sys.version_info >= (3, 11):
    from typing import TypeAlias
else:
    from typing_extensions import TypeAlias

__all__ = ["connect_with_new_party"]

NameGenFn: TypeAlias = Callable[[int], Optional[str]]

@overload
def connect_with_new_party(
    *,
    party_count: Literal[1] = 1,
    url: Optional[str] = None,
    read_as: Optional[Parties] = None,
    act_as: Optional[Parties] = None,
    admin: Optional[bool] = False,
    ledger_id: Optional[str] = None,
    dar: Optional[str | bytes | PathLike | BinaryIO] = None,
    identifier_hint: Optional[str | NameGenFn] = None,
    display_name: Optional[str | NameGenFn] = None,
) -> AsyncContextManager[ConnectionWithParty]: ...
@overload
def connect_with_new_party(
    *,
    party_count: Literal[2],
    url: Optional[str] = None,
    read_as: Optional[Parties] = None,
    act_as: Optional[Parties] = None,
    admin: Optional[bool] = False,
    ledger_id: Optional[str] = None,
    dar: Optional[str | bytes | PathLike | BinaryIO] = None,
    identifier_hint: Optional[str | NameGenFn] = None,
    display_name: Optional[str | NameGenFn] = None,
) -> AsyncContextManager[tuple[ConnectionWithParty, ConnectionWithParty]]: ...
@overload
def connect_with_new_party(
    *,
    party_count: Literal[3],
    url: Optional[str] = None,
    read_as: Optional[Parties] = None,
    act_as: Optional[Parties] = None,
    admin: Optional[bool] = False,
    ledger_id: Optional[str] = None,
    dar: Optional[str | bytes | PathLike | BinaryIO] = None,
    identifier_hint: Optional[str | NameGenFn] = None,
    display_name: Optional[str | NameGenFn] = None,
) -> AsyncContextManager[tuple[ConnectionWithParty, ConnectionWithParty, ConnectionWithParty]]: ...
@overload
def connect_with_new_party(
    *,
    party_count: Literal[4],
    url: Optional[str] = None,
    read_as: Optional[Parties] = None,
    act_as: Optional[Parties] = None,
    admin: Optional[bool] = False,
    ledger_id: Optional[str] = None,
    dar: Optional[str | bytes | PathLike | BinaryIO] = None,
    identifier_hint: Optional[str | NameGenFn] = None,
    display_name: Optional[str | NameGenFn] = None,
) -> AsyncContextManager[
    tuple[ConnectionWithParty, ConnectionWithParty, ConnectionWithParty, ConnectionWithParty]
]: ...
@overload
def connect_with_new_party(
    *,
    party_count: int,
    url: Optional[str] = None,
    read_as: Optional[Parties] = None,
    act_as: Optional[Parties] = None,
    admin: Optional[bool] = False,
    ledger_id: Optional[str] = None,
    dar: Optional[str | bytes | PathLike | BinaryIO] = None,
    identifier_hint: Optional[str | NameGenFn] = None,
    display_name: Optional[str | NameGenFn] = None,
) -> AsyncContextManager[Sequence[ConnectionWithParty]]: ...

class ConnectionWithParty(Seq["ConnectionWithParty"]):
    def __init__(self, connection: Connection, party: Party): ...
    @property
    def connection(self) -> Connection: ...
    @property
    def party(self) -> Party: ...
    def __getitem__(self, item): ...
    def __len__(self) -> Literal[1]: ...
