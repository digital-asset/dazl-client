# Copyright (c) 2017-2023 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
"""
dazl docs sphinx theme definition.
"""

from pathlib import Path
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from sphinx import Sphinx

SPHINX_ROOT = Path(__file__).parent
ROOT = SPHINX_ROOT.parent


__version__ = (ROOT / 'VERSION').read_text().strip()
__version_full__ = __version__


def get_html_theme_path() -> str:
    return str(SPHINX_ROOT)


def setup(app: 'Sphinx') -> None:
    app.add_html_theme('dazl_sphinx_theme', get_html_theme_path())
