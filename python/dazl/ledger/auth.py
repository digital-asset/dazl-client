# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

import base64
import json
import sys
from typing import Callable, Literal, Optional, final

from ..prim import Parties

if sys.version_info >= (3, 11):
    from typing import TypeAlias
else:
    from typing_extensions import TypeAlias

__all__ = [
    "TokenOrTokenProvider",
    "V1TokenNamespace",
    "get_token",
    "parse_token",
    "ParsedToken",
    "ParsedV1Token",
    "ParsedV2Token",
]

TokenOrTokenProvider: TypeAlias = str | Callable[[], Optional[str]]


V1TokenNamespace = "https://daml.com/ledger-api"
V2Scope = "daml_ledger_api"


@final
class ParsedV1Token:
    """
    Salient fields from a token used by Daml 1.
    """

    @property
    def token_version(self) -> Literal[1]:
        """
        Always returns "1".
        """
        return 1

    def __init__(
        self,
        read_as: Optional[Parties] = None,
        act_as: Optional[Parties] = None,
        admin: Optional[bool] = None,
        ledger_id: Optional[str] = None,
        application_name: Optional[str] = None,
    ) -> None:
        self.read_as = read_as
        self.act_as = act_as
        self.admin = admin
        self.ledger_id = ledger_id
        self.application_name = application_name

    read_as: Optional[Parties]
    act_as: Optional[Parties]
    admin: Optional[bool]
    ledger_id: Optional[str]
    application_name: Optional[str]


@final
class ParsedV2Token:
    """
    Salient fields from a token used by Daml 2 and later.
    """

    @property
    def token_version(self) -> Literal[2]:
        """
        Always returns "2".
        """
        return 2

    def __init__(self, user_id: str) -> None:
        self.user_id = user_id


ParsedToken: TypeAlias = ParsedV1Token | ParsedV2Token


def get_token(t: Optional[TokenOrTokenProvider], /) -> Optional[str]:
    """
    Get a token.

    :param t:
        Either:
         - None
         - a string that is a valid Daml JWT
         - a function that returns a valid Daml JWT, or None
    :return:
        A Daml JWT if one could be returned or None.
    :exception TypeError:
        raised if an unknown type is passed in, or returned from the function
    """
    if t is None:
        return None
    elif isinstance(t, str):
        return t
    elif callable(t):
        r = t()
        if r is None:
            return None
        elif isinstance(r, str):
            return r
        else:
            raise TypeError(f"a token provider function returned an invalid type: {type(r)}")
    else:
        raise TypeError(f"invalid type of a token provider: {type(t)}")


def parse_token(t: str, /) -> ParsedToken:
    components = t.split(".", 3)
    if len(components) != 3:
        raise ValueError("not a JWT")

    pad_bytes = "=" * (-len(components[1]) % 4)
    claim_str = base64.urlsafe_b64decode(components[1] + pad_bytes)
    claims = json.loads(claim_str)

    has_v2_scope_marker = V2Scope in claims.get("scope", "").split(" ")
    v1_claims = claims.get(V1TokenNamespace)

    if has_v2_scope_marker:
        # "scope": "daml_ledger_api" definitely marks this as a Daml v2 token;
        # the absence of the v1 namespace also marks this as a token that
        # Daml v2 and later ledgers understand
        user_id = claims.get("sub")
        if user_id is None:
            raise ValueError("sub is a required field in a Daml token")
        return ParsedV2Token(user_id)
    elif v1_claims is not None:
        # we found Daml V1 claims, so assume it's a Daml V1 token
        return ParsedV1Token(
            read_as=frozenset(v1_claims.get("readAs", ())),
            act_as=frozenset(v1_claims.get("actAs", ())),
            admin=bool(v1_claims.get("admin", False)),
            ledger_id=v1_claims.get("ledgerId", None),
            application_name=v1_claims.get("applicationId", None),
        )
    else:
        user_id = claims.get("sub")
        if user_id is None:
            raise ValueError("sub is a required field in a Daml token")
        return ParsedV2Token(user_id)
