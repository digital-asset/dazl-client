# Copyright (c) 2017-2022 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from collections import defaultdict
from dataclasses import dataclass
from functools import reduce
from operator import add
import sys
from threading import RLock
from types import MappingProxyType
from typing import (
    Any,
    Collection,
    DefaultDict,
    Dict,
    Generic,
    Iterable,
    List,
    Mapping,
    Optional,
    TypeVar,
    Union,
    no_type_check,
)
import warnings

from ..damlast.daml_lf_1 import Archive, Expr, Package, PackageRef, TypeConName, ValName, _Name
from ..damlast.lookup import validate_template
from ..util.typing import safe_cast, safe_dict_cast

if sys.version_info >= (3, 8):
    from typing import Protocol, runtime_checkable
else:
    from typing_extensions import Protocol, runtime_checkable


with warnings.catch_warnings():
    warnings.simplefilter("ignore", DeprecationWarning)

    from .types import (
        ConcreteType,
        PackageIdSet,
        Template,
        TemplateChoice,
        Type,
        TypeReference,
        UnresolvedTypeReference,
    )

K = TypeVar("K", bound=_Name)
T = TypeVar("T")
S = TypeVar("S")

warnings.warn(
    "The types of dazl.model.types_store are deprecated", DeprecationWarning, stacklevel=2
)


class PackageStoreBuilder:
    """
    Convenience class for building up a :class:`PackageStore`.
    """

    def __init__(self):
        warnings.warn(
            "PackageStoreBuilder is deprecated; there is no direct replacement.",
            DeprecationWarning,
            stacklevel=2,
        )

        self._archives = list()  # type: List[Archive]
        self._value_types = dict()  # type: Dict[ValName, Expr]
        self._data_types = dict()  # type: Dict[TypeConName, Type]
        self._templates = dict()  # type: Dict[TypeConName, Template]
        self._expected_package_ids = None  # type: Optional[Collection[PackageRef]]

    def add_archive(self, archive: "Archive") -> None:
        self._archives.append(archive)

    def add_type(self, name: "TypeConName", data_type: Type):
        safe_cast(TypeConName, name)
        self._data_types[name] = safe_cast(Type, data_type)

    def add_value(self, name: "ValName", value: "Expr"):
        safe_cast(ValName, name)
        self._value_types[name] = safe_cast(Expr, value)

    def add_template(self, template: Template):
        name = template.data_type.name
        if name is None:
            raise ValueError("template cannot be defined with an anonymous type")
        self._templates[name.con] = safe_cast(Template, template)

    def add_expected_package_ids(self, expected_package_ids: "Collection[PackageRef]"):
        self._expected_package_ids = expected_package_ids

    def get_type(self, name: TypeConName) -> "Optional[Type]":
        return self._data_types.get(name)

    def build(self) -> "PackageStore":
        return PackageStore(
            self._archives,
            self._value_types,
            self._data_types,
            self._templates,
            self._expected_package_ids,
        )


class PackageStore:
    """
    A thread-safe store of type information.
    """

    @classmethod
    def empty(cls):
        """
        Create an empty store.
        """
        warnings.warn(
            "PackageStore is deprecated; use PackageLoader/SymbolLookup instead",
            DeprecationWarning,
            stacklevel=2,
        )

        return cls([], {}, {}, {}, None)

    def __init__(
        self,
        archives: "Collection[Archive]",
        value_types: "Dict[ValName, Expr]",
        data_types: "Dict[TypeConName, Type]",
        templates: "Dict[TypeConName, Template]",
        expected_package_ids: "Optional[Collection[PackageRef]]" = None,
    ):
        warnings.warn(
            "PackageStore is deprecated; use PackageLoader/SymbolLookup instead",
            DeprecationWarning,
            stacklevel=2,
        )
        self._lock = RLock()
        self._archives = list(archives)
        self._cache = PackageStoreCache(EMPTY_TYPE_CACHE, EMPTY_TYPE_CACHE, EMPTY_TYPE_CACHE)
        self._value_types = safe_dict_cast(ValName, Expr, value_types)
        self._data_types = safe_dict_cast(TypeConName, Type, data_types)
        self._templates = safe_dict_cast(TypeConName, Template, templates)
        self._expected_package_ids = expected_package_ids

    def archives(self) -> "Collection[Archive]":
        """
        Return a copy of the collection of the set of loaded :class:`Archive`s.
        """
        warnings.warn(
            "PackageStore.archives() is deprecated; use SymbolLookup.archives() instead",
            DeprecationWarning,
            stacklevel=2,
        )

        with self._lock:
            return list(self._archives)

    def packages(self) -> "Collection[Package]":
        """
        Return a copy of the collection of the set of loaded :class:`Package`s.
        """
        warnings.warn(
            "PackageStore.packages() is deprecated; use SymbolLookup.archives() instead",
            DeprecationWarning,
            stacklevel=2,
        )

        with self._lock:
            return [a.package for a in self._archives]

    def package_ids(self) -> "Collection[PackageRef]":
        """
        Return a copy of the collection of the set of loaded :class:`Package`s.
        """
        warnings.warn(
            "PackageStore.package_ids() is deprecated; use SymbolLookup.package_ids() instead",
            DeprecationWarning,
            stacklevel=2,
        )

        with self._lock:
            return [a.hash for a in self._archives]

    def expected_package_ids(self) -> "Optional[Collection[PackageRef]]":
        """
        Return package IDs that are expected to be found on the ledger.
        """
        warnings.warn(
            "PackageStore.expected_package_ids() is deprecated; there is no replacement.",
            DeprecationWarning,
            stacklevel=2,
        )
        return self._expected_package_ids

    def register_all(self, other_store: "PackageStore") -> "PackageStore":
        """
        Register all types declared in the other :class:`PackageStore`.

        :param other_store: A package store to copy types, templates, and choices from.
        :return: A reference to this object.
        """
        warnings.warn(
            "PackageStore.register_all() is deprecated; use PackageLoader instead.",
            DeprecationWarning,
            stacklevel=2,
        )

        if self is not other_store:
            with self._lock:
                self._archives.extend(other_store._archives)
                self._value_types.update(other_store._value_types)
                self._data_types.update(other_store._data_types)
                self._templates.update(other_store._templates)
                self._cache = PackageStoreCache(
                    TypeCache.build(self._value_types),
                    TypeCache.build(self._data_types),
                    TypeCache.build(self._templates),
                )
        return self

    def resolve_value_reference(self, value_ref: "ValName") -> "Expr":
        warnings.warn(
            "PackageStore.resolve_value_reference() is deprecated; "
            "use SymbolLookup.value() instead.",
            DeprecationWarning,
            stacklevel=2,
        )

        with self._lock:
            return self._value_types[value_ref]

    def resolve_type_reference(self, template_ref: "Union[TypeConName, TypeReference]") -> Type:
        """
        Resolve a type based on its reference.

        :param template_ref:
            A :class:`TypeReference` that refers to a type.
        :return:
            The :class:`Type` that is referred to by this type reference.
        :raise KeyError:
            If the :class:`TypeReference` does not have a corresponding value in this store.
        """
        warnings.warn(
            "PackageStore.resolve_value_reference() is deprecated; "
            "use SymbolLookup.data_type() instead.",
            DeprecationWarning,
            stacklevel=2,
        )

        if isinstance(template_ref, TypeReference):
            con = template_ref.con
        elif isinstance(template_ref, TypeConName):
            con = template_ref
        else:
            raise ValueError("template_ref must either by a TypeConName or TypeReference")

        with self._lock:
            return self._data_types[con]

    def types(self) -> "Mapping[TypeConName, ConcreteType]":
        warnings.warn(
            'PackageStore.types() is deprecated; use SymbolLookup.data_type("*") instead.',
            DeprecationWarning,
            stacklevel=2,
        )

        with self._lock:
            return MappingProxyType(dict(self._data_types))  # type: ignore

    def get_templates_for_packages(
        self, package_ids: "Iterable[PackageRef]"
    ) -> "Collection[Template]":
        """
        Return a collection of :class:`Template` instances from the given set of package IDs.

        :param package_ids:
            The set of package IDs to restrict templates to.
        :return:
            A collection of matching templates, or an empty collection if none match. This method
            never returns ``None``.
        """
        warnings.warn(
            "PackageStore.get_templates_for_packages() is deprecated; "
            'use [SymbolLookup.templates(f"{pkg}:*") for pkg in package_ids] instead.',
            DeprecationWarning,
            stacklevel=2,
        )

        match = []  # type: List[Template]
        for pkg_id in package_ids:
            match.extend(self._cache.templates.lookup(pkg_id, "*"))
        return match

    def resolve_template(
        self, template: "Union[None, str, TypeReference, UnresolvedTypeReference, TypeConName]"
    ) -> Collection[Template]:
        """
        Return a collection of :class:`Template` instances that match the specified template name.

        Some special parameters:
         * If ``"*"`` is passed in, all templates are returned.
         * If ``None`` is passed in, an empty collection is returned.

        :param template:
            A template name or a :class:`TypeReference`.
        :return:
            A collection of matching templates, or an empty collection if none match. This method
            never returns ``None``.
        """
        warnings.warn(
            "PackageStore.resolve_template() is deprecated; use SymbolLookup.template() instead.",
            DeprecationWarning,
            stacklevel=2,
        )

        if isinstance(template, Template):
            # if we were given a Template for some strange reason, just simply return a single-item
            # tuple of that given Template
            return [template]

        package_id, template_name = validate_template(template, allow_deprecated_identifiers=True)
        return self._cache.templates.lookup(package_id, template_name)

    def resolve_template_type(
        self, template: "Union[None, str, TypeReference, UnresolvedTypeReference, TypeConName]"
    ) -> Dict[TypeReference, Type]:
        """
        Return a collection of types that match for the template.

        :param template:
            A template name or a :class:`TypeReference`.
        :return:
            A dictionary of possible matches, or empty if there are no matches. This method never
            returns ``None``.
        """
        warnings.warn(
            "PackageStore.resolve_template() is deprecated; use SymbolLookup.template() instead.",
            DeprecationWarning,
            stacklevel=2,
        )

        with warnings.catch_warnings():
            warnings.simplefilter("ignore", DeprecationWarning)

            return {
                template.data_type.name: template.data_type
                for template in self.resolve_template(template)
                if template.data_type.name is not None
            }

    def resolve_choice(self, template: Any, choice: str) -> Dict[TypeReference, TemplateChoice]:
        """
        Return all possible choices for the combination of template identifier and choice name.
        If template is ``'*'`` or ``None``, all choices with the specified name are returned.
        """
        warnings.warn(
            'PackageStore.resolve_choice() is deprecated; use SymbolLookup.template("*") instead, '
            "and lookup the choice within the returned Template.",
            DeprecationWarning,
            stacklevel=2,
        )

        with warnings.catch_warnings():
            warnings.simplefilter("ignore", DeprecationWarning)

            matches = dict()  # type: Dict[TypeReference, TemplateChoice]
            for t in self.resolve_template(template):
                for c in t.choices:
                    if c.name == choice and t.data_type.name is not None:
                        matches[t.data_type.name] = c
            return matches


@runtime_checkable
class PackageProvider(Protocol):
    """
    Interface to an object that can provide package information.
    """

    def __init__(self):
        warnings.warn(
            "PackageProvider is deprecated; use PackageLookup instead.",
            DeprecationWarning,
            stacklevel=2,
        )

    def get_package_ids(self) -> "PackageIdSet":
        """
        Return the current universe of package IDs.
        """
        raise NotImplementedError

    def fetch_package(self, package_id: "PackageRef") -> bytes:
        """
        Retrieve the bytes that correspond to a package.
        """
        raise NotImplementedError

    def get_all_packages(self) -> "Mapping[PackageRef, bytes]":
        raise NotImplementedError


class MemoryPackageProvider:
    def __init__(self, mapping: "Mapping[PackageRef, bytes]"):
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", DeprecationWarning)
            super().__init__()
        warnings.warn(
            "MemoryPackageProvider is deprecated; there is no replacement.",
            DeprecationWarning,
            stacklevel=2,
        )
        self.mapping = mapping

    def get_package_ids(self) -> "PackageIdSet":
        return frozenset(self.mapping.keys())

    # fetch_package is actually supposed to throw an error on missing packages, but people may
    # be reliant on the old behavior; anyway this entire file is deprecated; changing the behavior
    # of a soon-to-be-removed class seems unnecessary
    @no_type_check
    def fetch_package(self, package_id: "PackageRef") -> bytes:
        return self.mapping.get(package_id)

    def get_all_packages(self) -> "Mapping[PackageRef, bytes]":
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", DeprecationWarning)
            return {pkg_id: self.fetch_package(pkg_id) for pkg_id in self.get_package_ids()}


@dataclass(frozen=True)
class PackageStoreCache:
    value_types: "TypeCache[ValName, Expr]"
    data_types: "TypeCache[TypeConName, Type]"
    templates: "TypeCache[TypeConName, Template]"


@dataclass(frozen=True)
class TypeCache(Generic[K, T]):
    """
    Immutable cache of type information.

    Instance attributes:

    .. attribute:: TypeCache.by_package_lookup

        A mapping from package ID strings to another mapping, where keys are fully-qualified type
        names for templates to a collection of matching Template instances. These collections are
        never non-empty; they will only ever contain multiple entries if there is a collision in
        dot-separated names.

    .. attribute:: TypeCache.by_name_lookup

        A mapping from fully-qualified type names (excluding package IDs) to ``Collection[T]``.
        These subcollections will only contain multiple values if names are not unique with respect
        to package IDs.
    """

    everything: "Collection[T]"
    by_package_lookup: "Mapping[PackageRef, Mapping[str, Collection[T]]]"
    by_name_lookup: "Mapping[str, Collection[T]]"

    @classmethod
    def build(cls, objects: "Mapping[K, T]") -> "TypeCache[K, T]":
        from ..damlast.util import package_local_name, package_ref

        everything = tuple(objects.values())
        by_package_lookup: DefaultDict[PackageRef, DefaultDict[str, List[T]]] = defaultdict(
            lambda: defaultdict(list)
        )
        by_name_lookup = defaultdict(list)

        for k, v in objects.items():
            package_id = package_ref(k)
            module_entity_name = package_local_name(k)
            # This is kept here for backwards compatibility, but its use should be discouraged
            module_entity_name_deprecated = module_entity_name.replace(":", ".")
            for valid_name in (module_entity_name, module_entity_name_deprecated):
                by_package_lookup[package_id][valid_name].append(v)
                by_name_lookup[valid_name].append(v)

        return TypeCache(
            everything,
            _immutable_mmc(by_package_lookup),
            MappingProxyType({k: tuple(v) for k, v in by_name_lookup.items()}),
        )

    def lookup(self, package_id: PackageRef, type_name: str) -> "Collection[T]":
        """
        Look up items based on package ID and type name. The values cannot be ``None``, but they
        can be the special-meaning ``'*'`` value.
        """
        safe_cast(str, package_id)
        safe_cast(str, type_name)

        if package_id == "*":
            if type_name == "*":
                # *:* means return everything
                return self.everything
            else:
                # *:Specific.Module:Entity means return all matches of the requested name, but
                # under any package
                return self.by_name_lookup.get(type_name, ())
        elif type_name == "*":
            # PKG_ID:* means return all matches in a specific package
            return reduce(add, self.by_package_lookup.get(package_id, {}).values(), ())
        else:
            # PKG_ID:Specific.Module:Entity; we are looking for a very specific type
            return self.by_package_lookup.get(package_id, {}).get(type_name, ())


def _immutable_mmc(
    mapping: "Mapping[S, Mapping[str, Collection[T]]]",
) -> "Mapping[S, Mapping[str, Collection[T]]]":
    """
    Create an immutable copy of :class:`TemplateStoreCache` data structures.
    """
    return MappingProxyType(
        {k1: MappingProxyType({k2: tuple(v) for k2, v in v1.items()}) for k1, v1 in mapping.items()}
    )


EMPTY_MAPPING = MappingProxyType({})  # type: ignore
EMPTY_TYPE_CACHE = TypeCache((), EMPTY_MAPPING, EMPTY_MAPPING)  # type: ignore
