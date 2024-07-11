# Copyright (c) 2017-2024 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from datetime import datetime
from uuid import uuid4

from dazl import connect
import pytest

from .dars import Simple


@pytest.mark.asyncio
async def test_ledger_metrics(sandbox_v2) -> None:
    app_name = uuid4().hex

    async with connect(url=sandbox_v2.url, admin=True, application_name=app_name) as conn:
        report = await conn.get_metering_report(datetime.fromtimestamp(0), application_id=app_name)
        assert len(report.applications) == 0

        party_info = await conn.allocate_party()
        await conn.upload_package(Simple.read_bytes())

        await conn.create(
            "Simple:OperatorNotification",
            {"operator": party_info.party, "theObservers": [], "text": "some_stuff"},
            act_as=party_info.party,
        )
        await conn.create(
            "Simple:OperatorNotification",
            {"operator": party_info.party, "theObservers": [], "text": "more_stuff"},
            act_as=party_info.party,
        )
        report = await conn.get_metering_report(datetime.fromtimestamp(0), application_id=app_name)
        assert len(report.applications) == 1
        assert report.applications[0].events == 2
