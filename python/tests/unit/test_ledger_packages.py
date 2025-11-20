# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

import logging
from typing import Any

from dazl._gen_api import AuthenticatedClient
from dazl._gen_api.openapi.api.default import (
    get_v2_interactive_submission_preferred_package_version,
    get_v2_package_vetting,
    get_v2_packages,
    get_v2_packages_package_id,
    get_v2_packages_package_id_status,
    post_v2_interactive_submission_preferred_packages,
    post_v2_packages,
)
from dazl._gen_api.openapi.models.get_preferred_package_version_response import (
    GetPreferredPackageVersionResponse,
)
from dazl._gen_api.openapi.models.get_preferred_packages_request import GetPreferredPackagesRequest
from dazl._gen_api.openapi.models.list_packages_response import ListPackagesResponse
from dazl._gen_api.openapi.models.list_vetted_packages_request import ListVettedPackagesRequest
import httpx
import pytest


@pytest.mark.asyncio
async def test_list_packages_via_api(sandbox_v3: Any) -> None:
    timeout = httpx.Timeout(10.0, connect=5.0)
    async with AuthenticatedClient(
        base_url=sandbox_v3.url, token="test-token", timeout=timeout
    ) as client:
        response = await get_v2_packages.asyncio(client=client)

        assert isinstance(response, ListPackagesResponse)
        assert response.package_ids is not None
        assert isinstance(response.package_ids, list)

        for package_id in response.package_ids:
            logging.info(f"Package: {package_id}")


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

            logging.info(f"Preferred package version response received")
        else:
            logging.info("No packages available to test")


@pytest.mark.asyncio
async def test_upload_dar_package_via_api(sandbox_v3: Any) -> None:
    timeout = httpx.Timeout(10.0, connect=5.0)
    async with AuthenticatedClient(
        base_url=sandbox_v3.url, token="test-token", timeout=timeout
    ) as client:
        httpx_client = client.get_async_httpx_client()
        response = await httpx_client.post(
            "/v2/packages",
            files={"darFile": ("test.dar", b"fake-dar-content", "application/octet-stream")},
        )

        logging.info(f"Upload DAR response: {response.status_code} - {response.text}")
