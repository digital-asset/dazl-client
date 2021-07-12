.. Copyright (c) 2017-2021 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
   SPDX-License-Identifier: Apache-2.0

:mod:`daml.ledger.auth` — authentication utilities
==================================================

.. py:currentmodule:: dazl.ledger.auth

This module contains functions and type declarations for working with JSON Web Tokens (JWT) in a
format understood by Daml ledgers.

JSON Web Tokens and Daml claims
-------------------------------

The symbols in this module can be used to inspect JWTs that are intended to be used for accessing
Daml ledgers. Call :func:`decode_jwt_unverified` if you have a JWT that you wish to inspect.

The capabilities expressible by JWT Daml claims are documented
`here <https://docs.daml.com/app-dev/authorization.html>`_, and the format of a JWT as expected by
Ledger API implementations is documented on the help page for the
`Daml Sandbox <https://docs.daml.com/tools/sandbox.html#sandbox-authorization>`_.


For **testing purposes**, you may want to build your own JWTs. You can use
:func:`encode_jwt_unsigned`, which produces a valid JWT with no signature.

.. py:class:: DamlClaims

   Strongly-typed dict that describes the fields of a JWT with Daml-specific claims. Note that
   because this is ultimately a ``dict`` type, use the appropriate syntax to read/write fields
   (e.g., ``claims["iss"]`` instead of ``claims.iss``).

   .. py:attribute:: iss
      :type: str

      Identifies the principal that issued the JWT (see ``iss``,
      `RFC 7519 4.1.1 <https://datatracker.ietf.org/doc/html/rfc7519#section-4.1.1>`_).

   .. py:attribute:: sub
      :type: str

      Identifies the principal that issued the JWT (see ``sub``,
      `RFC 7519 4.1.2 <https://datatracker.ietf.org/doc/html/rfc7519#section-4.1.2>`_).

   .. py:attribute:: aud
      :type: str | Collection[str]

      Identifies the audience of the JWT (see ``aud``,
      `RFC 7519 4.1.3 <https://datatracker.ietf.org/doc/html/rfc7519#section-4.1.3>`_).

   .. py:attribute:: exp
      :type: float

      Identifies the expiration time of the JWT (see ``exp``,
      `RFC 7519 4.1.4 <https://datatracker.ietf.org/doc/html/rfc7519#section-4.1.4>`_).

   .. py:attribute:: nbf
      :type: float

      The ``"nbf"`` (not before) claim identifies the time before which the JWT **must not** be
      accepted for processing. (see ``nbf``,
      `RFC 7519 4.1.5 <https://datatracker.ietf.org/doc/html/rfc7519#section-4.1.5>`_).

   .. py:attribute:: iat
      :type: float

      The ``"iat"`` (issued at) claim identifies the time at which the JWT was issued (see ``iat``,
      `RFC 7519 4.1.6 <https://datatracker.ietf.org/doc/html/rfc7519#section-4.1.6>`_).

   .. py:attribute:: jti
      :type: str

      The ``"jti"`` (JWT ID) claim provides a unique identifier for the JWT. (see ``jti``,
      `RFC 7519 4.1.7 <https://datatracker.ietf.org/doc/html/rfc7519#section-4.1.7>`_).

   .. py:attribute:: https://daml.com/ledger-api/

      The private claim that contains information specific to Daml ledgers. This claim is an object
      with several properties:

      .. py:attribute:: readAs
         :type: Collection[str]

         The set of parties on whose behalf (in addition to all parties listed in ``act_as``)
         contracts can be retrieved
         (see ``readAs``, `Sandbox, Token Payload <https://docs.daml.com/tools/sandbox.html#token-payload>`_).

      .. py:attribute:: actAs
         :type: Collection[str]

         The set of parties on whose behalf commands should be executed.
         (see ``actAs``, `Sandbox, Token Payload <https://docs.daml.com/tools/sandbox.html#token-payload>`_).

      .. py:attribute:: ledgerId
         :type: str

         the ledger id

      .. py:attribute:: applicationId
         :type: str

         the application id
      .. py:attribute:: admin
         :type: bool

         ``True`` if admin endpoints can be used.

.. py:data:: DamlV1ClaimName
    :value: "https://daml.com/ledger-api"

    The key in a JWT payload that contains Daml ledger-specific claims (documented in detail on the
    help page for https://docs.daml.com/tools/sandbox.html#sandbox-authorization).

.. py:class:: DamlClaimValue

   A :class:`typing.TypedDict` definition that describes the value of the Daml claim named
   ``"https://daml.com/ledger-api/"`` (see :class:`DamlClaims`).


Decoding Claims
---------------

.. py:function:: decode_jwt_unverified(jwt: str | bytes) -> DamlClaims

    Decode a JSON web token *without* validating the signature of the JWT.

    If you want to validate JWTs on the client-side, use a third-party library, such as
    `PyJWT <https://pyjwt.readthedocs.io/en/stable/>`_. If you trust your authentication server
    and/or do not need information from the JWT, you can treat JWTs as opaque strings and you don't
    need to call this function.


Encoding Claims
---------------

You generally do not encode your own JWT's; they are given to you by an authentication server that
validates your identity and provides you with authorizations in the form of a Daml JWT.
Consequently, these functions really only have applicability in a testing context.

.. py:function:: daml_claims(**kwargs) -> DamlClaims

   Create a :class:`dict` that encode claims as a JWT. All parameters are optional and keyword-only.

   :param str iss:
      Identifies the issuer of the JWT (see :attr:`DamlClaims["iss"] <DamlClaims.iss>`).
   :param str sub:
      Identifies the subject of the JWT (see :attr:`DamlClaims["sub"] <DamlClaims.sub>`).
   :param str | Collection[str] aud:
      Identifies the audience of the JWT (see :attr:`DamlClaims["aud"] <DamlClaims.aud>`).
   :param str | Collection[str] read_as:
      The set of read parties (see :attr:`DamlClaims["https://daml.com/ledger-api/"]["readAs"] <DamlClaims.readAs>`).
   :param str | Collection[str] act_as:
      The set of read parties (see :attr:`DamlClaims["https://daml.com/ledger-api/"]["actAs"] <DamlClaims.actAs>`).


.. py:function:: encode_jwt_unsigned(claims, /) -> bytes

    Encode a JSON Web Token (JWT) for the specified claims. The resultant JWT is *not* signed, and
    should only be used in testing scenarios!

    :param DamlClaims claims: The Daml claims to use to produce a JWT (positional argument only).
    :return: The JWT-encoded form of claim.
