# Copyright (c) 2019 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0


from aiohttp import ClientSession
from aiohttp.web import get, post, Request, Response
from asyncio import get_event_loop
from oauthlib.oauth2 import WebApplicationClient
from typing import Dict
import uuid

from ..model.network import OAuthSettings


class OAuthHandler:

    AUTH_ROUTE = '/auth/callback'

    def __init__(self, url_prefix: str):
        self.url_prefix = url_prefix
        self.callbacks = {}  # type: Dict[str, OAuthAuthorizationCodeGrantRequest]
        self.routes = [
            get(self.AUTH_ROUTE, self.oauth_callback)
        ]

    async def auth_flow(self, settings: OAuthSettings) -> OAuthSettings:
        """
        Perform an authorization flow with the remote server and prepare the server for handling
        a response.

        :return:
            :class:`OAuthSettings` populated with an initial token and possibly information for
            refreshing that token.
        """
        oauth_req = OAuthAuthorizationCodeGrantRequest(self.url_prefix + self.AUTH_ROUTE, settings)
        self.callbacks[oauth_req.state] = oauth_req
        await oauth_req.start()

        # wait until the callback has been called
        return await oauth_req.future

    async def oauth_callback(self, request: Request) -> Response:
        code = request.query.get('code')
        state = request.query.get('state')
        oauth_req = self.callbacks.pop(state)
        if oauth_req is not None:
            try:
                await oauth_req.handle_redirect(str(request.url), code, state)
                return await self._auth_finished(request)
            finally:
                await oauth_req.close()
        else:
            return await self._invalid_state(request)

    async def _auth_finished(self, request: Request) -> Response:
        pass

    async def _invalid_state(self, request: Request) -> Response:
        pass


class OAuthAuthorizationCodeGrantRequest:
    def __init__(self, redirect_uri: str, settings: OAuthSettings):
        self.settings = settings
        self.future = get_event_loop().create_future()
        self.state = uuid.uuid4().hex
        self.client = WebApplicationClient(settings.client_id)
        self.redirect_uri = redirect_uri
        self.session = ClientSession()

    async def start(self) -> None:
        uri = self.client.prepare_request_uri(
            self.settings.token_uri, redirect_uri=self.redirect_uri, state=self.state)
        body = self.client.prepare_request_body()

        async with self.session.post(uri, data=body) as response:
            print(response.status)
            print(await response.text())

    async def handle_redirect(self, uri: str, code: str, state: str) -> OAuthSettings:
        self.client.parse_request_uri_response(uri, state)

        kwargs = {}
        if self.settings.client_secret:
            kwargs['client_secret'] = self.settings.client_secret

        uri = self.settings.token_uri
        body = self.client.prepare_request_body(
            code=code, redirect_uri=self.redirect_uri, **kwargs)

        # fetch token

        self.client.parse_request_body_response(response_body)

        new_settings = OAuthSettings(

        )

        self.future.set_result(new_settings)
        return new_settings

    async def close(self):
        await self.session.close()
