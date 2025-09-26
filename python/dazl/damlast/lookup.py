# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""
DAML-LF fast lookups
--------------------
"""

from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass
import threading
from types import MappingProxyType
from typing import (
    AbstractSet,
    Any,
    Collection,
    Generic,
    Iterable,
    Iterator,
    Literal,
    Mapping,
    NoReturn,
    Optional,
    Sequence,
    TypeVar,
    overload,
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
    _Name,
)
from .errors import AmbiguousMatchError, NameNotFoundError, PackageNotFoundError
from .protocols import SymbolLookup, TemplateOrInterface
from .util import package_local_name, package_ref

__all__ = [
    "STAR",
    "LookupResult",
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

K = TypeVar("K", bound=_Name)
V = TypeVar("V")
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


def validate_template(template: Any, /) -> tuple[PackageRef, str]:
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


def normalize(name: Optional[str | TypeConName], /) -> str:
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


def matching_normalizations(name: str | TypeConName, /) -> Sequence[str]:
    """
    Return strings that are possible matches for the given template ID.
    """
    p, m = validate_template(name)

    # throw away duplicates that arise from `name` not being fully specified (p and/or m are
    # allowed to be asterisks too)
    return list(dict.fromkeys([f"{p}:{m}", f"{p}:*", f"*:{m}", "*:*"]))


class LookupResult:
    """
    The results from a :meth:`SymbolLookup.lookup` call.
    """

    ref: Any
    data_types: LookupMapping[TypeConName, DefDataType]
    values: LookupMapping[ValName, DefValue]
    templates: LookupMapping[TypeConName, DefTemplate]
    interfaces: LookupMapping[TypeConName, DefInterface]

    def __init__(
        self,
        ref: Any,
        /,
        *,
        data_types: Sequence[LookupMappingItem[TypeConName, DefDataType]] = (),
        values: Sequence[LookupMappingItem[ValName, DefValue]] = (),
        templates: Sequence[LookupMappingItem[TypeConName, DefTemplate]] = (),
        interfaces: Sequence[LookupMappingItem[TypeConName, DefInterface]] = (),
    ) -> None:
        self.ref = ref
        self.data_types = LookupMapping(self, data_types)
        self.values = LookupMapping(self, values)
        self.templates = LookupMapping(self, templates)
        self.interfaces = LookupMapping(self, interfaces)

    def __bool__(self) -> bool:
        """
        Return ``True`` if this :class:`LookupResult` contains objects, or ``False`` otherwise.
        """
        return bool(self.data_types or self.values or self.templates or self.interfaces)

    def __add__(self, other: LookupResult, /) -> LookupResult:
        return LookupResult(
            self.ref,
            data_types=[*self.data_types._items, *other.data_types._items],
            values=[*self.values._items, *other.values._items],
            templates=[*self.templates._items, *other.templates._items],
            interfaces=[*self.interfaces._items, *other.interfaces._items],
        )


@dataclass(frozen=True)
class LookupMappingItem(Generic[K, V]):
    package_id_ref: K
    package_name_ref: Optional[K]
    object: V


class LookupMapping(Mapping[K, V]):
    """
    A mapping of references (where the :class:`PackageRef` is either ID-based or package name-based)
    to objects of a certain type.

    THIS IS NOT AN EFFICIENT STRUCTURE.
    """

    def __init__(self, parent: LookupResult, items: Sequence[LookupMappingItem[K, V]], /) -> None:
        """
        Construct a :class:`LookupMapping`.

        :param parent:
            The parent :class:`LookupMapping`.
        :param items:
            An ordered sequence of (ref [by package ID], ref [by package name], value).
            The package name is optional.
        """
        self._parent = parent
        self._items = tuple(items)

    def __getitem__(self, key: K, /) -> V:
        """
        Return the object that matches the specified key. This key can either be package-ID-based
        or package-name based.

        :param key: The key to fetch.
        :return: The matching object.
        :raises KeyError:
            Raised if the specified mapping does not exist.
        """
        for item in self._items:
            if key == item.package_id_ref or key == item.package_name_ref:
                return item.object
        raise KeyError(key)

    def __iter__(self) -> Iterator[K]:
        """
        Return an iterator over the package ID-based keys in this structure.
        """
        for item in self._items:
            yield item.package_id_ref

    def __len__(self) -> int:
        """
        Return the number of objects in this mapping.
        """
        return len(self._items)

    def __add__(self, other: LookupMapping[K, V], /) -> LookupMapping[K, V]:
        """
        Add the contents of this mapping and another mapping; return a new mapping that
        is the combined contents.

        :param other:
        :return:
        """
        return LookupMapping(self._parent, [*self._items, *other._items])

    def single(self) -> LookupMappingItem[K, V]:
        """
        Return the name and matching symbol in this :class:`LookupMapping`.

        When there are multiple matches because of Smart Contract Upgrade-compatible
        names, the most recent version is returned. Otherwise, if there are multiple
        matches, then an :class:`AmbiguousMatchError` is raised. If no names were
        found, a :class:`NameNotFoundError` is instead raised.
        """
        i = iter(self._items)
        item = next(i, None)
        if not item:
            raise NameNotFoundError(self._parent.ref)

        while other := next(i, None):
            # to support Smart Contract Upgradaes, multiple matches are allowed,
            # but only when the package names are the same
            if item.package_name_ref != other.package_name_ref:
                raise AmbiguousMatchError(self._parent.ref)

        return item

    def package_id_refs(self) -> Iterable[K]:
        """
        Return the unique set of package ID-based references that have matched.
        """
        for item in self._items:
            yield item.package_id_ref

    def package_name_refs(self) -> Iterable[K]:
        """
        Return the unique set of package name-based references that have matched.
        """
        seen = set[K]()
        for item in self._items:
            if item.package_name_ref is not None and item.package_name_ref not in seen:
                seen.add(item.package_name_ref)
                yield item.package_name_ref


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

    def search(self, ref: str | TypeConName, /, *, throw_if_missing: bool = True) -> LookupResult:
        raise empty_lookup_impl(ref)


class PackageLookup(SymbolLookup):
    """
    Caching structure to make lookups on type names within a :class:`Package` faster.
    """

    def __init__(self, archive: Archive):
        self.archive = archive

        # mappings of "naked names" (no package ID or package name) to items
        data_types = dict[str, LookupMappingItem[TypeConName, DefDataType]]()
        values = dict[str, LookupMappingItem[ValName, DefValue]]()
        templates = dict[str, LookupMappingItem[TypeConName, DefTemplate]]()
        interfaces = dict[str, LookupMappingItem[TypeConName, DefInterface]]()
        package_name = (
            PackageRef(f"#{self.archive.package.metadata.name}")
            if self.archive.package.metadata is not None
            else None
        )

        for module in archive.package.modules:
            module_id_ref = ModuleRef(archive.hash, module.name)
            module_name_ref = (
                ModuleRef(package_name, module.name) if package_name is not None else None
            )

            for dt in module.data_types:
                dt_id_ref = TypeConName(module_id_ref, dt.name.segments)
                dt_name_ref = (
                    TypeConName(module_name_ref, dt.name.segments)
                    if module_name_ref is not None
                    else None
                )
                data_types[f"{module.name}:{dt.name}"] = LookupMappingItem(
                    dt_id_ref, dt_name_ref, dt
                )

            for value in module.values:
                value_id_ref = ValName(module_id_ref, value.name_with_type.name)
                value_name_ref = (
                    ValName(module_name_ref, value.name_with_type.name)
                    if module_name_ref is not None
                    else None
                )
                values[f"{module.name}:{value.name_with_type.name}"] = LookupMappingItem(
                    value_id_ref, value_name_ref, value
                )

            for tmpl in module.templates:
                tmpl_id_ref = TypeConName(module_id_ref, tmpl.tycon.segments)
                tmpl_name_ref = (
                    TypeConName(module_name_ref, tmpl.tycon.segments)
                    if module_name_ref is not None
                    else None
                )
                templates[f"{module.name}:{tmpl.tycon}"] = LookupMappingItem(
                    tmpl_id_ref, tmpl_name_ref, tmpl
                )

            for iface in module.interfaces:
                iface_id_ref = TypeConName(module_id_ref, iface.name.segments)
                iface_name_ref = (
                    TypeConName(module_name_ref, iface.name.segments)
                    if module_name_ref is not None
                    else None
                )
                interfaces[f"{module.name}:{iface.name}"] = LookupMappingItem(
                    iface_id_ref, iface_name_ref, iface
                )

        self._package_name = (
            PackageRef(f"#{self.archive.package.metadata.name}")
            if self.archive.package.metadata is not None
            else None
        )
        self._data_types = MappingProxyType[str, LookupMappingItem[TypeConName, DefDataType]](
            data_types
        )
        self._values = MappingProxyType[str, LookupMappingItem[ValName, DefValue]](values)
        self._templates = MappingProxyType[str, LookupMappingItem[TypeConName, DefTemplate]](
            templates
        )
        self._interfaces = MappingProxyType[str, LookupMappingItem[TypeConName, DefInterface]](
            interfaces
        )

    def archives(self) -> Collection[Archive]:
        return [self.archive]

    def package_ids(self) -> AbstractSet[PackageRef]:
        return frozenset([self.archive.hash])

    @property
    def scu_package_name(self) -> Optional[PackageRef]:
        """
        Return the Smart Contract Upgradable (SCU) name of this package, with the preceding hash tag.
        """
        return self._package_name

    def search(self, ref: str | TypeConName, /, *, throw_if_missing: bool = True) -> LookupResult:
        """
        Search for symbols that match the specified string.

        :param ref:
            The string or :class:`TypeConName` to search for.
        :param throw_if_missing:
            Throw a :class:`NameNotFoundError` if no objects are returned; otherwise,
            return an empty object. The default behavior is to throw.
        :return:
            A :class:`LookupResult` that indicates the found objects.
        """
        pkg, name = validate_template(ref)
        if pkg == self.archive.hash or pkg == self.scu_package_name or pkg == STAR:
            if name == "*":
                # unspecified name, so return everything from everywhere
                return LookupResult(
                    ref,
                    data_types=tuple(self._data_types.values()),
                    values=tuple(self._values.values()),
                    templates=tuple(self._templates.values()),
                    interfaces=tuple(self._interfaces.values()),
                )
            else:
                data_type = self._data_types.get(name)
                value = self._values.get(name)
                template = self._templates.get(name)
                interface = self._interfaces.get(name)
                return LookupResult(
                    ref,
                    data_types=(data_type,) if data_type is not None else (),
                    values=(value,) if value is not None else (),
                    templates=(template,) if template is not None else (),
                    interfaces=(interface,) if interface is not None else (),
                )

        raise NameNotFoundError(ref)


class MultiPackageLookup(SymbolLookup):
    """
    Combines lookups across multiple archives.

    This class is thread-safe. When calling :meth:`add_archive` and any of the other read-only
    methods concurrently, read-only methods will NOT block; they will return the previous state
    of the lookup.

    Packages can only be added; they cannot be removed once added.
    """

    _cache_by_pkg_id: Mapping[PackageRef, PackageLookup]
    _cache_by_name: Mapping[PackageRef, Sequence[PackageLookup]]

    def __init__(self, archives: Optional[Collection[Archive]] = None):
        self._lock = threading.Lock()
        self._cache_by_pkg_id = MappingProxyType({})
        self._cache_by_name = MappingProxyType({})
        if archives is not None:
            self.add_archive(*archives)

    def archives(self) -> Collection[Archive]:
        """
        Return the list of known archives.
        """
        return [lookup.archive for lookup in self._cache_by_pkg_id.values()]

    def add_archive(self, *a: Archive) -> None:
        """
        Add one or more :class:`Archive` instances to this lookup.

        This method is thread-safe, but note that :class:`MultiPackageLookup` allows dirty reads for
        performance reasons.

        :param a: One or more :class:`Archive` instances to add.
        """
        new_lookups_by_id = {ar.hash: PackageLookup(ar) for ar in a}
        with self._lock:
            # replace the old cache with a new one, incorporating values from both the existing
            # cache and the new lookups that came in. When there is a key conflict between the two
            # APIs, always prefer the existing cache to provide stability to callers.
            cache_by_id = {**new_lookups_by_id, **self._cache_by_pkg_id}

            # (re)build the by-name package cache for smart contract upgrade (SCU) support;
            # we also allow template lookups by package name, and will prefer the most recent
            # version
            lookups_by_name = defaultdict[PackageRef, list[PackageLookup]](list)
            for package_lookup in cache_by_id.values():
                scu_name = package_lookup.scu_package_name
                if scu_name is not None:
                    lookups_by_name[scu_name].append(package_lookup)

            cache_by_name = {
                scu_pkg_ref: sorted(package_lookups, key=get_version_tuple)
                for scu_pkg_ref, package_lookups in lookups_by_name.items()
            }

            self._cache_by_pkg_id = cache_by_id
            self._cache_by_name = cache_by_name
            LOG.debug(
                "Updated package cache; now contains %d packages.", len(self._cache_by_pkg_id)
            )

    def package_ids(self) -> AbstractSet[PackageRef]:
        """
        Return the package IDs of packages stored in this lookup.

        Because the data is local and in memory, the timeout parameter is ignored.
        """
        return set(self._cache_by_pkg_id)

    def package(self, ref: PackageRef) -> Package:
        lookups = list(self._lookups(ref))
        if len(lookups) == 1:
            return lookups[0].archive.package

        # TODO: More descriptive error message here
        raise PackageNotFoundError(ref)

    def search(self, ref: str | TypeConName, /, *, throw_if_missing: bool = True) -> LookupResult:
        pkg, name = validate_template(ref)
        result = LookupResult(ref)
        for lookup in self._lookups(pkg, throw_if_missing=throw_if_missing):
            result += lookup.search(ref, throw_if_missing=False)

        if throw_if_missing and not result:
            raise NameNotFoundError(ref)

        return result

    def _lookups(
        self, ref: PackageRef, /, throw_if_missing: bool = True
    ) -> Iterable[PackageLookup]:
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
        if ref == STAR:
            # unspecified package ID, so return all possible package lookups
            return self._cache_by_pkg_id.values()

        elif ref.startswith("#"):
            # SCU-style template reference; find the most up-to-date package for this package name
            lookups = self._cache_by_name.get(ref)
            if lookups is not None:
                return lookups

        else:
            lookup = self._cache_by_pkg_id.get(ref)
            if lookup is not None:
                return (lookup,)

        if throw_if_missing:
            raise PackageNotFoundError(ref)
        else:
            return ()


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


def get_version_tuple(lookup: PackageLookup) -> tuple[int, ...]:
    md = lookup.archive.package.metadata
    if md is not None:
        return tuple([int(s) for s in md.version.split(".")])
    else:
        return ()
