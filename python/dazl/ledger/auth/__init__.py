# Copyright (c) 2017-2022 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""
This module contains functions and type declarations for working with JSON Web Tokens (JWT) in a
format understood by Daml ledgers.
"""

from __future__ import annotations

# NOTE: We intentionally do NOT use a third-party library to encode/decode JWTs to avoid prescribing
#  a specific JWT library onto libraries that use dazl. The *tests*, however, use PyJWT for JWT
#  generation, specifically where signed JWTs are used.
import base64
from datetime import datetime, timedelta
import json
import sys
from typing import Any, Collection, Optional, Union

from ...prim import Party, to_parties

if sys.version_info >= (3, 8):
    from typing import Literal, TypedDict
else:
    from typing_extensions import Literal, TypedDict


__all__ = [
    "DamlV1ClaimName",
    "DamlV1Claims",
    "DamlClaims",
    "decode_jwt_unverified",
    "encode_jwt_unsigned",
    "daml_claims",
]


DamlV1ClaimName: Literal["https://daml.com/ledger-api"] = "https://daml.com/ledger-api"


class DamlV1Claims(TypedDict, total=False):
    readAs: Optional[Collection[Party]]
    actAs: Optional[Collection[Party]]
    ledgerId: str
    applicationId: str
    admin: bool


DamlClaims = TypedDict(
    "DamlClaims",
    {
        "iss": str,
        "sub": str,
        "aud": Union[str, Collection[str]],
        "exp": float,
        "nbf": float,
        "iat": float,
        "jti": str,
        # Unfortunately, the Daml V1 namespace string here must be a string, and not a constant value:
        #  https://github.com/python/mypy/issues/4128
        "https://daml.com/ledger-api": DamlV1Claims,
    },
    total=False,
)


def decode_jwt_unverified(jwt: "Union[str, bytes]") -> "DamlClaims":
    """
    Decode a JSON web token *without* validating the signature of the JWT.

    :param jwt: A valid JSON Web Token (JWT).
    :return: A :class:`DamlClaims`.
    :raise ValueError: if the ``jwt`` is malformed or otherwise unrecognizable
    """
    if isinstance(jwt, bytes):
        # JWTs are supposed to be base64-encoded, so an ASCII decoding is more
        # than sufficient for a valid JWT
        jwt = jwt.decode("ascii")

    components = jwt.split(".", maxsplit=3)
    if len(components) != 3:
        raise ValueError("not a JWT")

    payload_encoded = components[1]
    payload_encoded += "=" * (-(len(payload_encoded) % -4))
    return json.loads(base64.urlsafe_b64decode(payload_encoded))


def encode_jwt_unsigned(__claims: "DamlClaims") -> "bytes":
    """
    Encode a JSON Web Token (JWT) for the specified claims. The resultant JWT is *not* signed, and
    should only be used in testing scenarios!

    :param __claims:
        The Daml claims to use to produce a JWT. This parameter should only be passed as a
        positional parameter.
    :return: The JWT-encoded form of claim.
    """
    hdr = {"alg": "none", "typ": "JWT"}
    return encode_jwt_segment(hdr) + b"." + encode_jwt_segment(__claims) + b"."


def encode_jwt_segment(s: Any) -> bytes:
    return base64.urlsafe_b64encode(json.dumps(s).encode("utf-8"))


def daml_claims(
    *,
    iss: Optional[str] = None,
    sub: Optional[str] = None,
    aud: Union[None, str, Collection[str]] = None,
    exp: Union[None, int, float, str, datetime, timedelta] = None,
    nbf: Union[None, int, float, str, datetime, timedelta] = None,
    iat: Union[None, int, float, str, datetime, timedelta] = None,
    jti: Optional[str] = None,
    read_as: Union[None, str, Party, Collection[str], Collection[Party]] = None,
    act_as: Union[None, str, Party, Collection[str], Collection[Party]] = None,
    ledger_id: Optional[str] = None,
    application_id: Optional[str] = None,
    admin: Optional[bool] = None,
) -> "DamlClaims":
    """
    Return a dict that can be used as the payload for a JWT.

    This function is not normally useful other than in tests; if you want to connect to a ledger
    that requires authorization, consult the documentation for your targer ledger to determine how
    to obtain a properly signed token for that ledger.

    :param iss:
        Identifies the principal that issued the JWT (``iss``).

    :param sub:
        Identifies the subject of the JWT (``sub``).

    :param aud:
        Identifies the recipients that the JWT is intended for. Each principal intended to process
        the JWT must identify itself with a value in the audience claim. If the principal processing
        the claim does not identify itself with a value in the aud claim when this claim is present,
        then the JWT must be rejected.

        Note that this field is permitted to be *either* a string or a collection of strings, and
        in Python, strings are also iterables over strings. If you want to distinguish between the
        case of a ``str`` or collection of ``str``, use ``isinstance(payload["aud"], str)``.

    :param exp:
        Identifies the expiration time on and after which the JWT must not be accepted for
        processing (``exp`` as defined in RFC 7519, 4.1.4).

    :param nbf:
        The ``"nbf"`` (not before) claim identifies the time before which the JWT MUST NOT be
        accepted for processing. The processing of the ``"nbf"`` claim requires that the current
        date/time MUST be after or equal to the not-before date/time listed in the ``"nbf"`` claim.
        Implementers MAY provide for some small leeway, usually no more than a few minutes, to
        account for clock skew.

        Its value MUST be a number containing a NumericDate value.

        Use of this claim is OPTIONAL.

        ``nbf`` is defined in RFC 7519, 4.1.5.

    :param iat:
        The ``"iat"`` (issued at) claim identifies the time at which the JWT was issued. This claim
        can be used to determine the age of the JWT.

        Its value MUST be a number containing a NumericDate value.

        Use of this claim is OPTIONAL.

        ``iat`` is defined in RFC 7519, 4.1.6.

    :param jti:
        The ``"jti"`` (JWT ID) claim provides a unique identifier for the JWT. The identifier value
        MUST be assigned in a manner that ensures that there is a negligible probability that the
        same value will be accidentally assigned to a different data object; if the application
        uses multiple issuers, collisions MUST be prevented among values produced by different
        issuers as well.  The ``"jti"`` claim can be used to prevent the JWT from being replayed.
        The "jti" value is a case-sensitive string.

        Use of this claim is OPTIONAL.

        ``jti`` is defined in RFC 7519, 4.1.7.

    :param read_as:
        A party or set of parties on whose behalf (in addition to all parties listed in ``act_as``)
        contracts can be retrieved.

    :param act_as:
        A party or set of parties on whose behalf commands should be executed. Parties here are also
        implicitly granted ``read_as`` access as well.

    :param ledger_id:
        The ledger ID to connect to.

        This value is OPTIONAL for gRPC Ledger API over Daml v1 (it will be inferred from the target
        ledger).

        This value is REQUIRED for the HTTP JSON API over Daml v1.

        This value is DEPRECATED for gRPC Ledger API and HTTP JSON API over Daml v2 or later.

    :param application_id:
        A string that identifies this application. This is used for tracing purposes on the
        server-side.

    :param admin:
        ``True`` to allow admin endpoints to be used. This flag is ignored when connecting to
        gRPC Ledger API implementations.
    """
    p = dict()  # type: DamlClaims

    if iss:
        p["iss"] = iss

    if sub:
        p["sub"] = sub

    if aud:
        p["aud"] = aud

    if exp:
        p["exp"] = jwt_normalize_date(exp)

    if nbf:
        p["nbf"] = jwt_normalize_date(nbf)

    if iat:
        p["iat"] = jwt_normalize_date(iat)

    if jti:
        p["jti"] = jti

    read_as_ = to_parties(read_as)
    if read_as_:
        if DamlV1ClaimName not in p:
            p[DamlV1ClaimName] = {}
        p[DamlV1ClaimName]["readAs"] = sorted(read_as_)

    act_as_ = to_parties(act_as)
    if act_as_:
        if DamlV1ClaimName not in p:
            p[DamlV1ClaimName] = {}
        p[DamlV1ClaimName]["actAs"] = sorted(act_as_)

    if ledger_id:
        if DamlV1ClaimName not in p:
            p[DamlV1ClaimName] = {}
        p[DamlV1ClaimName]["ledgerId"] = ledger_id

    if application_id:
        if DamlV1ClaimName not in p:
            p[DamlV1ClaimName] = {}
        p[DamlV1ClaimName]["applicationId"] = application_id

    if admin is not None:
        if DamlV1ClaimName not in p:
            p[DamlV1ClaimName] = {}
        p[DamlV1ClaimName]["admin"] = admin

    return p


def jwt_normalize_date(d: Union[float, str, datetime, timedelta]) -> float:
    """
    Convert a value to a ``NumericDate`` as per the JWT spec (see RFC 7519, 2).

    ``NumericDate`` is a JSON numeric value representing the number of seconds from
    ``1970-01-01T00:00:00 UTC`` until the specified UTC date/time, ignoring leap seconds.
    This is equivalent to the IEEE Std 1003.1, 2013 Edition [POSIX.1] definition "Seconds
    Since the Epoch", in which each day is accounted for by exactly 86400 seconds, other
    than that non-integer values can be represented.  See RFC 3339 for details regarding
    date/times in general and UTC in particular.
    """
    if isinstance(d, (int, float)):
        return d
    elif isinstance(d, str):
        return float(d)

    if isinstance(d, timedelta):
        d = datetime.utcnow() + d

    if isinstance(d, datetime):
        return d.timestamp()

    raise ValueError("unknown date format")
