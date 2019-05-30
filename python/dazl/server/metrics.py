from typing import Collection

from aiohttp import web


def build_routes(prefix: str = '/metrics', registry=None) -> 'Collection[web.RouteDef]':
    routes = web.RouteTableDef()

    from prometheus_client import exposition, REGISTRY

    if registry is None:
        registry = REGISTRY

    @routes.get(prefix)
    async def get_metrics(request: 'web.Request') -> 'web.Response':
        encoder, content_type = exposition.choose_encoder(request.headers['Accept'])
        metrics_bytes: bytes = encoder(registry)
        return web.HTTPOk(body=metrics_bytes, content_type='text/plain; version=0.0.4')

    return routes
