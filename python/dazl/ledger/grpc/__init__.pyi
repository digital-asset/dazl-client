# Copyright (c) 2017-2024 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from os import PathLike
from typing import Optional

from ...damlast.lookup import MultiPackageLookup
from ...prim import Parties, TimeDeltaLike
from .conn_aio import Connection

__all__ = ["connect", "Connection"]

# TODO: Figure out clever ways to make this function's type signature easier to maintain while
#  preserving its ease of use to callers.
def connect(
    url: str,
    *,
    read_as: Optional[Parties] = None,
    act_as: Optional[Parties] = None,
    admin: Optional[bool] = False,
    ledger_id: Optional[str] = None,
    application_name: Optional[str] = None,
    oauth_token: Optional[str] = None,
    ca: Optional[bytes] = None,
    ca_file: Optional[PathLike] = None,
    cert: Optional[bytes] = None,
    cert_file: Optional[PathLike] = None,
    cert_key: Optional[bytes] = None,
    cert_key_file: Optional[PathLike] = None,
    connect_timeout: Optional[TimeDeltaLike] = None,
    enable_http_proxy: bool = True,
    lookup: Optional[MultiPackageLookup] = None,
) -> Connection: ...
