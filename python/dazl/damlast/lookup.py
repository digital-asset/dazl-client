# Copyright (c) 2017-2021 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""
DAML-LF fast lookups
--------------------
"""

# Implementation notes:
#
# The code in here is fairly monotonous and boilerplate heavy. However, being too creative here can
# potentially lead to performance degradations, particularly at application startup where type and
# template lookups by name are very frequent. Please be conscious of the runtime costs of
# modifications in this file!

import threading
from types import MappingProxyType
from typing import Any, Collection, Dict, NoReturn, Iterable, Optional, Tuple, AbstractSet

from .daml_lf_1 import Archive, DefDataType, DefValue, DefTemplate, DottedName, ModuleRef, \
    PackageRef, TemplateChoice, TypeConName, ValName, Package
from .errors import NameNotFoundError, PackageNotFoundError
from .protocols import SymbolLookup
from ..model.lookup import validate_template

__all__ = [
    'find_choice', 'parse_type_con_name', 'EmptyLookup', 'PackageLookup', 'MultiPackageLookup'
]


def parse_type_con_name(val: str) -> 'TypeConName':
    """
    Parse the given string as a type constructor.
    """
    # TODO: validate_template should be deprecated and some of its remaining bits be moved in-line
    #  but it's used too heavily in its current form at the moment. This is a local import to avoid
    #  import cycles between dazl.damlast and dazl.model.
    from ..model.lookup import validate_template

    pkg, name = validate_template(val)
    module_name, _, entity_name = name.rpartition(':')
    module_ref = ModuleRef(pkg, DottedName(module_name.split('.')))
    return TypeConName(module_ref, entity_name.split('.'))


def empty_lookup_impl(ref: 'Any') -> 'NoReturn':
    pkg, _ = validate_template(ref)
    if pkg != '*':
        raise PackageNotFoundError(pkg)
    else:
        raise NameNotFoundError(ref)


class EmptyLookup(SymbolLookup):
    """
    A :class:`SymbolLookup` that trivially throws for all of its functions.

    This can be used where a :class:`SymbolLookup` instance is useful but an implementation is not
    required.

    All methods are implemented such that if the provided ref has a package ID,
    :class:`PackageNotFoundError` is thrown; otherwise, :class:`NameNotFoundError` is thrown.
    """

    __slots__ = ()

    def data_type_name(self, ref: 'Any') -> 'NoReturn':
        return empty_lookup_impl(ref)

    def data_type(self, ref: 'Any') -> 'NoReturn':
        return empty_lookup_impl(ref)

    def value(self, ref: 'Any') -> 'NoReturn':
        return empty_lookup_impl(ref)

    def template_name(self, ref: 'Any') -> 'NoReturn':
        return empty_lookup_impl(ref)

    def template(self, ref: 'Any') -> 'NoReturn':
        return empty_lookup_impl(ref)


class PackageLookup(SymbolLookup):
    """
    Caching structure to make lookups on type names within a :class:`Package` faster.
    """

    def __init__(self, archive: 'Archive'):
        self.archive = archive

        data_types = {}  # type: Dict[str, Tuple[TypeConName, DefDataType]]
        values = {}  # type: Dict[str, Tuple[ValName, DefValue]]
        templates = {}  # type: Dict[str, Tuple[TypeConName, DefTemplate]]
        for module in self.archive.package.modules:
            module_ref = ModuleRef(archive.hash, module.name)

            for dt in module.data_types:
                dt_name = TypeConName(module_ref, dt.name.segments)
                data_types[f'{module.name}:{dt.name}'] = (dt_name, dt)

            for value in module.values:
                value_name = ValName(module_ref, value.name_with_type.name)
                values[f'{module.name}:{value.name_with_type.name}'] = (value_name, value)

            for tmpl in module.templates:
                tmpl_name = TypeConName(module_ref, tmpl.tycon.segments)
                templates[f'{module.name}:{tmpl.tycon}'] = (tmpl_name, tmpl)

        self._data_types = MappingProxyType(data_types)
        self._values = MappingProxyType(values)
        self._templates = MappingProxyType(templates)

    def archives(self) -> 'Collection[Archive]':
        return [self.archive]

    def package_ids(self) -> 'AbstractSet[PackageRef]':
        return frozenset([self.archive.hash])

    def data_type_name(self, ref: 'Any') -> 'TypeConName':
        pkg, name = validate_template(ref)
        if pkg == self.archive.hash or pkg == '*':
            dt_name = self.local_data_type_name(name)
            if dt_name is not None:
                return dt_name

        raise NameNotFoundError(ref)

    def data_type(self, ref: 'Any') -> 'DefDataType':
        pkg, name = validate_template(ref)
        if pkg == self.archive.hash or pkg == '*':
            dt = self.local_data_type(name)
            if dt is not None:
                return dt

        raise NameNotFoundError(ref)

    def local_data_type_name(self, name: str) -> 'Optional[TypeConName]':
        r = self._data_types.get(name)
        return r[0] if r is not None else None

    def local_data_type(self, name: str) -> 'Optional[DefDataType]':
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

    def value(self, ref: 'Any') -> 'DefValue':
        pkg, name = validate_template(ref)
        if pkg == self.archive.hash or pkg == '*':
            dt = self.local_value(name)
            if dt is not None:
                return dt

        raise NameNotFoundError(ref)

    def local_value(self, name: str) -> 'Optional[DefValue]':
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

    def template_names(self, ref: 'Any') -> 'Collection[TypeConName]':
        pkg, name = validate_template(ref)
        if pkg == self.archive.hash or pkg == '*':
            if name == '*':
                return self.local_template_names()
            elif name in self._templates:
                n, _ = self._templates.get(name)
                return n
        return []

    def template_name(self, ref: 'Any') -> 'TypeConName':
        pkg, name = validate_template(ref)
        if pkg == self.archive.hash or pkg == '*':
            tmpl = self.local_template_name(name)
            if tmpl is not None:
                return tmpl

        raise NameNotFoundError(ref)

    def template(self, ref: 'Any') -> 'DefTemplate':
        pkg, name = validate_template(ref)
        if pkg == self.archive.hash or pkg == '*':
            tmpl = self.local_template(name)
            if tmpl is not None:
                return tmpl

        raise NameNotFoundError(ref)

    def local_template_names(self) -> 'Collection[TypeConName]':
        return [n for n, _ in self._templates.values()]

    def local_template_name(self, name: str) -> 'Optional[TypeConName]':
        r = self._templates.get(name)
        return r[0] if r is not None else None

    def local_template(self, name: str) -> 'Optional[DefTemplate]':
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
        r = self._templates.get(name)
        return r[1] if r is not None else None


class MultiPackageLookup(SymbolLookup):
    """
    Combines lookups across multiple archives.
    """

    def __init__(self, archives: 'Optional[Collection[Archive]]' = None):
        self._lock = threading.Lock()
        self._cache = {}  # type: Dict[PackageRef, PackageLookup]
        if archives is not None:
            self.add_archive(*archives)

    def archives(self) -> 'Collection[Archive]':
        """
        Return the list of known archives.
        """
        return [lookup.archive for lookup in self._cache.values()]

    def add_archive(self, *a: 'Archive') -> None:
        """
        Add one or more :class:`Archive`s to this lookup.

        This method is thread-safe, but note that :class:`MultiPackageLookup` allows dirty reads for
        performance reasons.

        :param a: One or more :class:`Archive`s to add.
        """
        new_lookups = {ar.hash: PackageLookup(ar) for ar in a}
        with self._lock:
            # replace the old cache with a new one, incorporating values from both the existing
            # cache and the new lookups that came in. When there is a key conflict between the two
            # APIs, always prefer the existing cache to provide stability to callers.
            self._cache = {**new_lookups, **self._cache}

    def package_ids(self) -> 'AbstractSet[PackageRef]':
        return set(self._cache)

    def package(self, ref: 'PackageRef') -> 'Package':
        lookup = self._cache.get(ref)
        if lookup is not None:
            return lookup.archive.package

        raise PackageNotFoundError(ref)

    def data_type_name(self, ref: 'Any') -> 'TypeConName':
        pkg, name = validate_template(ref)
        for lookup in self._lookups(pkg):
            dt_name = lookup.local_data_type_name(name)
            if dt_name is not None:
                return dt_name

        raise NameNotFoundError(ref)

    def data_type(self, ref: 'Any') -> 'DefDataType':
        pkg, name = validate_template(ref)
        for lookup in self._lookups(pkg):
            dt = lookup.local_data_type(name)
            if dt is not None:
                return dt

        raise NameNotFoundError(ref)

    def value(self, ref: 'Any') -> 'DefValue':
        pkg, name = validate_template(ref)
        for lookup in self._lookups(pkg):
            val = lookup.local_value(name)
            if val is not None:
                return val

        raise NameNotFoundError(ref)

    def template_names(self, ref: 'Any') -> 'Collection[TypeConName]':
        names = []

        pkg, name = validate_template(ref)
        for lookup in self._lookups(pkg):
            if name == '*':
                names.extend(lookup.local_template_names())
            else:
                n = lookup.local_template_name(name)
                if n is not None:
                    names.append(n)

        return names

    def template_name(self, ref: 'Any') -> 'TypeConName':
        pkg, name = validate_template(ref)
        for lookup in self._lookups(pkg):
            n = lookup.local_template_name(name)
            if n is not None:
                return n

        raise NameNotFoundError(ref)

    def template(self, ref: 'Any') -> 'DefTemplate':
        pkg, name = validate_template(ref)
        for lookup in self._lookups(pkg):
            tmpl = lookup.local_template(name)
            if tmpl is not None:
                return tmpl

        raise NameNotFoundError(ref)

    def _lookups(self, ref: 'PackageRef') -> 'Iterable[PackageLookup]':
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
        if ref == '*':
            return self._cache.values()

        lookup = self._cache.get(ref)
        if lookup is not None:
            return lookup,

        raise PackageNotFoundError(ref)


def find_choice(template: 'DefTemplate', name: str) -> 'TemplateChoice':
    """
    Find a choice in a :class:`DefTemplate`. If the choice could not be found,
    :class:`NameNotFoundError` is raised.
    """
    for choice in template.choices:
        if choice.name == name:
            return choice

    raise NameNotFoundError(f'choice {name}')
