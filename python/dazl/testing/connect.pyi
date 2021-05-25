# Copyright (c) 2017-2021 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from collections.abc import Sequence as Seq
from os import PathLike
import sys
from typing import (
    AsyncContextManager,
    BinaryIO,
    Callable,
    Collection,
    Optional,
    Sequence,
    Tuple,
    Union,
    overload,
)

from ..ledger.aio import Connection
from ..prim import Party

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
__all__ = ["connect_with_new_party"]
NameGenFn = Callable[[int], Optional[str]]
@overload
def connect_with_new_party(
    *,
    party_count: Literal[1] = 1,
    url: Optional[str] = None,
    read_as: Union[None, Party, Collection[Party]] = None,
    act_as: Union[None, Party, Collection[Party]] = None,
    admin: Optional[bool] = False,
    ledger_id: Optional[str] = None,
    dar: Union[str, bytes, PathLike, BinaryIO] = None,
    identifier_hint: Union[None, str, NameGenFn] = None,
    display_name: Union[None, str, NameGenFn] = None
) -> AsyncContextManager[ConnectionWithParty]: ...
@overload
def connect_with_new_party(
    *,
    party_count: Literal[2],
    url: Optional[str] = None,
    read_as: Union[None, Party, Collection[Party]] = None,
    act_as: Union[None, Party, Collection[Party]] = None,
    admin: Optional[bool] = False,
    ledger_id: Optional[str] = None,
    dar: Union[str, bytes, PathLike, BinaryIO] = None,
    identifier_hint: Union[None, str, NameGenFn] = None,
    display_name: Union[None, str, NameGenFn] = None
) -> AsyncContextManager[Tuple[ConnectionWithParty, ConnectionWithParty]]: ...
@overload
def connect_with_new_party(
    *,
    party_count: Literal[3],
    url: Optional[str] = None,
    read_as: Union[None, Party, Collection[Party]] = None,
    act_as: Union[None, Party, Collection[Party]] = None,
    admin: Optional[bool] = False,
    ledger_id: Optional[str] = None,
    dar: Union[str, bytes, PathLike, BinaryIO] = None,
    identifier_hint: Union[None, str, NameGenFn] = None,
    display_name: Union[None, str, NameGenFn] = None
) -> AsyncContextManager[Tuple[ConnectionWithParty, ConnectionWithParty, ConnectionWithParty]]: ...
@overload
def connect_with_new_party(
    *,
    party_count: Literal[4],
    url: Optional[str] = None,
    read_as: Union[None, Party, Collection[Party]] = None,
    act_as: Union[None, Party, Collection[Party]] = None,
    admin: Optional[bool] = False,
    ledger_id: Optional[str] = None,
    dar: Union[str, bytes, PathLike, BinaryIO] = None,
    identifier_hint: Union[None, str, NameGenFn] = None,
    display_name: Union[None, str, NameGenFn] = None
) -> AsyncContextManager[
    Tuple[ConnectionWithParty, ConnectionWithParty, ConnectionWithParty, ConnectionWithParty]
]: ...
@overload
def connect_with_new_party(
    *,
    party_count: int,
    url: Optional[str] = None,
    read_as: Union[None, Party, Collection[Party]] = None,
    act_as: Union[None, Party, Collection[Party]] = None,
    admin: Optional[bool] = False,
    ledger_id: Optional[str] = None,
    dar: Union[str, bytes, PathLike, BinaryIO] = None,
    identifier_hint: Union[None, str, NameGenFn] = None,
    display_name: Union[None, str, NameGenFn] = None
) -> AsyncContextManager[Sequence[ConnectionWithParty]]: ...

class ConnectionWithParty(Seq["ConnectionWithParty"]):
    def __init__(self, connection: Connection, party: Party): ...
    @property
    def connection(self) -> Connection: ...
    @property
    def party(self) -> Party: ...
    def __getitem__(self, item): ...
    def __len__(self) -> Literal[1]: ...
