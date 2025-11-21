# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from dazl.damlast.daml_lf_1 import PackageRef
from dazl.damlast.parse_factory.pb_parse_base import ProtobufParserBase
from dazl.damlast.pb_parse import ProtobufParserFactory, UnsupportedVersionError
import pytest


class TestProtobufParserFactory:
    """Tests for ProtobufParserFactory class."""

    def test_create_parser_version_1_17(self):
        """Factory creates Parser117 for version 1.17."""
        parser = ProtobufParserFactory.create_parser(PackageRef("test-pkg"), "1.17.0")

        assert isinstance(parser, ProtobufParserBase)
        assert parser.current_package == "test-pkg"
        # Check it's the 117 parser by class name
        assert "117" in parser.__class__.__name__

    def test_create_parser_version_2_x(self):
        """Factory creates Parser117 for version 2.x."""
        parser = ProtobufParserFactory.create_parser(PackageRef("test-pkg"), "2.10.1")
        assert isinstance(parser, ProtobufParserBase)
        assert "117" in parser.__class__.__name__

    def test_create_parser_version_3_x(self):
        """Factory creates Parser21 for version 3.x."""
        parser = ProtobufParserFactory.create_parser(PackageRef("test-pkg"), "3.4.0")

        assert isinstance(parser, ProtobufParserBase)
        assert parser.current_package == "test-pkg"
        # Check it's the 21 parser by class name
        assert "21" in parser.__class__.__name__

    def test_create_parser_version_3_x_dev(self):
        """Factory creates Parser21 for version 3.x.-dev.7773282.33"""
        parser = ProtobufParserFactory.create_parser(
            PackageRef("test-pkg"), "3.4.0-dev.3332dfds21.dd"
        )

        assert isinstance(parser, ProtobufParserBase)
        assert parser.current_package == "test-pkg"
        # Check it's the 21 parser by class name
        assert "21" in parser.__class__.__name__

    def test_create_parser_with_v_prefix(self):
        """Factory handles version strings with 'v' prefix."""
        parser = ProtobufParserFactory.create_parser(PackageRef("test-pkg"), "v3.4.0")
        assert isinstance(parser, ProtobufParserBase)
        assert "21" in parser.__class__.__name__

    def test_unsupported_version_invalid(self):
        """Factory returns default parser (117) for invalid version string."""
        parser = ProtobufParserFactory.create_parser(PackageRef("test-pkg"), "invalid")

        assert isinstance(parser, ProtobufParserBase)
        assert "117" in parser.__class__.__name__

    def test_unsupported_version_none(self):
        """Factory returns default parser (117) for None version."""
        parser = ProtobufParserFactory.create_parser(PackageRef("test-pkg"), None)

        assert isinstance(parser, ProtobufParserBase)
        assert "117" in parser.__class__.__name__

    def test_parser_initialization(self):
        """Created parsers are properly initialized."""
        parser = ProtobufParserFactory.create_parser(PackageRef("test-package-id"), "1.17.0")

        assert parser.current_package == "test-package-id"
        assert parser.current_module is None
        assert parser.interned_strings == []
        assert parser.interned_dotted_names == []
        assert parser.interned_types == []
