# Copyright (c) 2019 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0


from datetime import timedelta
from ..model.core import Party


class MetricEvents:

    def loop_responsiveness(self, responsiveness: 'timedelta') -> None:
        """
        Record the length of time it takes to immediately schedule and execute a no-op on the event
        loop. This measurement can be used to get a sense of how "backed up" the current event loop
        is.

        :param responsiveness:
            The length of time between the scheduling of an action and the invocation of it.
        """

    def party_offset(self, party: 'Party', offset: str) -> None:
        """
        Record that a party has reached a certain block offset.

        :param party: The party that has reached an offset.
        :param offset: The offset that has been reached.
        """
