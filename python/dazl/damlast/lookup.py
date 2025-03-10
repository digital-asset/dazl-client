# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""
DAML-LF fast lookups
--------------------
"""

from __future__ import annotations

# Implementation notes:
#
# The code in here is fairly monotonous and boilerplate heavy. However, being too creative here can
# potentially lead to performance degradations, particularly at application startup where type and
# template lookups by name are very frequent. Please be conscious of the runtime costs of
# modifications in this file!
import threading
from types import MappingProxyType
from typing import (
    AbstractSet,
    Any,
    Collection,
    Iterable,
    NoReturn,
    Optional,
    Sequence,
    Tuple,
    Union,
)
import warnings

from .. import LOG
from .daml_lf_1 import (
    Archive,
    DefDataType,
    DefInterface,
    DefTemplate,
    DefValue,
    DottedName,
    ModuleRef,
    Package,
    PackageRef,
    TemplateChoice,
    TypeConName,
    ValName,
)
from .errors import NameNotFoundError, PackageNotFoundError
from .protocols import SymbolLookup, TemplateOrInterface
from .util import package_local_name, package_ref

__all__ = [
    "STAR",
    "EmptyLookup",
    "MultiPackageLookup",
    "PackageLookup",
    "PackageExceptionTracker",
    "SymbolLookup",
    "find_choice",
    "matching_normalizations",
    "normalize",
    "parse_type_con_name",
    "validate_template",
]

STAR = PackageRef("*")


def parse_type_con_name(val: str, /) -> TypeConName:
    """
    Parse the given string as a type constructor.
    """
    pkg, name = validate_template(val)
    module_name, _, entity_name = name.rpartition(":")
    if module_name:
        module_ref = ModuleRef(pkg, DottedName(module_name.split(".")))
    else:
        module_ref = ModuleRef(pkg, DottedName())
    return TypeConName(module_ref, entity_name.split("."))


def empty_lookup_impl(ref: Any, /) -> NoReturn:
    pkg, _ = validate_template(ref)
    if pkg != STAR:
        raise PackageNotFoundError(pkg)
    else:
        raise NameNotFoundError(ref)


def validate_template(template: Any, /) -> Tuple[PackageRef, str]:
    """
    Return a module and type name component from something that can be interpreted as a template.

    :param template:
        Any object that can be interpreted as an identifier for a template.
    :return:
        A tuple of package ID and ``Module.Name:EntityName`` (the package-scoped identifier for the
        type). The special value ``'*'`` is used if either the package ID, module name, or both
        should be wildcarded.
    :raise ValueError:
        If the object could not be interpreted as a thing referring to a template.
    """
    if template == "*" or template is None:
        return STAR, "*"

    if isinstance(template, str):
        components = template.split(":")
        if len(components) == 3:
            # correct number of colons for a fully-qualified name
            pkgid, m, e = components
            return PackageRef(pkgid), f"{m}:{e}"

        elif len(components) == 2:
            # one colon, so assume the package ID is unspecified UNLESS the second component is a
            # wildcard; then we assume the wildcard means any module name and entity name
            m, e = components
            if m == STAR and e != STAR:
                # strings that look like "*:SOMETHING" are explicitly not allowed unless deprecated
                # identifier support is requested; this is almost certainly an attempt to use
                # periods instead of colons as a delimiter between module name and entity name
                raise ValueError("string must be in the format PKG_REF:MOD:ENTITY or MOD:ENTITY")

            return (STAR, f"{m}:{e}") if e != "*" else (PackageRef(m), "*")

        else:
            raise ValueError("string must be in the format PKG_REF:MOD:ENTITY or MOD:ENTITY")

    if isinstance(template, TypeConName):
        return package_ref(template), package_local_name(template)
    else:
        raise ValueError(f"Don't know how to convert {template!r} into a template")


def normalize(name: Union[None, str, TypeConName], /) -> str:
    """
    Return the canonical form for a string that represents a template ID or partial match of a
    template ID.

    Concretely, this function converts ``"MyMod:MyTemplate"`` to ``"*:MyMod:MyTemplate"`` and leaves
    most other strings unchanged.

    :param name:
        A template ID, expressed in either string form or as an instance of :class:`TypeConName`.
    :return:
        A string in canonical form (either ``PACKAGE_REF:MODULE_NAME:ENTITY_NAME`` or
        ``PACKAGE_REF:*``, where ``PACKAGE_REF`` is also allowed to be ``*``).
    """
    p, m = validate_template(name)
    return f"{p}:{m}"


def matching_normalizations(name: Union[str, TypeConName], /) -> Sequence[str]:
    """
    Return strings that are possible matches for the given template ID.
    """
    p, m = validate_template(name)

    # throw away duplicates that arise from `name` not being fully specified (p and/or m are
    # allowed to be asterisks too)
    return list(dict.fromkeys([f"{p}:{m}", f"{p}:*", f"*:{m}", "*:*"]))


class EmptyLookup(SymbolLookup):
    """
    A :class:`SymbolLookup` that trivially throws for all of its functions.

    This can be used where a :class:`SymbolLookup` instance is useful but an implementation is not
    required.

    All methods are implemented such that if the provided ref has a package ID,
    :class:`PackageNotFoundError` is thrown; otherwise, :class:`NameNotFoundError` is thrown.
    """

    __slots__ = ()

    def archives(self) -> Collection[Archive]:
        return frozenset()

    def package_ids(self) -> AbstractSet[PackageRef]:
        return frozenset()

    def data_type_name(self, ref: Any) -> NoReturn:
        raise empty_lookup_impl(ref)

    def data_type(self, ref: Any) -> NoReturn:
        raise empty_lookup_impl(ref)

    def value(self, ref: Any) -> NoReturn:
        raise empty_lookup_impl(ref)

    def template_names(self, ref: Any) -> Collection[TypeConName]:
        return frozenset()

    def template_name(self, ref: Any) -> NoReturn:
        raise empty_lookup_impl(ref)

    def template(self, ref: Any) -> NoReturn:
        raise empty_lookup_impl(ref)

    def interface_names(self, ref: Any) -> Collection[TypeConName]:
        return frozenset()

    def interface_name(self, ref: Any) -> NoReturn:
        raise empty_lookup_impl(ref)

    def interface(self, ref: Any) -> NoReturn:
        raise empty_lookup_impl(ref)

    def template_or_interface_names(self, ref: Any) -> Collection[TypeConName]:
        return frozenset()

    def template_or_interface_name(self, ref: Any) -> NoReturn:
        raise empty_lookup_impl(ref)

    def template_or_interface(self, ref: Any) -> NoReturn:
        raise empty_lookup_impl(ref)


class PackageLookup(SymbolLookup):
    """
    Caching structure to make lookups on type names within a :class:`Package` faster.
    """

    def __init__(self, archive: Archive):
        self.archive = archive

        data_types = dict[str, Tuple[TypeConName, DefDataType]]()
        values = dict[str, Tuple[ValName, DefValue]]()
        templates = dict[str, Tuple[TypeConName, DefTemplate]]()
        interfaces = dict[str, Tuple[TypeConName, DefInterface]]()
        for module in self.archive.package.modules:
            module_ref = ModuleRef(archive.hash, module.name)

            for dt in module.data_types:
                dt_name = TypeConName(module_ref, dt.name.segments)
                data_types[f"{module.name}:{dt.name}"] = (dt_name, dt)

            for value in module.values:
                value_name = ValName(module_ref, value.name_with_type.name)
                values[f"{module.name}:{value.name_with_type.name}"] = (value_name, value)

            for tmpl in module.templates:
                tmpl_name = TypeConName(module_ref, tmpl.tycon.segments)
                templates[f"{module.name}:{tmpl.tycon}"] = (tmpl_name, tmpl)

            for iface in module.interfaces:
                iface_name = TypeConName(module_ref, iface.name.segments)
                interfaces[f"{module.name}:{iface.name}"] = (iface_name, iface)

        self._data_types = MappingProxyType(data_types)
        self._values = MappingProxyType(values)
        self._templates = MappingProxyType(templates)
        self._interfaces = MappingProxyType(interfaces)

    def archives(self) -> Collection[Archive]:
        return [self.archive]

    def package_ids(self) -> AbstractSet[PackageRef]:
        return frozenset([self.archive.hash])

    def data_type_name(self, ref: Any) -> TypeConName:
        pkg, name = validate_template(ref)
        if pkg == self.archive.hash or pkg == STAR:
            dt_name = self.local_data_type_name(name)
            if dt_name is not None:
                return dt_name

        raise NameNotFoundError(ref)

    def data_type(self, ref: Any) -> DefDataType:
        pkg, name = validate_template(ref)
        if pkg == self.archive.hash or pkg == STAR:
            dt = self.local_data_type(name)
            if dt is not None:
                return dt

        raise NameNotFoundError(ref)

    def local_data_type_name(self, name: str) -> Optional[TypeConName]:
        r = self._data_types.get(name)
        return r[0] if r is not None else None

    def local_data_type(self, name: str) -> Optional[DefDataType]:
        """
        Variation of :meth:`data_type` that assumes the name is already scoped to this package.
        Unlike :meth:`data_type`, this method returns ``None`` in the case of no match.

        You should not normally use this method directly, and instead prefer to use the methods of
        the :class:`SymbolLookup` protocol.

        :param name:
            A name to search for. Must be of the form ``"ModuleName:EntityName"``, where both
            modules and entities are dot-delimited.
        :return:
            Either a matching :class:`DefDataType`, or ``None`` if no match.
        """
        r = self._data_types.get(name)
        return r[1] if r is not None else None

    def value(self, ref: Any) -> DefValue:
        pkg, name = validate_template(ref)
        if pkg == self.archive.hash or pkg == STAR:
            dt = self.local_value(name)
            if dt is not None:
                return dt

        raise NameNotFoundError(ref)

    def local_value(self, name: str) -> Optional[DefValue]:
        """
        Variation of :meth:`data_type` that assumes the name is already scoped to this package.
        Unlike :meth:`data_type`, this method returns ``None`` in the case of no match.

        You should not normally use this method directly, and instead prefer to use the methods of
        the :class:`SymbolLookup` protocol.

        :param name:
            A name to search for. Must be of the form ``"ModuleName:EntityName"``, where both
            modules and entities are dot-delimited.
        :return:
            Either a matching :class:`DefDataType`, or ``None`` if no match.
        """
        r = self._values.get(name)
        return r[1] if r is not None else None

    def template_names(self, ref: Any) -> Collection[TypeConName]:
        pkg, name = validate_template(ref)
        if pkg == self.archive.hash or pkg == STAR:
            if name == "*":
                return self.local_template_names()
            elif name in self._templates:
                n, _ = self._templates[name]
                return [n]
        return []

    def template_name(self, ref: Any) -> TypeConName:
        pkg, name = validate_template(ref)
        if pkg == self.archive.hash or pkg == STAR:
            tmpl = self.local_template_name(name)
            if tmpl is not None:
                return tmpl

        raise NameNotFoundError(ref)

    def template(self, ref: Any) -> DefTemplate:
        pkg, name = validate_template(ref)
        if pkg == self.archive.hash or pkg == STAR:
            tmpl = self.local_template(name)
            if tmpl is not None:
                return tmpl

        raise NameNotFoundError(ref)

    def interface_names(self, ref: Any) -> Collection[TypeConName]:
        pkg, name = validate_template(ref)
        if pkg == self.archive.hash or pkg == STAR:
            if name in self._interfaces:
                n, _ = self._interfaces[name]
                return [n]
        return []

    def interface_name(self, ref: Any) -> TypeConName:
        pkg, name = validate_template(ref)
        if pkg == self.archive.hash or pkg == STAR:
            iface = self.local_interface_name(name)
            if iface is not None:
                return iface

        raise NameNotFoundError(ref)

    def interface(self, ref: Any) -> DefInterface:
        pkg, name = validate_template(ref)
        if pkg == self.archive.hash or pkg == STAR:
            iface = self.local_interface(name)
            if iface is not None:
                return iface

        raise NameNotFoundError(ref)

    def template_or_interface_names(self, ref: Any) -> Collection[TypeConName]:
        pkg, name = validate_template(ref)
        if pkg == self.archive.hash or pkg == STAR:
            if name == "*":
                return self.local_template_names()
            elif name in self._templates:
                n, _ = self._templates[name]
                return [n]
            elif name in self._interfaces:
                n, _ = self._interfaces[name]
                return [n]
        return []

    def template_or_interface_name(self, ref: Any) -> TypeConName:
        pkg, name = validate_template(ref)
        if pkg == self.archive.hash or pkg == STAR:
            tmpl = self.local_template_name(name)
            if tmpl is not None:
                return tmpl

            iface = self.local_interface_name(name)
            if iface is not None:
                return iface

        raise NameNotFoundError(ref)

    def template_or_interface(self, ref: Any) -> TemplateOrInterface:
        pkg, name = validate_template(ref)
        if pkg == self.archive.hash or pkg == STAR:
            tmpl = self.local_template(name)
            if tmpl is not None:
                return tmpl

            iface = self.local_interface(name)
            if iface is not None:
                return iface

        raise NameNotFoundError(ref)

    def local_template_names(self) -> Collection[TypeConName]:
        return [n for n, _ in self._templates.values()]

    def local_template_name(self, name: str) -> Optional[TypeConName]:
        r = self._templates.get(name)
        return r[0] if r is not None else None

    def local_template(self, name: str) -> Optional[DefTemplate]:
        """
        Variation of :meth:`data_type` that assumes the name is already scoped to this package.
        Unlike :meth:`data_type`, this method returns ``None`` in the case of no match.

        You should not normally use this method directly, and instead prefer to use the methods of
        the :class:`SymbolLookup` protocol.

        :param name:
            A name to search for. Must be of the form ``"ModuleName:EntityName"``, where both
            modules and entities are dot-delimited.
        :return:
            Either a matching :class:`DefTemplate`, or ``None`` if no match.
        """
        r = self._templates.get(name)
        return r[1] if r is not None else None

    def local_interface_names(self) -> Collection[TypeConName]:
        return [n for n, _ in self._interfaces.values()]

    def local_interface_name(self, name: str) -> Optional[TypeConName]:
        r = self._interfaces.get(name)
        return r[0] if r is not None else None

    def local_interface(self, name: str) -> Optional[DefInterface]:
        """
        Variation of :meth:`data_type` that assumes the name is already scoped to this package.
        Unlike :meth:`data_type`, this method returns ``None`` in the case of no match.

        You should not normally use this method directly, and instead prefer to use the methods of
        the :class:`SymbolLookup` protocol.

        :param name:
            A name to search for. Must be of the form ``"ModuleName:EntityName"``, where both
            modules and entities are dot-delimited.
        :return:
            Either a matching :class:`DefInterface`, or ``None`` if no match.
        """
        r = self._interfaces.get(name)
        return r[1] if r is not None else None


class MultiPackageLookup(SymbolLookup):
    """
    Combines lookups across multiple archives.

    This class is thread-safe. When calling :meth:`add_archive` and any of the other read-only
    methods concurrently, read-only methods will NOT block; they will return the previous state
    of the lookup.

    Packages can only be added; they cannot be removed once added.
    """

    def __init__(self, archives: Optional[Collection[Archive]] = None):
        self._lock = threading.Lock()
        self._cache = dict[PackageRef, PackageLookup]()
        if archives is not None:
            self.add_archive(*archives)

    def archives(self) -> Collection[Archive]:
        """
        Return the list of known archives.
        """
        return [lookup.archive for lookup in self._cache.values()]

    def add_archive(self, *a: Archive) -> None:
        """
        Add one or more :class:`Archive` instances to this lookup.

        This method is thread-safe, but note that :class:`MultiPackageLookup` allows dirty reads for
        performance reasons.

        :param a: One or more :class:`Archive` instances to add.
        """
        new_lookups = {ar.hash: PackageLookup(ar) for ar in a}
        with self._lock:
            # replace the old cache with a new one, incorporating values from both the existing
            # cache and the new lookups that came in. When there is a key conflict between the two
            # APIs, always prefer the existing cache to provide stability to callers.
            self._cache = {**new_lookups, **self._cache}
            LOG.debug("Updated package cache; now contains %d packages.", len(self._cache))

    def package_ids(self) -> AbstractSet[PackageRef]:
        """
        Return the package IDs of packages stored in this lookup.

        Because the data is local and in memory, the timeout parameter is ignored.
        """
        return set(self._cache)

    def package(self, ref: PackageRef) -> Package:
        lookup = self._cache.get(ref)
        if lookup is not None:
            return lookup.archive.package

        raise PackageNotFoundError(ref)

    def data_type_name(self, ref: Any) -> TypeConName:
        pkg, name = validate_template(ref)
        for lookup in self._lookups(pkg):
            dt_name = lookup.local_data_type_name(name)
            if dt_name is not None:
                return dt_name

        raise NameNotFoundError(ref)

    def data_type(self, ref: Any) -> DefDataType:
        pkg, name = validate_template(ref)
        for lookup in self._lookups(pkg):
            dt = lookup.local_data_type(name)
            if dt is not None:
                return dt

        raise NameNotFoundError(ref)

    def value(self, ref: Any) -> DefValue:
        pkg, name = validate_template(ref)
        for lookup in self._lookups(pkg):
            val = lookup.local_value(name)
            if val is not None:
                return val

        raise NameNotFoundError(ref)

    def template_names(self, ref: Any) -> Collection[TypeConName]:
        names = list[TypeConName]()

        pkg, name = validate_template(ref)
        lookups = self._lookups(pkg)

        for lookup in lookups:
            if name == "*":
                names.extend(lookup.local_template_names())
            else:
                n = lookup.local_template_name(name)
                if n is not None:
                    names.append(n)

        return names

    def template_name(self, ref: Any) -> TypeConName:
        pkg, name = validate_template(ref)
        for lookup in self._lookups(pkg):
            n = lookup.local_template_name(name)
            if n is not None:
                return n

        raise NameNotFoundError(ref)

    def template(self, ref: Any) -> DefTemplate:
        pkg, name = validate_template(ref)
        for lookup in self._lookups(pkg):
            tmpl = lookup.local_template(name)
            if tmpl is not None:
                return tmpl

        raise NameNotFoundError(ref)

    def interface_names(self, ref: Any) -> Collection[TypeConName]:
        names = list[TypeConName]()

        pkg, name = validate_template(ref)
        lookups = self._lookups(pkg)

        for lookup in lookups:
            n = lookup.local_interface_name(name)
            if n is not None:
                names.append(n)

        return names

    def interface_name(self, ref: Any) -> TypeConName:
        pkg, name = validate_template(ref)
        for lookup in self._lookups(pkg):
            n = lookup.local_interface_name(name)
            if n is not None:
                return n

        raise NameNotFoundError(ref)

    def interface(self, ref: Any) -> DefInterface:
        pkg, name = validate_template(ref)
        for lookup in self._lookups(pkg):
            iface = lookup.local_interface(name)
            if iface is not None:
                return iface

        raise NameNotFoundError(ref)

    def template_or_interface_names(self, ref: Any) -> Collection[TypeConName]:
        names = list[TypeConName]()

        pkg, name = validate_template(ref)
        lookups = self._lookups(pkg)

        for lookup in lookups:
            if name == "*":
                names.extend(lookup.local_template_names())
            else:
                n = lookup.local_template_name(name)
                if n is not None:
                    names.append(n)
                n = lookup.local_interface_name(name)
                if n is not None:
                    names.append(n)

        return names

    def template_or_interface_name(self, ref: Any) -> TypeConName:
        pkg, name = validate_template(ref)
        for lookup in self._lookups(pkg):
            n = lookup.local_template_name(name)
            if n is not None:
                return n

            n = lookup.local_interface_name(name)
            if n is not None:
                return n

        raise NameNotFoundError(ref)

    def template_or_interface(self, ref: Any) -> TemplateOrInterface:
        pkg, name = validate_template(ref)
        for lookup in self._lookups(pkg):
            tmpl = lookup.local_template(name)
            if tmpl is not None:
                return tmpl

            iface = lookup.local_interface(name)
            if iface is not None:
                return iface

        raise NameNotFoundError(ref)

    def _lookups(self, ref: PackageRef) -> Iterable[PackageLookup]:
        """
        Return the individual :class:`PackageLookup` objects that should be consulted based on the
        :class:`PackageRef`.

        :param ref:
            A :class:`PackageRef` to look for.
        :return:
            A collection of :class:`PackageLookup` objects that match the :class:`PackageRef`. This
            collection is never empty.
        :raises PackageNotFoundError:
            if the :class:`PackageRef` points to a package that is not present in this lookup.
        """
        if ref == "*":
            return self._cache.values()

        lookup = self._cache.get(ref)
        if lookup is not None:
            return (lookup,)

        raise PackageNotFoundError(ref)


class PackageExceptionTracker:
    """
    A context manager that gracefully recovers from errors related to missing packages that are
    retryable.
    """

    def __init__(self) -> None:
        self._seen_types = set[str]()
        self._seen_packages = set[PackageRef]()
        self._pkg_refs = list[PackageRef]()
        self.done = False

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if isinstance(exc_val, PackageNotFoundError):
            # every time we fail serialization due to a missing package or type,
            # try to resolve it; remember what we tried, because if we fail again
            # for the same reason it is likely fatal
            if exc_val.ref in self._seen_packages:
                # we already looked for this package and couldn't find it; this will
                # never succeed, so we can't suppress this error
                return None

            self._seen_packages.add(exc_val.ref)

            # the caller should try to load the offending package, and then retry the operation
            self._pkg_refs.append(exc_val.ref)
            return True

        elif isinstance(exc_val, NameNotFoundError):
            if exc_val.ref in self._seen_types:
                # we already looked for this type and couldn't find it; this will
                # never succeed
                LOG.verbose(
                    "Failed to find name %s in all known packages, "
                    "even after fetching the latest.",
                    exc_val.ref,
                )
                raise

            with warnings.catch_warnings():
                warnings.simplefilter("ignore", DeprecationWarning)
                pkg_id, name = validate_template(exc_val.ref)
            if pkg_id == "*":
                # we don't know what package contains this type, so we have no
                # choice but to look in all known packages
                LOG.verbose(
                    "Failed to find name %s in all known packages, " "so loading ALL packages...",
                    name,
                )
                self._seen_types.add(exc_val.ref)

                # the caller should load all packages, and then retry the operation
                self._pkg_refs.append(STAR)
                return True
            else:
                # we know what package this type comes from, but it did not contain
                # the required type
                LOG.warning("Found package %s, but it did not include type %s", pkg_id, name)
                return None

    def pop_package(self) -> Optional[PackageRef]:
        """
        Return a :class:`PackageRef` that should be fetched before an operation is retried, or
        ``None`` if there is no such operation.
        """
        return self._pkg_refs.pop() if self._pkg_refs else None


def find_choice(template: DefTemplate, name: str) -> TemplateChoice:
    """
    Find a choice in a :class:`DefTemplate`. If the choice could not be found,
    :class:`NameNotFoundError` is raised.
    """
    for choice in template.choices:
        if choice.name == name:
            return choice

    raise NameNotFoundError(f"choice {name}")
