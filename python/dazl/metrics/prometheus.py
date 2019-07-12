# Copyright (c) 2019 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0


from datetime import timedelta
from typing import ClassVar, Optional, TYPE_CHECKING

from .api import MetricEvents
from ..model.core import Party

if TYPE_CHECKING:
    from prometheus_client import Gauge
    from prometheus_client.registry import CollectorRegistry


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

    def __init__(self, registry: 'Optional[CollectorRegistry]' = None):
        from prometheus_client import Gauge, REGISTRY

        if registry is None:
            registry = REGISTRY

        self._loop_responsiveness_seconds = Gauge(
            'dazl_network_loop_responsiveness_seconds',
            'Number of seconds to immediately schedule and execute a no-op on the event loop',
            registry=registry)
        self._offset = Gauge(
            'dazl_party_offset',
            'current read offset',
            ['party'],
            registry=registry)

    def loop_responsiveness(self, responsiveness: 'timedelta') -> None:
        self._loop_responsiveness_seconds.set(responsiveness.total_seconds())

    def party_offset(self, party: 'Party', offset: str) -> None:
        if offset is not None:
            self._offset.labels(party).set(offset)
