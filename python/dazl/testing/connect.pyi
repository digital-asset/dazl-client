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
    ContextManager,
    Optional,
    Sequence,
    Tuple,
    Union,
    overload,
)

from ..ledger import aio, blocking as _blocking
from ..prim import Party

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ["connect_with_new_party"]

NameGenFn = Callable[[int], Optional[str]]

# The specific ordering (and nauseating repetition) gives the best possible representation of this
# type for callers of the connect_with_new_party function:
#  * The repetition of each function signature with party_count specified as a Literal parameter
#    ensures that the specific number of returned parties can be checked by a static type checker.
#  * The very first overload specifies that party_count has a default value; no other overloads
#    do. This is how we also communicate to static type checkers what the default value is.
#  * We then supply three overloads; one with blocking omitted, one with blocking=Literal[False]...,
#    and blocking=Literal[True]. These allow for correct distinguishing between asyncio and
#    blocking headers.
@overload
def connect_with_new_party(
    *,
    party_count: Literal[1] = ...,
    url: Optional[str] = ...,
    read_as: Union[None, Party, Collection[Party]] = ...,
    act_as: Union[None, Party, Collection[Party]] = ...,
    admin: Optional[bool] = ...,
    ledger_id: Optional[str] = ...,
    dar: Union[str, bytes, PathLike, BinaryIO] = ...,
    identifier_hint: Union[None, str, NameGenFn] = ...,
    display_name: Union[None, str, NameGenFn] = ...
) -> AsyncContextManager[AsyncConnectionWithParty]: ...
@overload
def connect_with_new_party(
    *,
    party_count: Literal[2],
    url: Optional[str] = ...,
    read_as: Union[None, Party, Collection[Party]] = ...,
    act_as: Union[None, Party, Collection[Party]] = ...,
    admin: Optional[bool] = False,
    ledger_id: Optional[str] = ...,
    dar: Union[str, bytes, PathLike, BinaryIO] = ...,
    identifier_hint: Union[None, str, NameGenFn] = ...,
    display_name: Union[None, str, NameGenFn] = ...
) -> AsyncContextManager[Tuple[AsyncConnectionWithParty, AsyncConnectionWithParty]]: ...
@overload
def connect_with_new_party(
    *,
    party_count: Literal[3],
    url: Optional[str] = ...,
    read_as: Union[None, Party, Collection[Party]] = ...,
    act_as: Union[None, Party, Collection[Party]] = ...,
    admin: Optional[bool] = False,
    ledger_id: Optional[str] = ...,
    dar: Union[str, bytes, PathLike, BinaryIO] = ...,
    identifier_hint: Union[None, str, NameGenFn] = ...,
    display_name: Union[None, str, NameGenFn] = ...
) -> AsyncContextManager[
    Tuple[AsyncConnectionWithParty, AsyncConnectionWithParty, AsyncConnectionWithParty]
]: ...
@overload
def connect_with_new_party(
    *,
    party_count: Literal[4],
    url: Optional[str] = ...,
    read_as: Union[None, Party, Collection[Party]] = ...,
    act_as: Union[None, Party, Collection[Party]] = ...,
    admin: Optional[bool] = False,
    ledger_id: Optional[str] = ...,
    dar: Union[str, bytes, PathLike, BinaryIO] = ...,
    identifier_hint: Union[None, str, NameGenFn] = ...,
    display_name: Union[None, str, NameGenFn] = ...
) -> AsyncContextManager[
    Tuple[
        AsyncConnectionWithParty,
        AsyncConnectionWithParty,
        AsyncConnectionWithParty,
        AsyncConnectionWithParty,
    ]
]: ...
@overload
def connect_with_new_party(
    *,
    party_count: int,
    url: Optional[str] = ...,
    read_as: Union[None, Party, Collection[Party]] = ...,
    act_as: Union[None, Party, Collection[Party]] = ...,
    admin: Optional[bool] = False,
    ledger_id: Optional[str] = ...,
    dar: Union[str, bytes, PathLike, BinaryIO] = ...,
    identifier_hint: Union[None, str, NameGenFn] = ...,
    display_name: Union[None, str, NameGenFn] = ...
) -> AsyncContextManager[Sequence[AsyncConnectionWithParty]]: ...
@overload
def connect_with_new_party(
    *,
    blocking: Literal[False],
    party_count: Literal[1] = ...,
    url: Optional[str] = ...,
    read_as: Union[None, Party, Collection[Party]] = ...,
    act_as: Union[None, Party, Collection[Party]] = ...,
    admin: Optional[bool] = False,
    ledger_id: Optional[str] = ...,
    dar: Union[str, bytes, PathLike, BinaryIO] = ...,
    identifier_hint: Union[None, str, NameGenFn] = ...,
    display_name: Union[None, str, NameGenFn] = ...
) -> AsyncContextManager[AsyncConnectionWithParty]: ...
@overload
def connect_with_new_party(
    *,
    blocking: Literal[False],
    party_count: Literal[2],
    url: Optional[str] = ...,
    read_as: Union[None, Party, Collection[Party]] = ...,
    act_as: Union[None, Party, Collection[Party]] = ...,
    admin: Optional[bool] = False,
    ledger_id: Optional[str] = ...,
    dar: Union[str, bytes, PathLike, BinaryIO] = ...,
    identifier_hint: Union[None, str, NameGenFn] = ...,
    display_name: Union[None, str, NameGenFn] = ...
) -> AsyncContextManager[Tuple[AsyncConnectionWithParty, AsyncConnectionWithParty]]: ...
@overload
def connect_with_new_party(
    *,
    blocking: Literal[False],
    party_count: Literal[3],
    url: Optional[str] = ...,
    read_as: Union[None, Party, Collection[Party]] = ...,
    act_as: Union[None, Party, Collection[Party]] = ...,
    admin: Optional[bool] = False,
    ledger_id: Optional[str] = ...,
    dar: Union[str, bytes, PathLike, BinaryIO] = ...,
    identifier_hint: Union[None, str, NameGenFn] = ...,
    display_name: Union[None, str, NameGenFn] = ...
) -> AsyncContextManager[
    Tuple[AsyncConnectionWithParty, AsyncConnectionWithParty, AsyncConnectionWithParty]
]: ...
@overload
def connect_with_new_party(
    *,
    blocking: Literal[False],
    party_count: Literal[4],
    url: Optional[str] = ...,
    read_as: Union[None, Party, Collection[Party]] = ...,
    act_as: Union[None, Party, Collection[Party]] = ...,
    admin: Optional[bool] = False,
    ledger_id: Optional[str] = ...,
    dar: Union[str, bytes, PathLike, BinaryIO] = ...,
    identifier_hint: Union[None, str, NameGenFn] = ...,
    display_name: Union[None, str, NameGenFn] = ...
) -> AsyncContextManager[
    Tuple[
        AsyncConnectionWithParty,
        AsyncConnectionWithParty,
        AsyncConnectionWithParty,
        AsyncConnectionWithParty,
    ]
]: ...
@overload
def connect_with_new_party(
    *,
    blocking: Literal[False],
    party_count: int,
    url: Optional[str] = ...,
    read_as: Union[None, Party, Collection[Party]] = ...,
    act_as: Union[None, Party, Collection[Party]] = ...,
    admin: Optional[bool] = False,
    ledger_id: Optional[str] = ...,
    dar: Union[str, bytes, PathLike, BinaryIO] = ...,
    identifier_hint: Union[None, str, NameGenFn] = ...,
    display_name: Union[None, str, NameGenFn] = ...
) -> AsyncContextManager[Sequence[AsyncConnectionWithParty]]: ...
@overload
def connect_with_new_party(
    *,
    blocking: Literal[True],
    party_count: Literal[1] = ...,
    url: Optional[str] = ...,
    read_as: Union[None, Party, Collection[Party]] = ...,
    act_as: Union[None, Party, Collection[Party]] = ...,
    admin: Optional[bool] = False,
    ledger_id: Optional[str] = ...,
    dar: Union[str, bytes, PathLike, BinaryIO] = ...,
    identifier_hint: Union[None, str, NameGenFn] = ...,
    display_name: Union[None, str, NameGenFn] = ...
) -> ContextManager[BlockingConnectionWithParty]: ...
@overload
def connect_with_new_party(
    *,
    blocking: Literal[True],
    party_count: Literal[2],
    url: Optional[str] = ...,
    read_as: Union[None, Party, Collection[Party]] = ...,
    act_as: Union[None, Party, Collection[Party]] = ...,
    admin: Optional[bool] = False,
    ledger_id: Optional[str] = ...,
    dar: Union[str, bytes, PathLike, BinaryIO] = ...,
    identifier_hint: Union[None, str, NameGenFn] = ...,
    display_name: Union[None, str, NameGenFn] = ...
) -> ContextManager[Tuple[BlockingConnectionWithParty, BlockingConnectionWithParty]]: ...
@overload
def connect_with_new_party(
    *,
    blocking: Literal[True],
    party_count: Literal[3],
    url: Optional[str] = ...,
    read_as: Union[None, Party, Collection[Party]] = ...,
    act_as: Union[None, Party, Collection[Party]] = ...,
    admin: Optional[bool] = False,
    ledger_id: Optional[str] = ...,
    dar: Union[str, bytes, PathLike, BinaryIO] = ...,
    identifier_hint: Union[None, str, NameGenFn] = ...,
    display_name: Union[None, str, NameGenFn] = ...
) -> ContextManager[
    Tuple[BlockingConnectionWithParty, BlockingConnectionWithParty, BlockingConnectionWithParty]
]: ...
@overload
def connect_with_new_party(
    *,
    blocking: Literal[True],
    party_count: Literal[4],
    url: Optional[str] = ...,
    read_as: Union[None, Party, Collection[Party]] = ...,
    act_as: Union[None, Party, Collection[Party]] = ...,
    admin: Optional[bool] = False,
    ledger_id: Optional[str] = ...,
    dar: Union[str, bytes, PathLike, BinaryIO] = ...,
    identifier_hint: Union[None, str, NameGenFn] = ...,
    display_name: Union[None, str, NameGenFn] = ...
) -> ContextManager[
    Tuple[
        BlockingConnectionWithParty,
        BlockingConnectionWithParty,
        BlockingConnectionWithParty,
        BlockingConnectionWithParty,
    ]
]: ...
@overload
def connect_with_new_party(
    *,
    blocking: Literal[True],
    party_count: int,
    url: Optional[str] = ...,
    read_as: Union[None, Party, Collection[Party]] = ...,
    act_as: Union[None, Party, Collection[Party]] = ...,
    admin: Optional[bool] = False,
    ledger_id: Optional[str] = ...,
    dar: Union[str, bytes, PathLike, BinaryIO] = ...,
    identifier_hint: Union[None, str, NameGenFn] = ...,
    display_name: Union[None, str, NameGenFn] = ...
) -> ContextManager[Sequence[BlockingConnectionWithParty]]: ...

class AsyncConnectionWithParty(Sequence["AsyncConnectionWithParty"]):
    @property
    def connection(self) -> aio.Connection: ...
    @property
    def party(self) -> Party: ...
    async def __aenter__(self) -> Sequence[AsyncConnectionWithParty]: ...
    async def __aexit__(self, exc_type, exc_val, exc_tb) -> None: ...
    def __getitem__(self, item): ...
    def __len__(self) -> Literal[1]: ...

class BlockingConnectionWithParty(Sequence["BlockingConnectionWithParty"]):
    @property
    def connection(self) -> _blocking.Connection: ...
    @property
    def party(self) -> Party: ...
    def __enter__(self) -> Sequence[BlockingConnectionWithParty]: ...
    def __exit__(self, exc_type, exc_val, exc_tb) -> None: ...
    def __getitem__(self, item): ...
    def __len__(self) -> Literal[1]: ...
