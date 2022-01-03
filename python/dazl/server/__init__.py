# Copyright (c) 2017-2022 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from aiohttp import web

from ..client import _NetworkImpl


def get_app(network: "_NetworkImpl") -> "web.Application":
    from .management import build_routes as build_management_routes
    from .metrics import build_routes as build_metrics_routes

    app = web.Application()
    app.add_routes(build_metrics_routes(network))
    app.add_routes(build_management_routes(network))
    return app
