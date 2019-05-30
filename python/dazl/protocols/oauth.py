# Copyright (c) 2019 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from ..model.network import OAuthSettings


async def oauth_flow(settings: OAuthSettings) -> OAuthSettings:
    """
    Implementation of an OAuth flow that ensures that a token is provided.

    :param settings:
    :return:
    """
    if not settings.token:
        raise ValueError('the token must be directly supplied at this time')
        # if settings.redirect_uri:
        #     client = WebApplicationClient(settings.client_id)
        #     client.prepare_request_uri()
        #     client.prepare_request_body()
        #     client.parse_request_uri_response()
        #     settings.
    return settings
