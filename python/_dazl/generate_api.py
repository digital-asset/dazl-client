# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

import logging
from pathlib import Path
import shutil
import subprocess
import sys

logger = logging.getLogger("_dazl.generate_api")

__all__ = ["generate_api_clients"]


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
