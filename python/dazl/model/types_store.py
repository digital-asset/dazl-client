# Copyright (c) 2019 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from collections import defaultdict
from functools import reduce
from operator import add
from threading import RLock
from types import MappingProxyType

from dataclasses import dataclass
from typing import Any, Collection, Dict, Generic, List, Mapping, Optional, Sequence, TypeVar, \
    Union, TYPE_CHECKING

from .types import Template, TemplateChoice, Type, TypeReference, UnresolvedTypeReference, \
    TypeAdjective, ConcreteType, ValueReference
from ..util.typing import safe_cast, safe_dict_cast

if TYPE_CHECKING:
    from ..damlast.daml_lf_1 import Archive, Expr, Package

T = TypeVar('T')


class PackageStoreBuilder:
    """
    Convenience class for building up a :class:`PackageStore`.
    """

    def __init__(self):
        self._archives = list()  # type: List[Archive]
        self._value_types = dict()  # type: Dict[ValueReference, Expr]
        self._data_types = dict()  # type: Dict[TypeReference, Type]
        self._templates = dict()  # type: Dict[TypeReference, Template]

    def add_archive(self, archive: 'Archive') -> None:
        self._archives.append(archive)

    def add_type(self, name: TypeReference, data_type: Type):
        safe_cast(TypeReference, name)
        safe_cast(Type, data_type)
        self._data_types[name] = data_type

    def add_value(self, name: ValueReference, value: 'Expr'):
        self._value_types[name] = value

    def add_template(self, template: Template):
        self._templates[template.data_type.name] = safe_cast(Template, template)

    def get_type(self, name: TypeReference) -> Optional[Type]:
        return self._data_types.get(name)

    def build(self) -> 'PackageStore':
        return PackageStore(self._archives, self._value_types, self._data_types, self._templates)


class PackageStore:
    """
    A thread-safe store of type information.
    """

    @classmethod
    def empty(cls):
        """
        Create an empty store.
        """
        return cls([], {}, {}, {})

    def __init__(
            self,
            archives: 'Collection[Archive]',
            value_types: 'Dict[ValueReference, Expr]',
            data_types: 'Dict[TypeReference, Type]',
            templates: 'Dict[TypeReference, Template]'):
        self._lock = RLock()
        self._archives = list(archives)
        self._cache = PackageStoreCache(EMPTY_TYPE_CACHE, EMPTY_TYPE_CACHE, EMPTY_TYPE_CACHE)
        self._value_types = value_types  # safe_dict_cast(ValueReference, Expr, value_types)
        self._data_types = safe_dict_cast(TypeReference, Type, data_types)
        self._templates = safe_dict_cast(TypeReference, Template, templates)

    def archives(self) -> 'Collection[Archive]':
        """
        Return a copy of the collection of the set of loaded :class:`Archive`s.
        """
        with self._lock:
            return list(self._archives)

    def packages(self) -> 'Collection[Package]':
        """
        Return a copy of the collection of the set of loaded :class:`Package`s.
        """
        with self._lock:
            return [a.package for a in self._archives]

    def package_ids(self) -> 'Collection[str]':
        """
        Return a copy of the collection of the set of loaded :class:`Package`s.
        """
        with self._lock:
            return [a.hash for a in self._archives]

    def register_all(self, other_store: 'PackageStore') -> 'PackageStore':
        """
        Register all types declared in the other :class:`PackageStore`.

        :param other_store: A package store to copy types, templates, and choices from.
        :return: A reference to this object.
        """
        if self is not other_store:
            with self._lock:
                self._archives.extend(other_store._archives)
                self._value_types.update(other_store._value_types)
                self._data_types.update(other_store._data_types)
                self._templates.update(other_store._templates)
                self._cache = PackageStoreCache(
                    TypeCache.build(self._value_types),
                    TypeCache.build(self._data_types),
                    TypeCache.build(self._templates))
        return self

    def resolve_value_reference(self, value_ref: ValueReference) -> 'Expr':
        with self._lock:
            return self._value_types[value_ref]

    def resolve_type_reference(self, template_ref: TypeReference) -> Type:
        """
        Resolve a type based on its reference.

        :param template_ref:
            A :class:`TypeReference` that refers to a type.
        :return:
            The :class:`Type` that is referred to by this type reference.
        :raise KeyError:
            If the :class:`TypeReference` does not have a corresponding value in this store.
        """
        safe_cast(TypeReference, template_ref)

        with self._lock:
            return self._data_types[template_ref]

    def find_types(self, adjective: TypeAdjective = TypeAdjective.ANY) \
            -> Mapping[TypeReference, ConcreteType]:
        with self._lock:
            if adjective == TypeAdjective.ANY:
                return MappingProxyType(dict(self._data_types))

            return {tt: data_type
                    for tt, data_type in self._data_types.items()
                    if isinstance(data_type, ConcreteType)
                    and data_type.adjective & adjective != TypeAdjective.NONE}

    def resolve_template(self, template: Union[None, str, TypeReference, UnresolvedTypeReference]) \
            -> Collection[Template]:
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
        from .lookup import validate_template

        if isinstance(template, Template):
            # if we were given a Template for some strange reason, just simply return a single-item
            # tuple of that given Template
            return [template]

        package_id, template_name = validate_template(template)
        return self._cache.templates.lookup(package_id, template_name)

    def resolve_template_type(
            self, template: 'Union[None, str, TypeReference, UnresolvedTypeReference]') \
            -> Dict[TypeReference, Type]:
        """
        Return a collection of types that match for the template.

        :param template:
            A template name or a :class:`TypeReference`.
        :return:
            A dictionary of possible matches, or empty if there are no matches. This method never
            returns ``None``.
        """
        return {template.data_type.name: template.data_type
                for template in self.resolve_template(template)}

    def resolve_choice(self, template: Any, choice: str) -> Dict[TypeReference, TemplateChoice]:
        """
        Return all possible choices for the combination of template identifier and choice name.
        If template is ``'*'`` or ``None``, all choices with the specified name are returned.
        """
        matches = dict()
        for t in self.resolve_template(template):
            for c in t.choices:
                if c.name == choice:
                    matches[t.data_type.name] = c
        return matches


class PackageProvider:
    """
    Interface to an object that can provide package information.
    """

    def get_package_ids(self) -> 'Sequence[str]':
        """
        Return the current universe of package IDs.
        """
        raise NotImplementedError

    def fetch_package(self, package_id: str) -> bytes:
        """
        Retrieve the bytes that correspond to a package.
        """
        raise NotImplementedError

    def get_all_packages(self) -> 'Mapping[str, bytes]':
        return {pkg_id: self.fetch_package(pkg_id) for pkg_id in self.get_package_ids()}


class MemoryPackageProvider(PackageProvider):
    def __init__(self, mapping: 'Mapping[str, bytes]'):
        self.mapping = mapping

    def get_package_ids(self) -> 'Sequence[str]':
        return list(self.mapping.keys())

    def fetch_package(self, package_id: str) -> bytes:
        return self.mapping.get(package_id)


@dataclass(frozen=True)
class PackageStoreCache:
    value_types: 'TypeCache[Type]'
    data_types: 'TypeCache[Type]'
    templates: 'TypeCache[Template]'


@dataclass(frozen=True)
class TypeCache(Generic[T]):
    """
    Immutable cache of type information.

    Instance attributes:

    .. attribute:: TypeCache.by_package_lookup

        A mapping from package ID strings to another mapping, where keys are fully-qualified type
        names for templates to a collection of matching Template instances. These collections are
        never non-empty; they will only ever contain multiple entries if there is a collision in
        dot-separated names. None of these maps contain ``'*'`` as keys; wildcards mut be
        implemented by the caller.

    .. attribute:: TypeCache.by_name_lookup

        A mapping from fully-qualified type names to a sub-mapping, where the sub-mapping keys are
        package IDs and the value are collections of Template. None of these maps contain ``'*'``
        as keys; wildcards mut be implemented by the caller.
    """

    everything: Collection['T']
    by_package_lookup: 'Mapping[str, Mapping[str, Collection[T]]]'
    by_name_lookup: 'Mapping[str, Mapping[str, Collection[T]]]'

    @classmethod
    def build(cls, objects: 'Mapping[TypeReference, T]') -> 'TypeCache[T]':
        everything = tuple(objects)
        by_package_lookup = defaultdict(lambda: defaultdict(list))
        by_name_lookup = defaultdict(lambda: defaultdict(list))

        for k, v in objects.items():
            for package_id in (k.module.package_id, '*'):
                for valid_name in (k.full_name, k.full_name_unambiguous, '*'):
                    by_package_lookup[package_id][valid_name].append(v)
                    by_name_lookup[valid_name][package_id].append(v)

        return TypeCache(
            everything,
            _immutable_mmc(by_package_lookup),
            _immutable_mmc(by_name_lookup))

    def lookup(self, package_id: str, type_name: str) -> Collection[T]:
        """
        Look up items based on package ID and type name. The values cannot be ``None``, but they
        can be the special-meaning ``'*'`` value.
        """
        safe_cast(str, package_id)
        safe_cast(str, type_name)

        if package_id == '*':
            candidates = reduce(add, self.by_name_lookup.get(type_name, {}).values(), ())
        elif type_name == '*':
            candidates = reduce(add, self.by_package_lookup.get(package_id, {}).values(), ())
        else:
            candidates = self.by_package_lookup.get(package_id, {}).get(type_name, ())

        return {t.data_type.name.full_name_unambiguous: t for t in candidates}.values()


def _immutable_mmc(mapping: 'Mapping[str, Mapping[str, Collection[T]]]') -> \
        'Mapping[str, Mapping[str, Collection[T]]]':
    """
    Create an immutable copy of :class:`TemplateStoreCache` data structures.
    """
    return MappingProxyType({
        k1: MappingProxyType({k2: tuple(v) for k2, v in v1.items()})
        for k1, v1 in mapping.items()
    })


EMPTY_MAPPING = MappingProxyType({})
EMPTY_TYPE_CACHE = TypeCache((), EMPTY_MAPPING, EMPTY_MAPPING)
