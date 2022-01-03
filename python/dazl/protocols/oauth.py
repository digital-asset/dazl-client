# Copyright (c) 2017-2022 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import logging
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..client._conn_settings import OAuthSettings


__all__ = ["oauth_flow"]


async def oauth_flow(settings: "OAuthSettings") -> "OAuthSettings":
    """
    Implementation of an OAuth flow that ensures that a token is provided.

    :param settings:
    :return:
    """
    import requests

    from ..client._conn_settings import OAuthSettings

    if not settings.token:

        if settings.auth_audience == None:
            logging.error("ERROR: Need to supply an oAuth audience")
            raise ValueError("ERROR: Need to supply an oAuth audience")

        headers = {"Accept": "application/json"}
        data = {
            "client_id": settings.client_id,
            "client_secret": settings.client_secret,
            "audience": settings.auth_audience,
            "grant_type": "client_credentials",
        }

        if settings.token_uri is None:
            raise ValueError("missing a token URI")
        response = None
        try:
            response = requests.post(
                settings.token_uri,
                headers=headers,
                data=data,
                auth=None,
                verify=settings.auth_ca_file,
            )
        except Exception as ex:
            logging.info(ex)
            raise ValueError("Unable to get token at this time")

        if response.status_code != 200:
            logging.error("ERROR: Unable to retrieve token. Exiting")
            raise ValueError("Unable to get token from oAuth source")

        json = response.json()
        return_settings = OAuthSettings(
            client_id=settings.client_id,
            client_secret=settings.client_secret,
            token=json["access_token"],
            token_uri=settings.token_uri,
            refresh_token=settings.refresh_token,
            id_token=settings.id_token,
            auth_url=settings.auth_url,
            redirect_uri=settings.redirect_uri,
            auth_audience=settings.auth_audience,
            auth_ca_file=settings.auth_ca_file,
        )

        return return_settings

    else:
        return settings
