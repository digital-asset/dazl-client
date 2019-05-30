# Copyright (c) 2019 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from aiohttp import web


def get_app() -> 'web.Application':
    from .metrics import build_routes as build_metrics_routes
    app = web.Application()
    app.add_routes(build_metrics_routes())
    return app
