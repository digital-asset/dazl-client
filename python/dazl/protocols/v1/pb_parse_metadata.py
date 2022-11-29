# Copyright (c) 2017-2022 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from collections import OrderedDict, defaultdict
from dataclasses import dataclass
from typing import (
    TYPE_CHECKING,
    AbstractSet,
    Any,
    Collection,
    DefaultDict,
    List,
    Mapping,
    Optional,
    Set,
    Union,
)
import warnings

from toposort import toposort_flatten

from ... import LOG
from ..._gen.com.daml.daml_lf_1_15 import daml_lf_pb2 as lfpb
from ...damlast.daml_lf_1 import (
    Archive,
    DefDataType,
    DottedName,
    ModuleRef,
    PackageRef,
    TypeConName,
    ValName,
)

with warnings.catch_warnings():
    warnings.simplefilter("ignore", DeprecationWarning)
    from ...damlast.types import get_old_type

    if TYPE_CHECKING:
        from ...model.types import EnumType, RecordType, ScalarType, VariantType
        from ...model.types_store import PackageStore

__all__ = [
    "parse_archive_payload",
    "ArchiveDependencyResult",
    "find_dependencies",
    "parse_daml_metadata_pb",
]

warnings.warn(
    "The symbols in dazl.protocols.v1.pb_parse_metadata are deprecated",
    DeprecationWarning,
    stacklevel=2,
)


def parse_archive_payload(raw_bytes: bytes, package_id: "Optional[PackageRef]" = None):
    """
    Convert ``bytes`` into a :class:`G_ArchivePayload`.

    Note that this function will temporarily increase Python's recursion limit to handle cases where
    parsing a DAML-LF archive requires deeper recursion limits.
    """
    warnings.warn(
        "Use dazl.damlast.parse.parse_archive_payload instead.", DeprecationWarning, stacklevel=2
    )

    from ...damlast.parse import parse_archive_payload as pav

    return pav(package_id, raw_bytes)


@dataclass(frozen=True)
class ArchiveDependencyResult:
    sorted_archives: "Mapping[PackageRef, lfpb.ArchivePayload]"
    unresolvable_archives: "Mapping[PackageRef, lfpb.ArchivePayload]"


# noinspection PyDeprecation
def find_dependencies(
    metadatas_pb: "Mapping[PackageRef, lfpb.ArchivePayload]",
    existing_package_ids: "Collection[PackageRef]",
) -> "ArchiveDependencyResult":
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
    warnings.warn(
        "find_dependencies is deprecated; there is no replacement.",
        DeprecationWarning,
        stacklevel=2,
    )

    dependencies = defaultdict(set)  # type: DefaultDict[PackageRef, Set[PackageRef]]
    for package_id, archive_payload in metadatas_pb.items():
        for module_pb in archive_payload.daml_lf_1.modules:
            for data_type_pb in module_pb.data_types:
                deps = None
                if data_type_pb.HasField("record"):
                    deps = find_dependencies_of_fwts(data_type_pb.record.fields)
                elif data_type_pb.HasField("variant"):
                    deps = find_dependencies_of_fwts(data_type_pb.variant.fields)
                if deps is not None:
                    deps = set(deps)
                    deps.difference_update(existing_package_ids)
                    dependencies[package_id].update(deps)

    # identify any completely missing dependencies
    # TODO: This doesn't handle transitive missing dependencies; this will be a problem once
    #  DAML has proper dependency support
    unresolvable_package_ids = []  # type: List[PackageRef]
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
                LOG.warning("Failed to find a package %r", package_id)

    if unresolvable_package_ids:
        # This isn't a major problem in the grand scheme of things because the caller continually
        # retries all unknown packages, so if the missing dependent packages are eventually
        # uploaded, we will end up back in this function and all of the packages will be parsed.
        LOG.warning(
            "Some package IDs could not be resolved, so packages that depend on these IDs "
            "will be unavailable: %r",
            unresolvable_package_ids,
        )

    return ArchiveDependencyResult(
        sorted_archives=m_pb,
        unresolvable_archives={pkg_id: metadatas_pb[pkg_id] for pkg_id in unresolvable_package_ids},
    )


# noinspection PyDeprecation
def find_dependencies_of_fwts(fwts_pb) -> "AbstractSet[PackageRef]":
    warnings.warn(
        "find_dependencies_of_fwts is deprecated; there is no replacement.",
        DeprecationWarning,
        stacklevel=2,
    )

    with warnings.catch_warnings():
        warnings.simplefilter("ignore", DeprecationWarning)

        dependencies = set()  # type: Set[PackageRef]
        for fwt in fwts_pb:
            dependencies.update(find_dependencies_of_fwt(fwt))
        return dependencies


# noinspection PyDeprecation
def find_dependencies_of_fwt(fwt_pb) -> "Collection[PackageRef]":
    warnings.warn(
        "find_dependencies_of_fwt is deprecated; there is no replacement.",
        DeprecationWarning,
        stacklevel=2,
    )

    with warnings.catch_warnings():
        warnings.simplefilter("ignore", DeprecationWarning)

        return find_dependencies_of_type(fwt_pb.type)


# noinspection PyDeprecation
def find_dependencies_of_type(type_pb) -> "Collection[PackageRef]":
    warnings.warn(
        "find_dependencies_of_type is deprecated; there is no replacement.",
        DeprecationWarning,
        stacklevel=2,
    )

    with warnings.catch_warnings():
        warnings.simplefilter("ignore", DeprecationWarning)

        dependencies = set()  # type: Set[PackageRef]
        t = type_pb.WhichOneof("Sum")  # type: str
        if t == "prim":
            for arg in type_pb.prim.args:
                dependencies.update(find_dependencies_of_type(arg))
            return sorted(dependencies)
        elif t == "con":
            if type_pb.con.tycon.module.package_ref.WhichOneof("Sum") == "package_id":
                dependencies.add(type_pb.con.tycon.module.package_ref.package_id)
            for arg in type_pb.con.args:
                dependencies.update(find_dependencies_of_type(arg))
            return sorted(dependencies)
        elif t == "var":
            for arg in type_pb.var.args:
                dependencies.update(find_dependencies_of_type(arg))
            return sorted(dependencies)
        elif t == "fun":
            for arg in type_pb.fun.params:
                dependencies.update(find_dependencies_of_type(arg))
            dependencies.update(find_dependencies_of_type(type_pb.fun.result))
            return dependencies
        elif t == "forall":
            return find_dependencies_of_type(type_pb.forall.body)
        elif t == "tuple":
            return find_dependencies_of_fwts(type_pb.tuple.fields)
        elif t == "nat":
            return ()
        elif t == "interned":
            # This isn't strictly correct, but we're catching this here to suppress errors
            # ahead of removal of this deprecated function
            return ()
        else:
            LOG.warning("Unknown DAML-LF Type: %s (when evaluating %s)", t, type_pb)
            return ()


def parse_daml_metadata_pb(package_id: "PackageRef", metadata_pb: Any) -> "PackageStore":
    """
    Parse the contents of the given DAML-LF archive.

    :param package_id:
        The package to associate "self"-modules to.
    :param metadata_pb:
        The Protobuf-generated Archive object.
    :return:
        A :class:`PackageStore` with additional entries resulting from the parse of this archive.
    """
    warnings.warn(
        "parse_daml_metadata_pb and PackageStore are deprecated; "
        "use dazl.damlast.parse_archive instead",
        DeprecationWarning,
        stacklevel=2,
    )

    LOG.debug("Parsing package ID: %r", package_id)

    from ...damlast.pb_parse import ProtobufParser

    parser = ProtobufParser(package_id)
    package = parser.parse_Package(metadata_pb.daml_lf_1)

    return _parse_daml_metadata_pb(Archive(package_id, package))


# noinspection PyDeprecation
def _parse_daml_metadata_pb(archive: "Archive") -> "PackageStore":
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", DeprecationWarning)
        from ...model.types import EnumType, RecordType, Template, TemplateChoice, VariantType
        from ...model.types_store import PackageStoreBuilder

        psb = PackageStoreBuilder()
        psb.add_archive(archive)

        for module in archive.package.modules:
            current_module = ModuleRef(archive.hash, DottedName(module.name.segments))
            for vv in module.values:
                vt = ValName(current_module, vv.name_with_type.name)
                psb.add_value(vt, vv.expr)

            for dt in module.data_types:
                tt = create_data_type(current_module, dt)
                if isinstance(tt, (RecordType, VariantType, EnumType)) and tt.name is not None:
                    psb.add_type(tt.name.con, tt)
                else:
                    LOG.warning("Unexpected non-complex type will be ignored: %r", tt)

            for template_pb in module.templates:
                con = TypeConName(current_module, template_pb.tycon.segments)
                data_type = psb.get_type(con)
                if isinstance(data_type, RecordType):
                    psb.add_template(
                        Template(
                            data_type=data_type,
                            key_type=get_old_type(template_pb.key.type)
                            if template_pb.key is not None
                            else None,
                            choices=[
                                TemplateChoice(
                                    c.name,
                                    c.consuming,
                                    get_old_type(c.arg_binder.type),
                                    get_old_type(c.ret_type),
                                    c.controllers,
                                )
                                for c in template_pb.choices
                            ],
                            observers=template_pb.observers,
                            signatories=template_pb.signatories,
                            agreement=template_pb.agreement,
                            ensure=template_pb.precond,
                        )
                    )
                elif data_type is None:
                    LOG.warning(
                        "The template %s did not have a corresponding data definition; "
                        "it will be ignored",
                        con,
                    )
                else:
                    LOG.warning(
                        "The template %s was of type %s; only records are supported for templates",
                        con,
                        data_type,
                    )

        LOG.debug("Fully registered all types for package ID %r", archive.hash)
        return psb.build()


# noinspection PyDeprecation
def create_data_type(
    current_module_ref: "ModuleRef", dt: "DefDataType"
) -> "Union[RecordType, VariantType, EnumType, ScalarType]":
    warnings.warn(
        "create_data_type is deprecated; there is no replacement.", DeprecationWarning, stacklevel=2
    )
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", DeprecationWarning)
        from ...damlast.types import get_old_type
        from ...model.types import (
            SCALAR_TYPE_UNIT,
            EnumType,
            NamedArgumentList,
            RecordType,
            TypeReference,
            TypeVariable,
            VariantType,
        )

        type_vars = tuple(TypeVariable(type_var.var) for type_var in dt.params)
        tt = TypeReference(con=TypeConName(current_module_ref, dt.name.segments))

        if dt.record is not None:
            d = OrderedDict()
            for fwt in dt.record.fields:
                d[fwt.field] = get_old_type(fwt.type)
            return RecordType(NamedArgumentList(d.items()), tt, type_vars)
        elif dt.variant is not None:
            d = OrderedDict()
            for fwt in dt.variant.fields:
                d[fwt.field] = get_old_type(fwt.type)
            return VariantType(NamedArgumentList(d.items()), tt, type_vars)
        elif dt.enum is not None:
            return EnumType(tt, dt.enum.constructors)
        else:
            return SCALAR_TYPE_UNIT
