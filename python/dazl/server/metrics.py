# Copyright (c) 2017-2022 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from dataclasses import asdict, dataclass
from typing import TYPE_CHECKING, Collection, Mapping

from ..client import _NetworkImpl
from ..prim import Party

if TYPE_CHECKING:
    from aiohttp import web


def build_routes(network_impl: "_NetworkImpl", registry=None) -> "Collection[web.AbstractRouteDef]":
    # this import is optional, so do it as late as possible
    from aiohttp import web

    routes = web.RouteTableDef()

    from prometheus_client import REGISTRY, exposition

    if registry is None:
        registry = REGISTRY

    @dataclass(frozen=True)
    class ReadyResult:
        parties: "Mapping[Party, ReadyPartyResult]"

    @dataclass(frozen=True)
    class ReadyPartyResult:
        url: str
        ready: bool

    @routes.get("/metrics")
    async def get_metrics(request: "web.Request") -> "web.Response":
        encoder, content_type = exposition.choose_encoder(request.headers["Accept"])
        metrics_bytes: bytes = encoder(registry)
        return web.HTTPOk(body=metrics_bytes, content_type="text/plain; version=0.0.4")

    @routes.get("/healthz")
    async def get_health(_: "web.Request") -> "web.Response":
        return web.json_response({})

    @routes.get("/readyz")
    async def get_ready(_: "web.Request") -> "web.Response":
        parties = {
            party_impl.party: ReadyPartyResult(
                ready=party_impl.ready().done(), url=party_impl.resolved_config().url
            )
            for party_impl in network_impl.party_impls()
        }
        return web.json_response(asdict(ReadyResult(parties=parties)))

    return routes
