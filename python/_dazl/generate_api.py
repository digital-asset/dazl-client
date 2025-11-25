# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

import logging
from pathlib import Path
import shutil
import subprocess
import sys

from .codegen.python_header import HEADER

logger = logging.getLogger("_dazl.generate_api")

__all__ = ["generate_api_clients"]


def _add_copyright_headers(directory: Path) -> None:
    for py_file in directory.rglob("*.py"):
        content = py_file.read_text()
        if not content.startswith("# Copyright"):
            py_file.write_text(HEADER + content)
            logger.debug(f"Added copyright header to {py_file}")


def _fix_missing_response_models(directory: Path) -> None:
    openapi_dir = directory / "openapi"
    models_dir = openapi_dir / "models"
    api_dir = openapi_dir / "api" / "default"

    response_file = models_dir / "list_vetted_packages_response.py"
    response_content = (
        HEADER
        + '''from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.vetted_package import VettedPackage


T = TypeVar("T", bound="ListVettedPackagesResponse")


@_attrs_define
class ListVettedPackagesResponse:
    """
    Attributes:
        next_page_token (str): Pagination token to fetch the next page.
        vetted_packages (list[VettedPackage]): List of vetted packages.
    """

    next_page_token: str
    vetted_packages: list[VettedPackage]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        next_page_token = self.next_page_token

        vetted_packages = []
        for vetted_packages_item_data in self.vetted_packages:
            vetted_packages_item = vetted_packages_item_data.to_dict()
            vetted_packages.append(vetted_packages_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "nextPageToken": next_page_token,
                "vettedPackages": vetted_packages,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.vetted_package import VettedPackage

        d = dict(src_dict)
        next_page_token = d.pop("nextPageToken", "")

        vetted_packages = []
        _vetted_packages = d.pop("vettedPackages", [])
        for vetted_packages_item_data in _vetted_packages:
            vetted_packages_item = VettedPackage.from_dict(vetted_packages_item_data)
            vetted_packages.append(vetted_packages_item)

        list_vetted_packages_response = cls(
            next_page_token=next_page_token,
            vetted_packages=vetted_packages,
        )

        list_vetted_packages_response.additional_properties = d
        return list_vetted_packages_response

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
'''
    )
    response_file.write_text(response_content)
    logger.debug(f"Created {response_file}")

    api_file = api_dir / "get_v2_package_vetting.py"
    if api_file.exists():
        content = api_file.read_text()

        content = content.replace(
            "from ...models.list_vetted_packages_request import ListVettedPackagesRequest\nfrom ...types import Response",
            "from ...models.list_vetted_packages_request import ListVettedPackagesRequest\nfrom ...models.list_vetted_packages_response import ListVettedPackagesResponse\nfrom ...types import Response",
        )

        content = content.replace(
            "def _parse_response(\n    *, client: AuthenticatedClient | Client, response: httpx.Response\n) -> JsCantonError | str:\n    if response.status_code == 400:\n        response_400 = response.text\n        return response_400\n\n    response_default = JsCantonError.from_dict(response.json())\n\n    return response_default",
            "def _parse_response(\n    *, client: AuthenticatedClient | Client, response: httpx.Response\n) -> ListVettedPackagesResponse | JsCantonError | str:\n    if response.status_code == 200:\n        response_200 = ListVettedPackagesResponse.from_dict(response.json())\n        return response_200\n\n    if response.status_code == 400:\n        response_400 = response.text\n        return response_400\n\n    response_default = JsCantonError.from_dict(response.json())\n\n    return response_default",
        )

        content = content.replace(
            "Response[JsCantonError | str]",
            "Response[ListVettedPackagesResponse | JsCantonError | str]",
        )

        content = content.replace(
            ") -> JsCantonError | str | None:",
            ") -> ListVettedPackagesResponse | JsCantonError | str | None:",
        )

        content = content.replace(
            "    Returns:\n        JsCantonError | str",
            "    Returns:\n        ListVettedPackagesResponse | JsCantonError | str",
        )

        api_file.write_text(content)
        logger.debug(f"Fixed {api_file}")

    init_file = models_dir / "__init__.py"
    if init_file.exists():
        content = init_file.read_text()

        content = content.replace(
            "from .list_vetted_packages_request import ListVettedPackagesRequest\nfrom .map_int_field import MapIntField",
            "from .list_vetted_packages_request import ListVettedPackagesRequest\nfrom .list_vetted_packages_response import ListVettedPackagesResponse\nfrom .map_int_field import MapIntField",
        )

        content = content.replace(
            '    "ListVettedPackagesRequest",\n    "MapIntField",',
            '    "ListVettedPackagesRequest",\n    "ListVettedPackagesResponse",\n    "MapIntField",',
        )

        init_file.write_text(content)
        logger.debug(f"Updated {init_file}")


def _format_generated_code(directory: Path) -> None:
    venv_bin = Path(sys.executable).parent
    isort_exe = venv_bin / "isort"
    black_exe = venv_bin / "black"

    try:
        subprocess.run(
            [str(isort_exe), str(directory)],
            check=True,
            capture_output=True,
            text=True,
        )
        logger.debug("Successfully ran isort")
    except subprocess.CalledProcessError as e:
        logger.warning(f"isort failed: {e.stderr}")

    try:
        subprocess.run(
            [str(black_exe), str(directory)],
            check=True,
            capture_output=True,
            text=True,
        )
        logger.debug("Successfully ran black")
    except subprocess.CalledProcessError as e:
        logger.warning(f"black failed: {e.stderr}")


def generate_api_clients(openapi_specs_dir: Path, output_dir: Path) -> None:
    if output_dir.exists():
        shutil.rmtree(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    spec_file = openapi_specs_dir / "ledger-api" / "openapi.yaml"
    if not spec_file.exists():
        logger.error(f"Ledger API spec not found at {spec_file}")
        return

    logger.info(f"Generating Ledger API client from {spec_file}")

    venv_bin = Path(sys.executable).parent
    openapi_client_exe = venv_bin / "openapi-python-client"

    if not openapi_client_exe.exists():
        logger.error(f"openapi-python-client not found at {openapi_client_exe}")
        return

    client_output_dir = output_dir / "openapi"

    try:
        subprocess.run(
            [
                str(openapi_client_exe),
                "generate",
                "--path",
                str(spec_file),
                "--output-path",
                str(client_output_dir),
                "--meta",
                "none",
            ],
            check=True,
            capture_output=True,
            text=True,
        )
        logger.info("Successfully generated Ledger API client")

        _add_copyright_headers(client_output_dir)
        logger.info("Added copyright headers to generated files")

        _fix_missing_response_models(output_dir)
        logger.info("Fixed missing response models")

        _format_generated_code(output_dir)
        logger.info("Formatted generated files")
    except subprocess.CalledProcessError as e:
        logger.error(f"Failed to generate client: {e.stderr}")
        return

    init_file = output_dir / "__init__.py"
    init_file.write_text(
        "# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.\n"
        "# SPDX-License-Identifier: Apache-2.0\n"
        "\n"
        "from __future__ import annotations\n"
        "\n"
        "from .openapi.client import AuthenticatedClient, Client\n"
        "\n"
        '__all__ = ["Client", "AuthenticatedClient"]\n'
    )
