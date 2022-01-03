# Copyright (c) 2017-2022 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0


from datetime import timedelta
from typing import TYPE_CHECKING, ClassVar, Optional

from ..prim import Party
from .api import MetricEvents

if TYPE_CHECKING:
    from prometheus_client import Gauge
    from prometheus_client.registry import CollectorRegistry


__all__ = ["PrometheusMetricEvents"]


class PrometheusMetricEvents(MetricEvents):

    _DEFAULT = None  # type: ClassVar[PrometheusMetricEvents]

    @classmethod
    def default(cls):
        if PrometheusMetricEvents._DEFAULT is not None:
            return PrometheusMetricEvents._DEFAULT
        else:
            from prometheus_client import REGISTRY

            PrometheusMetricEvents._DEFAULT = PrometheusMetricEvents(REGISTRY)
            return PrometheusMetricEvents._DEFAULT

    def __init__(self, registry: "Optional[CollectorRegistry]" = None):
        from prometheus_client import REGISTRY, Gauge

        if registry is None:
            registry = REGISTRY

        self._loop_responsiveness_seconds = Gauge(
            "dazl_network_loop_responsiveness_seconds",
            "Number of seconds to immediately schedule and execute a no-op on the event loop",
            registry=registry,
        )

    def loop_responsiveness(self, responsiveness: "timedelta") -> None:
        self._loop_responsiveness_seconds.set(responsiveness.total_seconds())

    def party_offset(self, party: "Party", offset: str) -> None:
        pass
