# Copyright (c) 2017-2020 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import sys
import threading
from asyncio import ensure_future, get_event_loop, gather
from concurrent.futures import Future as ConcurrentFuture, ThreadPoolExecutor
from types import MappingProxyType
from typing import Any, Awaitable, Callable, Collection, Dict, Set, TypeVar\

if sys.version_info >= (3, 7):
    from typing import Protocol
else:
    from typing_extensions import Protocol

from ..damlast.daml_lf_1 import Archive, TemplateChoice, Package
from ..model.core import Dar, DazlError
from ..model.lookup import validate_template
from ..model.types import PackageId, PackageIdSet, Type, Template
from ..util.tools import get_matches

T = TypeVar('T')


class _PackageParser:
    """
    Background parser for DAML-LF packages.

    The concurrent API is used here instead of asyncio because DAML-LF parsing is inherently a
    blocking call.

    This _can_ be a global object because DAML-LF package hashes are meant to uniquely identify
    packages, and in contexts where requests to load packages occur frequently, we can save both
    time and memory by parsing any given package ID once for the lifetime of an application.

    This behavior can be overridden by subclassing PackageCache and supplying an alternate
    implementation of this class, though this is not normally recommended or required.
    """

    def __init__(self):
        self._executor = ThreadPoolExecutor(3, thread_name_prefix='dazl-packageparser')
        self._lock = threading.Lock()
        self._package_futures = dict()  # type: Dict[PackageId, ConcurrentFuture]

    def parse(self, package_id: PackageId, archive_bytes: bytes) -> 'ConcurrentFuture':
        """
        Parse a package in a background thread.

        :param package_id:
        :param archive_bytes:
        :return:
        """
        with self._lock:
            fut = self._package_futures.get(package_id)
            if fut is None:
                fut = self._executor.submit(self._parse, package_id, archive_bytes)
                self._package_futures[package_id] = fut
            return fut

    def _parse(self, package_id: PackageId, archive_bytes: bytes) -> 'ConcurrentFuture':
        pass


class SyncPackageService(Protocol):

    def fetch_package_bytes(self, package_id: 'PackageId') -> bytes:
        raise NotImplementedError

    def fetch_package_ids(self) -> 'PackageIdSet':
        raise NotImplementedError


class PackageCache:
    """
    Local cache of packages and mappings to types. This is used extensively by dazl to translate
    complex DAML-LF values back and forth to standard Python types.
    """

    def __init__(self, conn: 'SyncPackageService' = None):
        self._conn = conn
        self._cache = dict()  # type: Dict[PackageId, _PackageIndex]
        self._loading_futs = dict()  # type: Dict[PackageId, Awaitable[Package]]
        self._parsing_futs = dict()  # type: Dict[PackageId, Awaitable[Archive]]
        self._executor = ThreadPoolExecutor(3)

    def set_connection(self, conn):
        self._conn = conn

    async def do_with_retry(self, fn: 'Callable[[PackageCache], T]') -> 'T':
        """
        Perform a synchronous action against the contents of this :class:`PackageCache`. In the
        event of cache misses, the required package/type is fetched and the operation retried again.

        If, after a retry, an expected package or type could not be found, the exception is
        re-raised to the caller.

        :param fn: A function to invoke.
        :return: The result of that function.
        """
        failed_types = set()  # type: Set[str]
        failed_packages = set()  # type: Set[PackageId]
        while True:
            try:
                return fn(self)

            except PackageNotFoundError as ex:
                # every time we fail serialization due to a missing package or type,
                # try to resolve it; remember what we tried, because if we fail again
                # for the same reason it is likely fatal
                if ex.package_id in failed_packages:
                    # we already looked for this package and couldn't find it; this will
                    # never succeed
                    raise
                failed_packages.add(ex.package_id)
                await self.load(ex.package_id)

            except TypeNotFoundError as ex:
                if ex.type_ref in failed_types:
                    # we already looked for this type and couldn't find it; this will
                    # never succeed
                    raise

                pkg_id, _ = validate_template(ex.type_ref)
                if pkg_id == '*':
                    # we don't know what package contains this type, so we have no
                    # choice but to look in all known packages
                    failed_types.add(ex.type_ref)
                    await self.load_all()
                else:
                    # we know what package this type comes from, but it did not contain
                    # the required type
                    raise

    async def preload(self, *contents: 'Dar') -> None:
        """
        Populate a :class:`PackageCache` with types from DARs.

        :param contents:
            One or more DARs to load into a local package cache.
        """

    async def load(self, package_id: 'PackageId') -> 'Package':
        """
        Load a package ID from the remote server. If the package has additional dependencies, they
        are also loaded.

        :param package_id: The package ID to
        :raises: PackageNotFoundError if the package could not be resolved
        """
        # If the package has already been loaded, then skip all the expensive I/O stuff
        index = self._cache.get(package_id)
        if index is not None:
            return index.package

        # If we already have a request in-flight, simply return that same Future to our caller;
        # do not try to schedule a new request
        fut = self._loading_futs.get(package_id)
        if fut is None:
            fut = ensure_future(self._load_and_parse_package(package_id))
            self._loading_futs[package_id] = fut
        package = await fut

        _ = self._loading_futs.pop(package_id, None)
        _ = self._parsing_futs.pop(package_id, None)

        return package

    async def _load_and_parse_package(self, package_id: 'PackageId') -> 'Package':
        from ..protocols.v1.pb_parse_metadata import parse_archive

        loop = get_event_loop()
        conn = self._conn
        if conn is None:
            raise DazlError('a connection is not configured')

        archive_bytes = await loop.run_in_executor(
            self._executor, lambda: conn.fetch_package_bytes(package_id))

        # we only ever want a package to be parsed once; it could be that there were multiple
        # attempts to load a package in flight (though this shouldn't happen either)
        fut = self._parsing_futs.get(package_id)
        if fut is None:
            fut = ensure_future(loop.run_in_executor(
                self._executor, lambda: parse_archive(package_id, archive_bytes)))
            self._parsing_futs[package_id] = fut

        archive = await fut
        index = _PackageIndex(archive.package)
        self._cache[package_id] = index
        return archive.package

    async def load_all(self):
        """
        Load all packages from the remote server.
        """
        loop = get_event_loop()

        package_ids = set(await loop.run_in_executor(self._executor, self._conn.fetch_package_ids))
        package_ids.intersection_update(self._cache)
        if package_ids:
            await gather(*(self.load(package_id) for package_id in package_ids))

    def resolve_type_from_cache(self, type_ref: 'Any') -> 'Type':
        """
        Attempt to resolve a type reference, but strictly from the local cache (will NOT try to
        lazily fetch).

        Because this operation only consults the local cache, it is _not_ an asynchronous call.
        This can be used as an optimization to avoid asynchronous overhead when performance is a
        concern and it is known that types are available locally.

        :param type_ref: The string that represents a type to look for.
        :return: The ``Type``.
        :raises: PackageNotFoundError if the package could not be resolved
        :raises: TypeNotFoundError if the type could not be resolved
        :raises: AmbiguousTypeError if more than one type matches
        """
        types = self.resolve_types_from_cache(type_ref, allow_empty=False)
        if len(types) == 1:
            return next(iter(types))
        else:
            raise AmbiguousTypeError(type_ref)

    def resolve_types_from_cache(self, type_ref: 'Any', allow_empty: bool = True) \
            -> 'Collection[Type]':
        """
        Attempt to resolve type references from the local cache.

        :param type_ref: The string that represents a type to look for.
        :param allow_empty:
            True to return an empty list if no matching type/package could be found;
            False to throw an exception in the event of a missing package or type.
        :return: The ``Type``.
        :raises: PackageNotFoundError if the package could not be resolved
        :raises: TypeNotFoundError if the type could not be resolved (and allow_empty is False)
        :raises: AmbiguousTypeError if more than one type matches
        """
        package_id, name = validate_template(type_ref)

        pkg_not_found_error = None if allow_empty else PackageNotFoundError
        type_not_found_error = None if package_id == '*' else lambda _: TypeNotFoundError(type_ref)

        types = [
            tt
            for archive_index in get_matches(
                self._cache, PackageId(package_id), exc_class=pkg_not_found_error)
            for tt in get_matches(archive_index.types, name, exc_class=type_not_found_error)
        ]
        if not types and not allow_empty:
            raise TypeNotFoundError(type_ref)

        return types

    def resolve_template_from_cache(self, type_ref: 'Any') -> 'Template':
        templates = self.resolve_templates_from_cache(type_ref, allow_empty=False)
        if len(templates) == 1:
            return next(iter(templates))
        raise AmbiguousTypeError(type_ref)

    def resolve_templates_from_cache(self, type_ref: 'Any', allow_empty: bool = True) \
            -> 'Collection[Template]':
        """
        Attempt to resolve references to a template from the local cache.

        :param type_ref: The string that represents a template to look for.
        :param allow_empty:
            True to return an empty list if no matching template/package could be found;
            False to throw an exception in the event of a missing package or type.
        :return: The ``Template``.
        :raises: PackageNotFoundError if the package could not be resolved
        :raises: TypeNotFoundError if the type could not be resolved (and allow_empty is False)
        :raises: AmbiguousTypeError if more than one type matches
        """
        package_id, name = validate_template(type_ref)

        pkg_not_found_error = None if allow_empty else PackageNotFoundError
        type_not_found_error = None if package_id == '*' else lambda _: TypeNotFoundError(type_ref)

        templates = [
            tt
            for archive_index in get_matches(
                self._cache, PackageId(package_id), exc_class=pkg_not_found_error)
            for tt in get_matches(archive_index.templates, name, exc_class=type_not_found_error)
        ]
        if not templates and not allow_empty:
            raise TypeNotFoundError(type_ref)

        return templates

    def resolve_choice_from_cache(self, type_ref: 'Any', choice_name: str) -> 'TemplateChoice':
        """
        Attempt to resolve references to a template from the local cache.

        :param type_ref: The string that represents a template to look for.
        :param choice_name: The name of the choice.
        :return: The ``Template``.
        :raises: PackageNotFoundError if the package could not be resolved
        :raises: TypeNotFoundError if the type could not be resolved (and allow_empty is False)
        :raises: ChoiceNotFoundError if the type could be resolved, but the choice could not
        :raises: AmbiguousTypeError if more than one type matches
        """
        template = self.resolve_template_from_cache(type_ref)
        for choice in template.choices:
            if choice.name == choice_name:
                return choice
        raise ChoiceNotFoundError(type_ref, choice_name)


class PackageNotFoundError(DazlError):
    """
    Raised when a :class:`Package` was expected but could not be found.
    """

    def __init__(self, package_id: 'PackageId'):
        super(package_id)
        self.package_id = package_id


class TypeNotFoundError(DazlError):
    """
    Raised when a :class:`Type` was expected but could not be found.
    """

    def __init__(self, type_ref: str):
        super(type_ref)
        self.type_ref = type_ref


class ChoiceNotFoundError(DazlError):
    def __init__(self, type_ref, choice_name):
        super(f'{type_ref} {choice_name}')
        self.type_ref = type_ref
        self.choice_name = choice_name


class AmbiguousTypeError(DazlError):
    """
    Raised when a single :class:`Type` was expected, but more than one possible match arose.
    """

    def __init__(self, type_ref: str):
        super(type_ref)
        self.type_ref = type_ref


class _PackageIndex:
    """
    A lightweight index on top of a Package that makes looking for individual types, choices, and
    templates within a package slightly faster.

    The dictionaries are indexed by name that already assume a level of nesting withi
    """

    __slots__ = 'package', 'templates', 'values', 'types'

    def __init__(self, package: 'Package'):
        self.package = package
        self.templates = MappingProxyType({
            f'{module.name}:{template.tycon}': template
            for module in package.modules
            for template in module.templates
        })
        self.values = MappingProxyType({
            f'{module.name}:{value.name_with_type.name}': value
            for module in package.modules
            for value in module.values
        })
        self.types = MappingProxyType({
            f'{module.name}:{data_type.name}': data_type
            for module in package.modules
            for data_type in module.data_types
        })
