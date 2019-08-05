# Copyright (c) 2019 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""
Endpoints for managing parties/bots connected via a dazl client.
"""

from dataclasses import asdict, dataclass
from typing import Collection, Sequence, TYPE_CHECKING

from ..client import Bot, _NetworkImpl
from ..model.core import DazlImportError, Party, SourceLocation

if TYPE_CHECKING:
    from aiohttp import web


@dataclass(frozen=True)
class BotInfoList:
    bots: 'Collection[BotInfo]'


@dataclass(frozen=True)
class BotInfo:
    id: str
    name: str
    party: Party
    state: str
    entries: 'Sequence[BotInfoEntry]'


@dataclass(frozen=True)
class BotInfoEntry:
    event_key: str
    source_location: 'SourceLocation'


def build_routes(network_impl: '_NetworkImpl') -> 'Collection[web.RouteDef]':
    try:
        from aiohttp import web
    except ImportError:
        raise DazlImportError('aiohttp', 'server routes could not be built because aiohttp is not installed')

    routes = web.RouteTableDef()

    @routes.get('/parties')
    async def get_parties(_: 'web.Request') -> 'web.Response':
        json_dict = dict(parties=[{"id": party} for party in network_impl.parties()])
        return web.json_response(json_dict)

    @routes.get('/bots')
    async def get_bots(_: 'web.Request') -> 'web.Response':
        bot_infos = [_get_bot_info(bot)
                     for party_impl in network_impl.party_impls()
                     for bot in party_impl.bots]
        return web.json_response(asdict(BotInfoList(bots=bot_infos)))

    @routes.get('/bots/{bot_id}')
    async def get_bot_by_id(request: 'web.Request') -> 'web.Response':
        bot = get_bot(request)
        return web.json_response(asdict(_get_bot_info(bot)))

    @routes.post('/bots/{bot_id}/state/{action}')
    async def change_bot_state(request: 'web.Request') -> 'web.Response':
        bot = get_bot(request)
        action = request.match_info['action']

        if action.lower() == 'pause':
            bot.pause()
            return web.HTTPAccepted()
        elif action.lower() == 'resume':
            bot.resume()
            return web.HTTPAccepted()
        else:
            raise web.HTTPBadRequest()

    def get_bot(request: 'web.Request') -> 'Bot':
        """
        Return the bot referenced by the request. Throw HTTPNotFound if a bot with the ID specified
        in the URL does not exist.
        """
        bot_id = request.match_info['bot_id']
        bot = network_impl.find_bot(bot_id)
        if bot is None:
            raise web.HTTPNotFound()
        return bot

    return routes


def _get_bot_info(bot: 'Bot') -> 'BotInfo':
    entries = [BotInfoEntry(event_key=entry.event_key, source_location=entry.source_location)
               for entry in bot.entries()]

    return BotInfo(
        id=bot.id, party=bot.party, name=bot.name, state=bot.state.value, entries=entries)
