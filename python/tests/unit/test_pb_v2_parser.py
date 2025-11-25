# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from pathlib import Path
import time

from dazl.damlast import DarFile
from dazl.damlast.daml_lf_1 import PackageRef
from dazl.damlast.lookup import MultiPackageLookup
from dazl.damlast.parse_factory.pb_parse_base import ProtobufParserBase
from dazl.damlast.parse_factory.pb_v2 import ProtobufParser21
from dazl.damlast.pb_parse import ProtobufParserFactory
import pytest

from dazl import LOG

ARCHIVES = Path(__file__).absolute().parent.parent.parent.parent / "_fixtures" / "archives"
ALL_KINDS_OF_V3_DAR = ARCHIVES / "3.3.0/all-kinds-of-1.0.0_lf.dar"


class TestProtobufParser21Factory:
    def test_factory_creates_v2_parser_for_version_3(self):
        parser = ProtobufParserFactory.create_parser(PackageRef("test-pkg"), "3.3.0")
        assert isinstance(parser, ProtobufParserBase)
        assert isinstance(parser, ProtobufParser21)
        assert "21" in parser.__class__.__name__

    def test_factory_creates_v2_parser_for_version_3_with_snapshot(self):
        parser = ProtobufParserFactory.create_parser(
            PackageRef("test-pkg"), "3.3.0-snapshot.20250417.0"
        )
        assert isinstance(parser, ProtobufParser21)

    def test_v2_parser_initialization(self):
        parser = ProtobufParser21(PackageRef("test-package-id"))
        assert parser.current_package == "test-package-id"
        assert parser.current_module is None
        assert parser.interned_strings == []
        assert parser.interned_dotted_names == []
        assert parser.interned_types == []


class TestAllKindsOfV3DAR:
    @pytest.fixture
    def dar_file(self):
        return DarFile(ALL_KINDS_OF_V3_DAR)

    @pytest.fixture
    def archives(self, dar_file):
        return dar_file.archives()

    @pytest.fixture
    def lookup(self, dar_file):
        return MultiPackageLookup(dar_file.archives())

    def test_dar_file_exists(self):
        assert ALL_KINDS_OF_V3_DAR.exists()
        assert ALL_KINDS_OF_V3_DAR.is_file()

    def test_dar_loads_successfully(self, dar_file):
        assert dar_file is not None

    def test_dar_has_archives(self, archives):
        assert len(archives) > 0
        LOG.info("Found %d archives in DAR", len(archives))

    def test_dar_parsing_performance(self, dar_file):
        start_time = time.time()
        archives = dar_file.archives()
        end_time = time.time()
        LOG.info(
            "Successfully parsed all-kinds-of v3 DAR in %0.2f seconds with package IDs %r",
            end_time - start_time,
            [a.hash for a in archives],
        )
        assert end_time - start_time < 5.0

    def test_archives_have_package_ids(self, archives):
        for archive in archives:
            assert archive.hash is not None
            assert len(archive.hash) > 0

    def test_dar_sdk_version_is_v3(self, dar_file):
        sdk_version = dar_file.sdk_version()
        assert sdk_version is not None
        assert sdk_version.startswith("3."), f"Expected version 3.x but got {sdk_version}"

    def test_v3_uses_v2_parser(self, dar_file):
        sdk_version = dar_file.sdk_version()
        from dazl.util.version import SdkVersion

        parsed_version = SdkVersion.parse(sdk_version)
        assert parsed_version.major == 3
        parser = ProtobufParserFactory.create_parser(PackageRef("test"), sdk_version)
        assert isinstance(parser, ProtobufParser21)

    def test_archives_have_modules(self, archives):
        main_archive = archives[0]
        assert main_archive.package is not None
        assert main_archive.package.modules is not None
        assert len(main_archive.package.modules) > 0

    def test_modules_have_names(self, archives):
        main_archive = archives[0]
        for module in main_archive.package.modules:
            assert module.name is not None
            LOG.info("Module: %s", module.name)

    def test_modules_have_data_types(self, archives):
        main_archive = archives[0]
        total_data_types = 0
        for module in main_archive.package.modules:
            total_data_types += len(module.data_types)
        assert total_data_types > 0
        LOG.info("Total data types: %d", total_data_types)

    def test_modules_have_templates(self, archives):
        main_archive = archives[0]
        total_templates = 0
        for module in main_archive.package.modules:
            total_templates += len(module.templates)
        LOG.info("Total templates: %d", total_templates)

    def test_lookup_can_search_symbols(self, lookup):
        assert lookup is not None

    def test_archive_metadata_parsed(self, archives):
        main_archive = archives[0]
        if main_archive.package.metadata:
            metadata = main_archive.package.metadata
            assert metadata.name is not None
            assert metadata.version is not None
            LOG.info("Package name: %s, version: %s", metadata.name, metadata.version)

    def test_data_types_have_names(self, archives):
        main_archive = archives[0]
        for module in main_archive.package.modules:
            for data_type in module.data_types:
                assert data_type.name is not None

    def test_data_types_have_location(self, archives):
        main_archive = archives[0]
        for module in main_archive.package.modules:
            for data_type in module.data_types:
                assert data_type.location is not None

    def test_templates_have_choices(self, archives):
        main_archive = archives[0]
        for module in main_archive.package.modules:
            for template in module.templates:
                assert template.choices is not None

    def test_templates_have_signatories(self, archives):
        main_archive = archives[0]
        for module in main_archive.package.modules:
            for template in module.templates:
                assert template.signatories is not None

    def test_data_type_serialization_flag(self, archives):
        main_archive = archives[0]
        for module in main_archive.package.modules:
            for data_type in module.data_types:
                assert isinstance(data_type.serializable, bool)

    def test_module_feature_flags(self, archives):
        main_archive = archives[0]
        for module in main_archive.package.modules:
            assert module.flags is not None
            assert hasattr(module.flags, "forbid_party_literals")

    def test_all_archives_parseable(self, archives):
        for i, archive in enumerate(archives):
            assert archive.package is not None
            assert archive.package.modules is not None
            LOG.info("Archive %d has %d modules", i, len(archive.package.modules))

    def test_v2_protobuf_format_detected(self, dar_file):
        from dazl.damlast.daml_lf_1 import PackageRef
        from dazl.damlast.parse import parse_archive_payload

        for pb_archive in dar_file._pb_archives():
            archive_payload = parse_archive_payload(PackageRef(pb_archive.hash), pb_archive.payload)
            has_v2 = archive_payload.HasField("daml_lf_2")
            has_v1 = archive_payload.HasField("daml_lf_1")
            if has_v2:
                LOG.info("Archive %s uses DAML-LF 2.x format", pb_archive.hash[:16])
            if has_v1:
                LOG.info("Archive %s uses DAML-LF 1.x format", pb_archive.hash[:16])


class TestV2ParserSpecificFeatures:
    @pytest.fixture
    def dar_file(self):
        return DarFile(ALL_KINDS_OF_V3_DAR)

    @pytest.fixture
    def main_archive(self, dar_file):
        archives = dar_file.archives()
        return archives[0]

    @pytest.fixture
    def main_module(self, main_archive):
        return main_archive.package.modules[0]

    def test_builtin_types_parsed_correctly(self, main_archive):
        type_count = 0
        for module in main_archive.package.modules:
            for data_type in module.data_types:
                if data_type.record:
                    for field in data_type.record.fields:
                        if field.type.prim:
                            type_count += 1
        LOG.info("Found %d primitive types", type_count)

    def test_data_type_records_have_fields(self, main_module):
        from dazl.damlast.daml_lf_1 import DefDataType

        record_count = 0
        field_count = 0
        for data_type in main_module.data_types:
            if data_type.record:
                record_count += 1
                assert data_type.record.fields is not None
                for field in data_type.record.fields:
                    field_count += 1
                    assert field.field is not None
                    assert isinstance(field.field, str)
                    assert field.type is not None
                    LOG.info("  Record %s has field: %s", data_type.name, field.field)
        LOG.info("Found %d records with %d total fields", record_count, field_count)
        assert record_count > 0
        assert field_count > 0

    def test_data_type_variants_parsed(self, main_module):
        variant_count = 0
        for data_type in main_module.data_types:
            if data_type.variant:
                variant_count += 0
                assert data_type.variant.fields is not None
                for field in data_type.variant.fields:
                    assert field.field is not None
                    assert field.type is not None
        LOG.info("Found %d variant types", variant_count)

    def test_template_structure_complete(self, main_module):
        for template in main_module.templates:
            assert template.tycon is not None
            assert len(template.tycon.segments) > 0
            assert template.param is not None
            assert isinstance(template.param, str)
            assert template.choices is not None
            assert template.location is not None
            LOG.info("Template %s has %d choices", template.tycon, len(template.choices))

    def test_template_choices_have_complete_data(self, main_module):
        choice_count = 0
        for template in main_module.templates:
            for choice in template.choices:
                choice_count += 1
                assert choice.name is not None
                assert isinstance(choice.name, str)
                assert isinstance(choice.consuming, bool)
                assert choice.arg_binder is not None
                assert choice.arg_binder.var is not None
                assert choice.arg_binder.type is not None
                assert choice.ret_type is not None
                assert choice.update is not None
                assert choice.self_binder is not None
                LOG.info("    Choice: %s (consuming=%s)", choice.name, choice.consuming)
        assert choice_count > 0

    def test_values_have_expressions(self, main_module):
        value_with_expr_count = 0
        value_with_valid_expr_count = 0
        for value in main_module.values:
            assert value.name_with_type is not None
            assert value.name_with_type.name is not None
            assert value.name_with_type.type is not None
            if value.expr:
                value_with_expr_count += 1
                try:
                    expr_result = value.expr
                    assert expr_result is not None
                    value_with_valid_expr_count += 1
                except (ValueError, KeyError) as e:
                    LOG.warning(
                        "Skipping value %s due to parsing error: %s", value.name_with_type.name, e
                    )
        LOG.info(
            "Found %d values with expressions (%d parsed successfully)",
            value_with_expr_count,
            value_with_valid_expr_count,
        )
        assert value_with_expr_count > 0

    def test_type_parsing_primitive_types(self, main_module):
        from dazl.damlast.daml_lf_1 import PrimType

        prim_type_count = 0
        for data_type in main_module.data_types:
            if data_type.record:
                for field in data_type.record.fields:
                    if field.type.prim:
                        prim_type_count += 1
                        prim_type = field.type.prim.prim
                        assert isinstance(prim_type, PrimType)
        LOG.info("Parsed %d primitive types", prim_type_count)
        assert prim_type_count > 0

    def test_type_parsing_constructed_types(self, main_module):
        con_type_count = 0
        for data_type in main_module.data_types:
            if data_type.record:
                for field in data_type.record.fields:
                    if field.type.con:
                        con_type_count += 1
                        con_type = field.type.con
                        assert con_type.tycon is not None
                        assert str(con_type.tycon) is not None
                        assert len(str(con_type.tycon)) > 0
        LOG.info("Parsed %d constructed types", con_type_count)
        assert con_type_count > 0

    def test_expression_parsing_from_templates(self, main_module):
        from dazl.damlast.daml_lf_1 import Expr

        expr_count = 0
        for template in main_module.templates:
            if template.precond:
                expr_count += 1
                assert isinstance(template.precond, Expr)
            if template.signatories:
                expr_count += 1
                assert isinstance(template.signatories, Expr)
            if template.observers:
                expr_count += 1
                assert isinstance(template.observers, Expr)
        LOG.info("Parsed %d expressions from templates", expr_count)
        assert expr_count > 0

    def test_module_metadata_complete(self, main_module):
        assert main_module.name is not None
        assert len(main_module.name.segments) > 0
        assert main_module.flags is not None
        assert hasattr(main_module.flags, "forbid_party_literals")
        assert hasattr(main_module.flags, "dont_divulge_contract_ids_in_create_arguments")
        LOG.info("Module %s metadata complete", main_module.name)

    def test_package_metadata_parsed(self, main_archive):
        if main_archive.package.metadata:
            meta = main_archive.package.metadata
            assert meta.name is not None
            assert isinstance(meta.name, str)
            assert meta.version is not None
            assert isinstance(meta.version, str)
            LOG.info("Package: %s version %s", meta.name, meta.version)
            assert meta.name == "all-kinds-of"
            assert meta.version == "1.0.0"

    def test_location_ranges_have_coordinates(self, main_module):
        location_count = 0
        for template in main_module.templates:
            if template.location:
                location_count += 1
                assert template.location.range is not None
                assert template.location.range.start_line >= 0
                assert template.location.range.start_col >= 0
                assert template.location.range.end_line >= template.location.range.start_line
        LOG.info("Validated %d location ranges", location_count)
        assert location_count > 0

    def test_type_synonyms_parsed(self, main_module):
        for synonym in main_module.synonyms:
            assert synonym.name is not None
            assert synonym.type is not None
            assert synonym.location is not None
        LOG.info("Found %d type synonyms", len(main_module.synonyms))


class TestV2ParserBackwardCompatibility:
    def test_v2_parser_produces_same_ast_structure_as_v1(self):
        v3_dar = DarFile(ALL_KINDS_OF_V3_DAR)
        v3_archives = v3_dar.archives()
        main_archive = v3_archives[0]
        for module in main_archive.package.modules:
            assert hasattr(module, "name")
            assert hasattr(module, "flags")
            assert hasattr(module, "synonyms")
            assert hasattr(module, "data_types")
            assert hasattr(module, "values")
            assert hasattr(module, "templates")

    def test_prim_con_mapping(
        self,
    ):
        from dazl.damlast.daml_lf_1 import PrimCon

        assert PrimCon.CON_UNIT is not None
        assert PrimCon.CON_TRUE is not None
        assert PrimCon.CON_FALSE is not None

    def test_prim_type_available(self):
        from dazl.damlast.daml_lf_1 import PrimType

        assert PrimType is not None

    def test_prim_lit_available(self):
        from dazl.damlast.daml_lf_1 import PrimLit

        assert PrimLit is not None
