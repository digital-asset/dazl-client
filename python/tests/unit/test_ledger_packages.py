# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

import logging
from typing import Any

from dazl.api import (
    AuthenticatedClient,
    File,
    ListPackagesResponse,
    ListVettedPackagesRequest,
    get_v2_interactive_submission_preferred_package_version,
    get_v2_package_vetting,
    get_v2_packages,
    get_v2_packages_package_id,
    get_v2_packages_package_id_status,
    post_v2_packages,
)
import httpx
import pytest


@pytest.mark.asyncio
async def test_get_package_by_id_via_api(sandbox_v3: Any) -> None:
    timeout = httpx.Timeout(10.0, connect=5.0)
    async with AuthenticatedClient(
        base_url=sandbox_v3.url, token="test-token", timeout=timeout
    ) as client:
        packages_response = await get_v2_packages.asyncio(client=client)
        assert isinstance(packages_response, ListPackagesResponse)
        assert packages_response.package_ids is not None
        assert isinstance(packages_response.package_ids, list)

        if len(packages_response.package_ids) > 0:
            package_id = packages_response.package_ids[0]

            response = await get_v2_packages_package_id.asyncio(
                client=client, package_id=package_id
            )

            assert response is not None
            logging.info(f"Retrieved package: {package_id}")
        else:
            logging.info("No packages available to test")


@pytest.mark.asyncio
async def test_get_package_status_via_api(sandbox_v3: Any) -> None:
    timeout = httpx.Timeout(10.0, connect=5.0)
    async with AuthenticatedClient(
        base_url=sandbox_v3.url, token="test-token", timeout=timeout
    ) as client:
        packages_response = await get_v2_packages.asyncio(client=client)
        assert isinstance(packages_response, ListPackagesResponse)
        assert packages_response.package_ids is not None
        assert isinstance(packages_response.package_ids, list)

        if len(packages_response.package_ids) > 0:
            package_id = packages_response.package_ids[0]

            response = await get_v2_packages_package_id_status.asyncio(
                client=client, package_id=package_id
            )

            assert response is not None
            logging.info(f"Package status for {package_id} retrieved")
        else:
            logging.info("No packages available to test")


@pytest.mark.asyncio
async def test_list_vetted_packages_via_api(sandbox_v3: Any) -> None:
    timeout = httpx.Timeout(10.0, connect=5.0)
    async with AuthenticatedClient(
        base_url=sandbox_v3.url, token="test-token", timeout=timeout
    ) as client:
        request_body = ListVettedPackagesRequest(
            page_token="",
            page_size=100,
        )

        response = await get_v2_package_vetting.asyncio(client=client, body=request_body)

        assert response is not None
        logging.info(f"Vetted packages response received")


@pytest.mark.asyncio
async def test_get_preferred_package_version_via_api(sandbox_v3: Any) -> None:
    timeout = httpx.Timeout(10.0, connect=5.0)
    async with AuthenticatedClient(
        base_url=sandbox_v3.url, token="test-token", timeout=timeout
    ) as client:
        packages_response = await get_v2_packages.asyncio(client=client)
        assert isinstance(packages_response, ListPackagesResponse)
        assert packages_response.package_ids is not None
        assert isinstance(packages_response.package_ids, list)

        if len(packages_response.package_ids) > 0:
            package_name = "test-package"

            response = await get_v2_interactive_submission_preferred_package_version.asyncio(
                client=client, package_name=package_name
            )
            assert response is not None

            logging.info(f"Preferred package version response received")
        else:
            logging.info("No packages available to test")


@pytest.mark.asyncio
async def test_upload_dar_package_via_api(sandbox_v3: Any) -> None:
    from io import BytesIO

    timeout = httpx.Timeout(10.0, connect=5.0)
    async with AuthenticatedClient(
        base_url=sandbox_v3.url, token="test-token", timeout=timeout
    ) as client:
        dar_content = BytesIO(b"fake-dar-content")
        dar_file = File(
            payload=dar_content,
            file_name="test.dar",
            mime_type="application/octet-stream",
        )

        response = await post_v2_packages.asyncio(client=client, body=dar_file)
        assert response is not None

        logging.info(f"Upload DAR response: {response}")
