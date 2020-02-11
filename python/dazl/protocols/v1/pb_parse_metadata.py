# Copyright (c) 2019 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import sys
import time
from collections import OrderedDict, defaultdict
from typing import Any, Collection, Mapping, Set, Union

from dataclasses import dataclass
from toposort import toposort_flatten

from ... import LOG
from ...damlast.daml_lf_1 import DefDataType, Archive
from ...damlast.types import get_old_type
from ...model.types import TypeReference, RecordType, VariantType, EnumType, SCALAR_TYPE_UNIT, \
    NamedArgumentList, TypeVariable, ModuleRef, TemplateChoice, Template, TypeAdjective, \
    ScalarType, ValueReference
from ...model.types_store import PackageStore, PackageStoreBuilder


def parse_archive_payload(raw_bytes: bytes) -> 'G.ArchivePayload':
    """
    Convert ``bytes`` into a :class:`G.ArchivePayload`.

    Note that this function will temporarily increase Python's recursion limit to handle cases where
    parsing a DAML-LF archive requires deeper recursion limits.
    """
    # noinspection PyPackageRequirements
    from google.protobuf.message import DecodeError
    from . import model as G

    current_time = time.time()

    prev_recursion_limit = sys.getrecursionlimit()
    sys.setrecursionlimit(5000)
    archive_payload = G.ArchivePayload()
    try:
        archive_payload.ParseFromString(raw_bytes)
    except DecodeError:
        # noinspection PyPackageRequirements
        from google.protobuf.internal import api_implementation
        if api_implementation.Type() == 'cpp':
            LOG.error('Failed to decode metadata. This may be due to bugs in the native Protobuf')
            LOG.error('implementation as exposed through Python, so setting an environment')
            LOG.error('variable to force a non-native implementation may help work around this')
            LOG.error('problem:')
            LOG.error('    export PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION=python')
        raise
    finally:
        sys.setrecursionlimit(prev_recursion_limit)

    final_time = time.time()
    total_millis = (final_time - current_time) * 1000
    LOG.info('Parsed %s bytes of metadata in %2.f ms.', len(raw_bytes), total_millis)

    return archive_payload


@dataclass(frozen=True)
class ArchiveDependencyResult:
    sorted_archives: 'Mapping[str, G.ArchivePayload]'
    unresolvable_archives: 'Mapping[str, G.ArchivePayload]'


def find_dependencies(
        metadatas_pb: 'Mapping[str, G.ArchivePayload]', existing_package_ids: 'Collection[str]') \
        -> 'ArchiveDependencyResult':
    """
    Return a topologically-sorted list of dependencies for the package IDs.

    :param metadatas_pb:
        The collection of gRPC ArchivePayload to re-order, indexed by package ID.
    :param existing_package_ids:
        Collection of package IDs that are to be treated as pre-existing.
    :return:
        A topologically-sorted dictionary of package IDs to ArchivePayload objects. Iterations
        through the dictionary are guaranteed to be in the correct order.
    """
    dependencies = defaultdict(set)
    for package_id, archive_payload in metadatas_pb.items():
        for module_pb in archive_payload.daml_lf_1.modules:
            for data_type_pb in module_pb.data_types:
                deps = None
                if data_type_pb.HasField('record'):
                    deps = find_dependencies_of_fwts(data_type_pb.record.fields)
                elif data_type_pb.HasField('variant'):
                    deps = find_dependencies_of_fwts(data_type_pb.variant.fields)
                if deps is not None:
                    deps.difference_update(existing_package_ids)
                    dependencies[package_id].update(deps)

    # identify any completely missing dependencies
    # TODO: This doesn't handle transitive missing dependencies; this will be a problem once
    #  DAML has proper dependency support
    unresolvable_package_ids = []
    for package_id, package_dependencies in dependencies.items():
        if not package_dependencies.issubset(metadatas_pb):
            unresolvable_package_ids.append(package_id)

    m_pb = {}
    sorted_package_ids = toposort_flatten(dependencies)

    # packages with no dependencies or dependents can safely be added in the front
    remainders = set(metadatas_pb) - set(unresolvable_package_ids) - set(sorted_package_ids)
    sorted_package_ids[0:0] = sorted(remainders)

    for package_id in sorted_package_ids:
        if package_id not in unresolvable_package_ids:
            required_package = metadatas_pb.get(package_id)
            if required_package is not None:
                m_pb[package_id] = required_package
            else:
                LOG.warning('Failed to find a package %r', package_id)

    if unresolvable_package_ids:
        # This isn't a major problem in the grand scheme of things because the caller continually
        # retries all unknown packages, so if the missing dependent packages are eventually
        # uploaded, we will end up back in this function and all of the packages will be parsed.
        LOG.warning('Some package IDs could not be resolved, so packages that depend on these IDs '
                    'will be unavailable: %r', unresolvable_package_ids)

    return ArchiveDependencyResult(
        sorted_archives=m_pb,
        unresolvable_archives={pkg_id: metadatas_pb[pkg_id] for pkg_id in unresolvable_package_ids})


def find_dependencies_of_fwts(fwts_pb) -> 'Set[str]':
    dependencies = set()
    for fwt in fwts_pb:
        dependencies.update(find_dependencies_of_fwt(fwt))
    return dependencies


def find_dependencies_of_fwt(fwt_pb) -> 'Collection[str]':
    return find_dependencies_of_type(fwt_pb.type)


def find_dependencies_of_type(type_pb) -> 'Collection[str]':
    t = type_pb.WhichOneof('Sum')  # type: str
    if t == 'prim':
        dependencies = set()  # type: Set[str]
        for arg in type_pb.prim.args:
            dependencies.update(find_dependencies_of_type(arg))
        return sorted(dependencies)
    elif t == 'con':
        dependencies = set()  # type: Set[str]
        if type_pb.con.tycon.module.package_ref.WhichOneof('Sum') == 'package_id':
            dependencies.add(type_pb.con.tycon.module.package_ref.package_id)
        for arg in type_pb.con.args:
            dependencies.update(find_dependencies_of_type(arg))
        return sorted(dependencies)
    elif t == 'var':
        dependencies = set()  # type: Set[str]
        for arg in type_pb.var.args:
            dependencies.update(find_dependencies_of_type(arg))
        return sorted(dependencies)
    elif t == 'fun':
        dependencies = set()  # type: Set[str]
        for arg in type_pb.fun.params:
            dependencies.update(find_dependencies_of_type(arg))
        dependencies.update(find_dependencies_of_type(type_pb.fun.result))
        return dependencies
    elif t == 'forall':
        return find_dependencies_of_type(type_pb.forall.body)
    elif t == 'tuple':
        return find_dependencies_of_fwts(type_pb.tuple.fields)
    elif t == 'nat':
        return ()
    else:
        LOG.warning('Unknown DAML-LF Type: %s (when evaluating %s)', t, type_pb)
        return ()


def parse_daml_metadata_pb(package_id: str, metadata_pb: Any) -> 'PackageStore':
    """
    Parse the contents of the given DAML-LF archive.

    :param package_id:
        The package to associate "self"-modules to.
    :param metadata_pb:
        The Protobuf-generated Archive object.
    :return:
        A :class:`PackageStore` with additional entries resulting from the parse of this archive.
    """
    from ...damlast.pb_parse import ProtobufParser

    parser = ProtobufParser(package_id)
    package = parser.parse_Package(metadata_pb.daml_lf_1)

    psb = PackageStoreBuilder()
    psb.add_archive(Archive(package_id, package))

    for module in package.modules:
        current_module = ModuleRef(package_id, module.name.segments)
        for vv in module.values:
            vt = ValueReference(current_module, vv.name_with_type.name)
            psb.add_value(vt, vv.expr)

        for dt in module.data_types:
            tt = create_data_type(current_module, dt)
            if isinstance(tt, (RecordType, VariantType, EnumType)):
                psb.add_type(tt.name, tt)
            else:
                LOG.warning('Unexpected non-complex type will be ignored: %r', tt)

        for template_pb in module.templates:
            tt = TypeReference(current_module, template_pb.tycon.segments)
            data_type = psb.get_type(tt)
            if isinstance(data_type, RecordType):
                psb.add_template(Template(
                    data_type=data_type,
                    key_type=get_old_type(template_pb.key.type) if template_pb.key is not None else None,
                    choices=[
                        TemplateChoice(
                            c.name,
                            c.consuming,
                            get_old_type(c.arg_binder.type),
                            get_old_type(c.ret_type),
                            c.controllers)
                        for c in template_pb.choices],
                    observers=template_pb.observers,
                    signatories=template_pb.signatories,
                    agreement=template_pb.agreement,
                    ensure=template_pb.precond))
            elif data_type is None:
                LOG.warning('The template %s did not have a corresponding data definition; '
                            'it will be ignored', tt)
            else:
                LOG.warning(
                    'The template %s was of type %s; only records are supported for templates',
                    tt, data_type)

    LOG.debug('Fully registered all types for package ID %r', package_id)
    return psb.build()


def create_data_type(current_module_ref: 'ModuleRef', dt: 'DefDataType') \
        -> 'Union[RecordType, VariantType, EnumType, ScalarType]':
    from ...damlast.types import get_old_type

    type_vars = tuple(TypeVariable(type_var.var) for type_var in dt.params)
    tt = TypeReference(current_module_ref, tuple(dt.name.segments))

    if dt.record is not None:
        d = OrderedDict()
        for fwt in dt.record.fields:
            d[fwt.field] = get_old_type(fwt.type)
        return RecordType(NamedArgumentList(d.items()), tt, type_vars, TypeAdjective.USER_DEFINED)
    elif dt.variant is not None:
        d = OrderedDict()
        for fwt in dt.variant.fields:
            d[fwt.field] = get_old_type(fwt.type)
        return VariantType(NamedArgumentList(d.items()), tt, type_vars, TypeAdjective.USER_DEFINED)
    elif dt.enum is not None:
        return EnumType(tt, dt.enum.constructors)
    else:
        return SCALAR_TYPE_UNIT
