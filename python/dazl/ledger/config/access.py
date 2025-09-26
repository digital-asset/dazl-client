# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

import base64
from dataclasses import dataclass
import json
import os
from pathlib import Path
import sys
from typing import TYPE_CHECKING, AbstractSet, Any, Collection, Mapping, Optional, TypedDict

from ...prim import Parties, Party, to_parties
from ..auth import TokenOrTokenProvider, V1TokenNamespace

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = [
    "AccessConfig",
    "AccessConfigArgs",
    "create_access",
]

if TYPE_CHECKING:
    # We refer to the Config class in a docstring and
    # without this import, Sphinx can't resolve the reference
    # noinspection PyUnresolvedReferences
    from . import Config


def parties_from_env(*env_vars: str) -> Optional[AbstractSet[Party]]:
    """
    Read the set of parties
    """
    env_values = [os.getenv(env_var, "") for env_var in env_vars]
    if sum(map(len, env_values)) == 0:
        return None
    return {Party(p) for env_value in env_values for p in env_value.split(",") if p}


class AccessConfigArgs(TypedDict, total=False):
    user_id: Optional[str]
    read_as: Optional[Parties]
    act_as: Optional[Parties]
    admin: Optional[bool]
    ledger_id: Optional[str]
    application_name: Optional[str]
    token: Optional[TokenOrTokenProvider]
    oauth_token: Optional[str]
    oauth_token_file: Optional[str]


def create_access(**kwargs: Unpack[AccessConfigArgs]) -> AccessConfig:
    """
    Create an appropriate instance of :class:`AccessConfig`.

    See :meth:`Config.create` for a more detailed description of these parameters.
    """
    # BUG: mypy 1.18 is unhappy with kwargs.get(SOME_STR, os.getenv(OTHER_STR, "")),
    #  so rewrite this in a way that it has less problems with
    user_id: str = kwargs.get("user_id") or os.getenv("DAML_USER_ID") or ""
    read_as = kwargs.get("read_as", parties_from_env("DAML_LEDGER_READ_AS", "DABL_PUBLIC_PARTY"))
    act_as = kwargs.get("act_as", parties_from_env("DAML_LEDGER_ACT_AS", "DAML_LEDGER_PARTY"))
    admin = kwargs.get("admin", None)
    ledger_id: str = kwargs.get("ledger_id") or os.getenv("DAML_LEDGER_ID") or ""
    application_name = kwargs.get("application_name", os.getenv("DAML_LEDGER_APPLICATION_NAME"))

    token = kwargs.get("token", None)
    if token is None:
        oauth_token = kwargs.get("oauth_token", os.getenv("DAML_LEDGER_OAUTH_TOKEN"))
        if oauth_token:
            token = oauth_token
        else:
            oauth_token_file = kwargs.get(
                "oauth_token_file", os.getenv("DAML_LEDGER_OAUTH_TOKEN_FILE")
            )
            if oauth_token_file is not None:
                token = lambda: Path(oauth_token_file).read_text().strip()

    return AccessConfig(
        user_id=user_id,
        read_as=read_as,
        act_as=act_as,
        admin=admin,
        ledger_id=ledger_id,
        application_name=application_name,
        token=token,
    )


def parties(*pp: Optional[Collection[str]]) -> Parties:
    s = set[Party]()
    for p in pp:
        if p is not None:
            s.update(to_parties(p))
    return sorted(s)


@dataclass
class AccessConfig:
    """
    Configuration parameters for providing access to a ledger.
    """

    user_id: Optional[str]
    read_as: Optional[Parties]
    act_as: Optional[Parties]
    admin: Optional[bool]
    ledger_id: Optional[str]
    application_name: Optional[str]
    token: Optional[TokenOrTokenProvider]

    def __init__(
        self,
        *,
        user_id: Optional[str] = None,
        read_as: Optional[Parties] = None,
        act_as: Optional[Parties] = None,
        admin: Optional[bool] = None,
        ledger_id: Optional[str] = None,
        application_name: Optional[str] = None,
        token: Optional[TokenOrTokenProvider] = None,
    ) -> None:
        self.user_id = user_id
        self.read_as = read_as
        self.act_as = act_as
        self.admin = admin
        self.ledger_id = ledger_id
        self.application_name = application_name
        self.token = token


def decode_token_claims(token: str) -> Mapping[str, Any]:
    """
    Decode the claims section from a JSON Web Token (JWT).

    Note that the signature is NOT verified; this is the responsibility of the caller!
    """
    components = token.split(".", 3)
    if len(components) != 3:
        raise ValueError("not a JWT")

    pad_bytes = "=" * (-len(components[1]) % 4)
    claim_str = base64.urlsafe_b64decode(components[1] + pad_bytes)
    return json.loads(claim_str)


def encode_unsigned_token(
    read_as: Optional[Collection[Party]],
    act_as: Optional[Collection[Party]],
    ledger_id: Optional[str],
    application_id: Optional[str],
    admin: bool = True,
) -> bytes:
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
