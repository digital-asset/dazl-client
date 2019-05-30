# Copyright (c) 2019 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import asyncio
import warnings
from asyncio import Future
from collections import defaultdict
from typing import Awaitable, Dict, List, Optional, Union, Collection, cast

from ..client._reader_match import is_match
from ..model.core import ContractId, ContractsState, ContractMatch, \
    UnknownTemplateWarning, ContractContextualData, ContractContextualDataCollection
from ..model.reading import ContractCreateEvent, ContractArchiveEvent
from ..model.types import TypeReference
from ..model.types_store import PackageStore
from ..util.asyncio_util import ContextFreeFuture, safe_create_future, propagate, completed, await_then


class ActiveContractSet:
    def __init__(self):
        self.metadata_future = ContextFreeFuture()
        self._tcdata = defaultdict(TemplateContractData)  # type: Dict[TypeReference, TemplateContractData]

    def handle_create(self, event: ContractCreateEvent) -> None:
        self._tcdata[event.cid.template_id].handle_create(event)

    def handle_archive(self, event: ContractArchiveEvent) -> None:
        self._tcdata[event.cid.template_id].handle_archive(event)

    def get(self, cid: 'Union[str, ContractId]') -> 'Optional[ContractContextualData]':
        """
        Return information for the associated :class:`ContractId`.

        :param cid: Either a ContractId or a string that represents a ContractId.
        :return: Contract information for the specified contract ID.
        """
        tcd = self._tcdata.get(cid.template_id) if isinstance(cid, ContractId) else None
        if tcd is not None:
            return tcd.get(cid)
        else:
            # untyped ContractId lookup, so scan across all templates
            for tcd in self._tcdata.values():
                cxd = tcd.get(cid)
                if cxd is not None:
                    return cxd
            return None

    def read_active(self, template_name: str, match: ContractMatch = None) -> ContractsState:
        return {cxd.cid: cxd.cdata for cxd in self.read_full(template_name, match)}

    def read_full(self,
                  template_name: str,
                  match: ContractMatch = None,
                  include_archived: bool = False) -> ContractContextualDataCollection:
        if not self.metadata_future.done():
            return ContractContextualDataCollection()

        unfiltered = self._get_template_state(self.metadata_future.result(), template_name)
        all_items = [item
                     for tcd in unfiltered.values()
                     for item in tcd.subset(match, include_archived)]
        return ContractContextualDataCollection(all_items)

    def read_async(self, template_name: str, match: ContractMatch = None, min_count: int = 1) \
            -> Awaitable[ContractsState]:
        if self.metadata_future.done():
            unfiltered = self._get_template_state(self.metadata_future.result(), template_name)
            if len(unfiltered) > 1:
                warnings.warn('Wildcard searches are not supported on async ACS queries',
                              UnknownTemplateWarning, stacklevel=3)
                unfiltered = dict()  # type: Dict[TypeReference, TemplateContractData]

            if len(unfiltered) == 0:
                # TODO: A slightly smarter implementation could hang around until/if a matching
                #  template shows up
                return completed({})

            (tt, tcd), = unfiltered.items()

            query = PendingQuery(asyncio.get_event_loop(), match, min_count)
            # if the current state is already a match, then don't remember the query since we're
            # already done
            if tcd is None or not query.check_ready(tcd):
                tcd.register_query(query)

            return await_then(query.future, lambda cxds: {cxd.cid: cxd.cdata for cxd in cxds})
        else:
            # delay the invocation of this entire method call until metadata is made available to us
            future = safe_create_future()

            def delayed_invoke(_):
                propagate(
                    asyncio.ensure_future(self.read_async(template_name, match, min_count)), future)

            self.metadata_future.add_done_callback(delayed_invoke)
            return future

    def _get_template_state(self, store: PackageStore, template_name: str) -> \
            'Dict[TypeReference, TemplateContractData]':
        matching_templates = store.resolve_template_type(template_name)
        if matching_templates:
            return {tt: self._tcdata[tt] for tt in matching_templates}
        else:
            warnings.warn(f'Unknown template name: {template_name}', UnknownTemplateWarning,
                          stacklevel=4)
            return {}


class TemplateContractData:
    """
    Storage for state related to a specific :class:`Template`.
    """
    def __init__(self):
        # raw ContractId to ContractContextualData
        self._data = dict()  # type: Dict[str, ContractContextualData]
        # outstanding ACS queries
        self._queries = list()  # type: List[PendingQuery]

    def handle_create(self, event: ContractCreateEvent) -> None:
        self._data[event.cid.contract_id] = ContractContextualData(
            cid=event.cid,
            cdata=event.cdata,
            effective_at=event.time,
            archived_at=None,
            active=True)

        self._queries = [q for q in self._queries if not q.check_ready(self)]

    def handle_archive(self, event: ContractArchiveEvent) -> None:
        self._data[event.cid.contract_id] = ContractContextualData(
            cid=event.cid,
            cdata=None,
            effective_at=self._data[event.cid.contract_id].effective_at,
            archived_at=event.time,
            active=False)

    def get(self, cid: 'Union[str, ContractId]') -> 'Optional[ContractContextualData]':
        if isinstance(cid, ContractId):
            cid = cid.contract_id
        return self._data.get(cid)

    def subset(self, match: 'ContractMatch', include_archived: bool) -> 'Collection[ContractContextualData]':
        return [cxd for cxd in self._data.values()
                if (include_archived or cxd.active)
                and is_match(match, cxd.cdata)]

    def register_query(self, query: 'PendingQuery') -> None:
        self._queries.append(query)


class PendingQuery:
    def __init__(self, loop, match, min_count: int):
        self.future = loop.create_future()  # type: Awaitable[Collection[ContractContextualData]]
        self.match = match
        self.min_count = min_count

    def check_ready(self, tcd: 'TemplateContractData') -> bool:
        matches = tcd.subset(self.match, False)
        if len(matches) >= self.min_count:
            cast(Future, self.future).set_result(matches)
            return True
        else:
            return False
