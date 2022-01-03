# Copyright (c) 2017-2022 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""
This module has been relocated to ``dazl.client._conn_settings``.
"""

__all__ = ["HTTPConnectionSettings", "SSLSettings", "OAuthSettings", "connection_settings"]

from ..client._conn_settings import (
    HTTPConnectionSettings,
    OAuthSettings,
    SSLSettings,
    connection_settings,
)
