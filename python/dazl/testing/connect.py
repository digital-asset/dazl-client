# Copyright (c) 2017-2021 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from asyncio import gather
from contextlib import ExitStack
from os import PathLike
import sys
from typing import BinaryIO, Callable, Collection, Optional, TypeVar, Union

from .. import connect
from ..prim import Party

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

if sys.version_info >= (3, 7):
    from contextlib import AsyncExitStack
else:
    from async_exit_stack import AsyncExitStack

__all__ = ["connect_with_new_party"]

Conn = TypeVar("Conn", bound="Connection")
Self = TypeVar("Self", bound="ConnectionWithParty")


NameGenFn = Callable[[int], Optional[str]]


def connect_with_new_party(
    *,
    party_count=1,
    url=None,
    read_as=None,
    act_as=None,
    admin=False,
    ledger_id=None,
    dar=None,
    identifier_hint=None,
    display_name=None,
    blocking=False,
):
    """
    A helper function for connecting to a ledger as a brand new party. This isn't normally useful
    outside of tests, where having creating new parties for each test helps keep test data isolated.

    Like the :func:`dazl.ledger.connect` function, all parameters are optional, and if unspecified,
    get their default values from the environment.

    This function can NOT be used with ledgers that require authentication since it has no way to
    ask a token granter for an appropriate token for the newly allocated party.

    :param url:
        The URL of the ledger to connect to. This ledger MUST NOT require authentication!
    :type url: str
    :param read_as:
        Extra parties to for which read-as access should be granted.
    :type read_as: str or Collection[str]
    :param act_as:
        Extra parties to for which act-as access should be granted. The created party is added to
        this list.
    :type read_as: str or Collection[str]
    :param admin:
        ``True`` if the created connection should have "admin" rights; otherwise ``False``. Note
        that in order to allocate parties, an initial connection with admin rights is ALWAYS
        created, and the value of this call only affects the returned connection.
    :type admin: bool
    :param ledger_id:
        The ledger ID to connect to. As with the ``connect`` api, if the target is the gRPC Ledger
        API, then supplying this field is optional, and with an HTTP JSON API server, this field
        must be supplied.
    :type ledger_id: str
    :param dar:
        A path to a file, the contents of the file (as ``bytes``), or a byte buffer that point to a
        DAR that should also be uploaded.
    :type dar: str or bytes or PathLike or BinaryIO
    :param party_count:
        The number of parties (and connections) to create. The default value is 1.
    :type party_count: int
    :param blocking:
        Whether to return a blocking connection or an asyncio connection. The default is ``False``
        (an asyncio connection).
    :param identifier_hint:
        A hint to the backing participant. Note that the Daml ledger is free to ignore this
        hint entirely. If `party_count` is greater than 1, then
    :type identifier_hint: str
    :param display_name:
        A human-readable name that corresponds to the allocated ``Party``.
    :return:
        An asynchronous context manager that returns one or more :class:`ConnectionWithParty`
        objects.
    """
    if party_count < 0:
        raise ValueError("party_count must be a positive number")

    contents = None  # type: Optional[bytes]
    if dar is not None:
        if isinstance(dar, bytes):
            contents = dar
        elif isinstance(dar, (str, PathLike)):
            with open(dar, "rb") as buf:
                contents = buf.read()
        else:
            contents = dar.read()

    if blocking:
        return BlockingConnectWithNewParty(
            party_count=party_count,
            url=url,
            read_as=read_as,
            act_as=as_party_collection(act_as),
            admin=admin,
            ledger_id=ledger_id,
            dar=contents,
            identifier_hint_fn=convert_to_fn(identifier_hint, party_count=party_count),
            display_name_fn=convert_to_fn(display_name, party_count=party_count),
        )
    else:
        return AsyncConnectWithNewParty(
            party_count=party_count,
            url=url,
            read_as=read_as,
            act_as=as_party_collection(act_as),
            admin=admin,
            ledger_id=ledger_id,
            dar=contents,
            identifier_hint_fn=convert_to_fn(identifier_hint, party_count=party_count),
            display_name_fn=convert_to_fn(display_name, party_count=party_count),
        )


def as_party_collection(p: "Union[None, Party, Collection[Party]]") -> "Collection[Party]":
    if not p:
        return []
    elif isinstance(p, str):
        return [Party(o) for o in p.split(",")]
    else:
        return p


def convert_to_fn(party_or_fn: Union[None, str, NameGenFn], *, party_count: int = 1) -> NameGenFn:
    if party_or_fn is None:
        return lambda _: None
    if isinstance(party_or_fn, str):
        if party_count == 1:
            return lambda _: party_or_fn
        else:
            return lambda i: f"{party_or_fn}{i:03}"
    else:
        return party_or_fn


class ConnectionWithParty:
    # We're cheating here; we declare the types of our fields as properties in the typing file,
    # but really they're just plain attributes
    # noinspection PyPropertyAccess
    def __init__(self, connection, party):
        self.connection = connection
        self.party = party

    def __getitem__(self, item: "Literal[0]") -> "ConnectionWithParty":
        return self

    def __len__(self) -> "Literal[1]":
        return 1


class ConnectWithNewPartyBase:
    def __init__(
        self,
        *,
        url: Optional[str],
        read_as: Union[Party, Collection[Party]],
        act_as: Collection[Party],
        admin: Optional[bool],
        ledger_id: str,
        dar: Optional[bytes],
        party_count: int,
        identifier_hint_fn: NameGenFn,
        display_name_fn: NameGenFn,
    ):
        self.url = url
        self.read_as = read_as
        self.act_as = act_as
        self.admin = admin
        self.ledger_id = ledger_id
        self.dar = dar
        self.party_count = party_count
        self.identifier_hint_fn = identifier_hint_fn
        self.display_name_fn = display_name_fn


class AsyncConnectWithNewParty(ConnectWithNewPartyBase):
    def __init__(self, **kwargs):
        super(AsyncConnectWithNewParty, self).__init__(**kwargs)
        self._cm = AsyncExitStack()

    async def __aenter__(self):
        party_infos = await self._set_up_ledger()
        ret = []
        for party_info in party_infos:
            party_conn = await self._cm.enter_async_context(
                connect(
                    url=self.url,
                    read_as=self.read_as,
                    act_as=[party_info.party, *self.act_as],
                    admin=self.admin,
                    ledger_id=self.ledger_id,
                )
            )
            ret.append(ConnectionWithParty(party_conn, party_info.party))
        if len(ret) == 1:
            return ret[0]
        else:
            return tuple(ret)

    async def __aexit__(self, exc_type, exc_val, exc_tb) -> None:
        await self._cm.aclose()

    async def _set_up_ledger(self):
        # Party allocation and package uploading require "admin" access, so we disregard the given
        # user parameters to upload packages and allocate parties
        async with connect(url=self.url, admin=True, ledger_id=self.ledger_id) as admin_conn:
            if self.dar is not None:
                await admin_conn.upload_package(self.dar)

            return await gather(
                *(
                    admin_conn.allocate_party(
                        identifier_hint=self.identifier_hint_fn(i),
                        display_name=self.display_name_fn(i),
                    )
                    for i in range(self.party_count)
                )
            )


class BlockingConnectWithNewParty(ConnectWithNewPartyBase):
    def __init__(self, **kwargs):
        super(BlockingConnectWithNewParty, self).__init__(**kwargs)
        self._cm = ExitStack()

    def __enter__(self):
        party_infos = self._set_up_ledger()
        ret = []
        for party_info in party_infos:
            party_conn = self._cm.enter_context(
                connect(
                    url=self.url,
                    read_as=self.read_as,
                    act_as=[party_info.party, *self.act_as],
                    admin=self.admin,
                    ledger_id=self.ledger_id,
                    blocking=True,
                )
            )
            ret.append(ConnectionWithParty(party_conn, party_info.party))
        if len(ret) == 1:
            return ret[0]
        else:
            return tuple(ret)

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        self._cm.close()

    def _set_up_ledger(self):
        # Party allocation and package uploading require "admin" access, so we disregard the given
        # user parameters to upload packages and allocate parties
        with connect(
            url=self.url, admin=True, ledger_id=self.ledger_id, blocking=True
        ) as admin_conn:
            if self.dar is not None:
                admin_conn.upload_package(self.dar)

            return [
                admin_conn.allocate_party(
                    identifier_hint=self.identifier_hint_fn(i),
                    display_name=self.display_name_fn(i),
                )
                for i in range(self.party_count)
            ]
