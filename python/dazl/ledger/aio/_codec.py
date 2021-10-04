# Copyright (c) 2017-2021 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from typing import AbstractSet, Any, Generic, Optional, Sequence, Set, Tuple, TypeVar

from . import PackageService
from ...damlast import TypeConName
from ...damlast.daml_lf_1 import DefTemplate, TemplateChoice, Type
from ...damlast.lookup import MultiPackageLookup
from ...values import Context, ValueMapper
from ..pkgcache import SHARED_PACKAGE_DATABASE
from .pkgloader import PackageLoader

E = TypeVar("E", bound=ValueMapper)
D = TypeVar("D", bound=ValueMapper)

__all__ = ["CoreCodecFactory", "CoreCodec"]


class CoreCodecFactory(Generic[E, D]):
    def __init__(self, encoder: E, decoder: D):
        self.encoder = encoder
        self.decoder = decoder

    def build(self, conn: "PackageService", lookup: "Optional[MultiPackageLookup]" = None):
        return CoreCodec(conn, lookup=lookup, encoder=self.encoder, decoder=self.decoder)


class CoreCodec(Generic[E, D]):
    """
    Shared code for codecs.
    """

    def __init__(
        self,
        conn: "PackageService",
        *,
        lookup: "Optional[MultiPackageLookup]" = None,
        encoder: E,
        decoder: D,
    ):
        self.conn = conn
        self.encoder = encoder
        self.decoder = decoder
        self.lookup = lookup or SHARED_PACKAGE_DATABASE
        self._loader = PackageLoader(self.lookup, conn)
        self._encode_context = Context(encoder, self.lookup)
        self._decode_context = Context(decoder, self.lookup)

    async def encode_value(self, __type: "Type", __obj: "Any") -> "Any":
        return await self._loader.do_with_retry(self._encode_context.convert(__type, __obj))

    async def decode_value(self, __type: "Type", __obj: "Any") -> "Any":
        return await self._loader.do_with_retry(self._decode_context.convert(__type, __obj))

    async def look_up_type(self, __template_id: "Any"):
        return await self._loader.do_with_retry(lambda: self.lookup.template_name(__template_id))

    async def look_up_types(
        self, __template_ids: "Sequence[TypeConName]"
    ) -> "AbstractSet[TypeConName]":
        requested_types = set()  # type: Set[TypeConName]
        for template_id in __template_ids:
            requested_types.update(
                await self._loader.do_with_retry(lambda: self.lookup.template_names(template_id))
            )
        return requested_types

    async def look_up_choice(
        self, template_id: "Any", choice_name: str
    ) -> "Tuple[TypeConName, DefTemplate, TemplateChoice]":
        template_type = await self._loader.do_with_retry(
            lambda: self.lookup.template_name(template_id)
        )
        template = self.lookup.template(template_type)
        for choice in template.choices:
            if choice.name == choice_name:
                return template_type, template, choice
        raise ValueError(f"template {template.tycon} has no choice named {choice_name}")
