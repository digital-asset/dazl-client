# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

import base64
import json
from typing import Any, Mapping, Optional

from dazl.ledger.auth import V1TokenNamespace
from dazl.prim import Parties

__all__ = ["encode_unsigned_token"]


def encode_unsigned_token(
    *,
    user_id: Optional[str] = None,
    read_as: Optional[Parties] = None,
    act_as: Optional[Parties] = None,
    ledger_id: Optional[str] = None,
    application_id: Optional[str] = None,
    admin: Optional[bool] = None,
) -> bytes:
    """
    Generate a JSON Web Token (JWT) that has no signature.

    Because this JWT has no signature, it is really only useful in a testing context. Do not use
    to generate tokens against a real ledger!

    :param user_id:
    :param read_as:
        If specified, generates a Daml V1 token with the specified read-as values.
    :param act_as:
        If specified, generates a Daml V1 token with the specified act-as values.
    :param ledger_id:
        If specified, generates a Daml V1 token with the specified ledger ID value.
    :param application_id:
    :param admin:
    :return:
    """
    header = {
        "alg": "none",
        "typ": "JWT",
    }
    payload = {V1TokenNamespace: {}}  # type: Mapping[str, Any]
    if ledger_id is not None:
        payload[V1TokenNamespace]["ledgerId"] = ledger_id
    if application_id is not None:
        payload[V1TokenNamespace]["applicationId"] = application_id
    if act_as is not None:
        payload[V1TokenNamespace]["actAs"] = sorted(act_as)
    if read_as is not None:
        payload[V1TokenNamespace]["readAs"] = sorted(read_as)
    if admin:
        payload[V1TokenNamespace]["admin"] = admin

    return (
        base64.urlsafe_b64encode(json.dumps(header).encode("utf-8")).rstrip(b"=")
        + b"."
        + base64.urlsafe_b64encode(json.dumps(payload).encode("utf-8")).rstrip(b"=")
        + b"."
    )
