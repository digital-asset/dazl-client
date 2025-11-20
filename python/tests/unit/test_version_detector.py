# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from dazl.util.version import SdkVersion
import pytest


class TestSdkVersion:
    """Tests for SdkVersion helper class."""

    def test_parse_version_simple(self):
        """Parses simple version strings correctly."""
        version = SdkVersion.parse("1.17.0")
        assert version is not None
        assert version.major == 1
        assert version.minor == 17
        assert version.patch == 0

    def test_parse_version_with_v_prefix(self):
        """Parses version with 'v' prefix."""
        version = SdkVersion.parse("v2.1.0")
        assert version is not None
        assert version.major == 2
        assert version.minor == 1
        assert version.patch == 0

    def test_parse_version_three_parts(self):
        """Parses three-part version correctly."""
        version = SdkVersion.parse("3.4.5")
        assert version is not None
        assert version.major == 3
        assert version.minor == 4
        assert version.patch == 5

    def test_parse_version_three_parts_with_dash(self):
        """Parses three-part version correctly."""
        version = SdkVersion.parse("3.4.2-dev.jjdks93.dd")
        assert version is not None
        assert version.major == 3
        assert version.minor == 4
        assert version.patch == 2

    def test_parse_version_two_parts(self):
        """Handles two-part version (adds .0 for patch)."""
        version = SdkVersion.parse("2.10")
        assert version is not None
        assert version.major == 2
        assert version.minor == 10
        assert version.patch == 0

    def test_parse_version_none(self):
        """Returns None for None input."""
        version = SdkVersion.parse(None)
        assert version is None

    def test_parse_version_invalid(self):
        """Returns None for invalid version strings."""
        assert SdkVersion.parse("invalid") is None
        assert SdkVersion.parse("a.b.c") is None
        assert SdkVersion.parse("") is None

    def test_parse_version_with_whitespace(self):
        """Handles whitespace in version string."""
        version = SdkVersion.parse("  2.10.1  ")
        assert version is not None
        assert version.major == 2
        assert version.minor == 10
        assert version.patch == 1
