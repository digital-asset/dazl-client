# Copyright (c) 2019 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import asyncio
import copy
import itertools
import functools

from asyncio import Future
from collections import defaultdict
from functools import partial
from io import StringIO
from typing import Any, Callable, Tuple, Dict

from .. import LOG
from ..client import LedgerClientManager, ParticipantLedgerClient
from ..util.tools import flatten
from ..model.reading import TransactionStartEvent
from ..plugins import Plugin

from .appbuilder import Application
from .builtins import BUILTIN_AND
from .visitor_eval import generate_lambda
from .visitor_pretty import pretty_print
from .expr_base import TRIGGER_ON_INIT
from .expr_impl import and_, AppExpr
from .expr_util import get_distinct_templates, get_distinct_aliases


class ApplicationContext(Plugin):
    """
    Manages the lifetime of a running Application.
    """
    def __init__(self, application):
        self.suite_contexts = tuple(map(SuiteContext, application.suites))

    def install(self, manager):
        for suite_context in self.suite_contexts:
            suite_context.register_into(manager.client(suite_context.party))


class SuiteContext:
    """
    Manages the lifetime of a suite of programs associated with a single party.
    """
    def __init__(self, suite, loop=None):
        self.loop = loop or asyncio.get_event_loop()
        self.suite = suite
        self.client = None

    @property
    def party(self):
        return self.suite.party

    def _init_ready(self, program):
        def _invoke_init_program(party, client):
            return generate_lambda(program.update)(dict())
        return _invoke_init_program

    def register_into(self, client: ParticipantLedgerClient):
        self.client = client

        for program in self.suite.programs:
            # init programs with no preconditions runs first
            if program.trigger == TRIGGER_ON_INIT and program.select is None:
                # these special programs run with the trivial initial state
                client.on_ready(self._init_ready(program))
            else:
                # these special programs are supposed to only when crossing a boundary of a
                # pre-state not matching and post-state matching
                # TODO: Proper implementation; this implementation is too aggressive
                template_refs = get_distinct_templates(program)
                if not template_refs:
                    LOG.error('A program somehow referenced no templates: %r', program)

                runner = Runner(self.loop, self.client, program, flatten(template_refs.values()))
                client.on_event('transaction-start', runner.start_transaction)
                for template_ref, aliases in template_refs.items():
                    client.on_event(template_ref, runner.state_updater(aliases))
                client.on_event('transaction-end', runner.end_transaction)
                client.on_done(runner.log_post_checks)

                # have the program force the application to stay alive if it is an `init` program
                client._keepalive.wait_for_future(runner.run(), keep_alive=program.trigger == TRIGGER_ON_INIT)


def register_application(client_manager: LedgerClientManager, application: Application):
    """
    Install listeners into clients managed by a `LedgerClientManager` that allow for
    starting an application.
    """
    client_manager.register(ApplicationContext(application))


def trivial_future(loop, result='TRIVIAL_FUTURE'):
    future = loop.create_future()
    future.set_result(result)
    return future


class _TransactionBuilder:
    __slots__ = ('bim', 'events')

    def __init__(self):
        self.bim = None
        self.events = []

    def build(self):
        return _Transaction(self.bim, self.events)


class _Transaction:
    __slots__ = ('bim', 'events')

    def __init__(self, bim, events):
        self.bim = bim
        self.events = tuple(events)


class ProgramMetrics:
    """
    Metrics on a running program.
    """
    __slots__ = ('trigger_count', 'update_count')

    def __init__(self):
        self.trigger_count = 0
        self.update_count = 0


class _ProgramState:
    """
    Tracks all state required by a running program.
    """
    def __init__(self, loop, client, program, state_predicate_fn, defined_aliases):
        self.loop = loop
        self.client = client
        self._program = program

        self._state_predicate_fn = state_predicate_fn
        self._update_fn = generate_lambda(program.update)
        self._state = {alias: dict() for alias in defined_aliases}
        self._current_command = None
        self.metrics = ProgramMetrics()
        self._error = None

    def apply_transaction(self, tx: _Transaction) -> bool:
        """
        Applies the state as necessary and submits the corresponding update to the server.

        :return:
            ``True`` generally; ``False`` if the state of the program dictates that it needs to
            terminate.
        """
        # TODO: Holy moly, what a hack.
        # This essentially stops `init`-based programs from being retriggered once their initial
        # entry criteria have been met.
        if self._program.trigger == TRIGGER_ON_INIT and self.metrics.update_count:
            self._current_command = None
            return False

        if self._error is not None:
            return False

        for alias, cid, cdata in tx.events:
            if cdata is not None:
                self._state[alias][cid] = cdata
            else:
                self._state[alias].pop(cid, None)

        self._attempt_submit()
        return True

    def _attempt_submit(self):
        if self._current_command is None or self._current_command.done():
            self._current_command = None
            self.metrics.trigger_count += 1
            update = self.compute_update()
            if update:
                # TODO: questionable...
                if self._program.trigger == TRIGGER_ON_INIT and self.metrics.update_count:
                    return

                self.metrics.update_count += 1

                self._current_command = self.client.submit(update)
                self._current_command.state_snapshot = copy.deepcopy(self._state)
                self._current_command.update_command = update
                self._current_command.add_done_callback(self._check_for_errors)

    def _check_for_errors(self, future):
        try:
            if future.exception() is not None:
                self._error = True
                with StringIO() as buf:
                    try:
                        buf.write('Failed to execute a program!\n')
                        self.write_state(snapshot=future.state_snapshot, buf=buf)
                        buf.write('\nProposed Update:\n')
                        buf.write(str(future.update_command))
                        buf.write('\nServer Error\n')
                        buf.write(repr(future.exception()))
                        LOG.error(buf.getvalue())
                    finally:
                        LOG.exception("Failed to log an exception!")
        except:
            LOG.exception('Error when trying to process an error result.')

    def compute_update(self):
        """
        Computes the fully-realized update block from the current state.
        """
        return compute_update(self._state, self._state_predicate_fn, self._update_fn)

    def write_state(self, snapshot=None, buf=None):
        if buf is None:
            buf = StringIO()
        if snapshot is None:
            snapshot = self._state

        buf.write('Program:\n')
        buf.write(pretty_print(self._program))
        buf.write('\nState:\n')
        for alias, data in snapshot.items():
            buf.write('  {} ({} item(s))\n'.format(alias, len(data)))
            for cid, cdata in data.items():
                buf.write('    ')
                buf.write(str(cid))
                buf.write(' ')
                buf.write(str(cdata))
                buf.write('\n')
        return buf

    def log_post_checks(self):
        """
        Log warnings based on operations that have (or more helpfully, have NOT) been performed.
        """
        if self.metrics.update_count == 0:
            # this is almost certainly a problem; there is no use for a program that never produces
            # an update
            LOG.warning('The program %r for party %r never produced an update!', self._program.name, self.client.party_name)
            LOG.warning('  update count: %r', self.metrics.update_count)
            LOG.warning('  trigger count: %r', self.metrics.trigger_count)
            with StringIO() as buf:
                self.write_state(buf=buf)
                LOG.warning(buf.getvalue())
        if self._current_command is not None and not self._current_command.done():
            LOG.warning('The program %r for party %r is stuck waiting for an update!', self._program.name, self.client.party_name)
            LOG.warning('  stuck command: %r', self._current_command)
            LOG.warning('  update count: %r', self.metrics.update_count)
            LOG.warning('  trigger count: %r', self.metrics.trigger_count)
            with StringIO() as buf:
                self.write_state(buf=buf)
                LOG.warning(buf.getvalue())

    def __repr__(self):
        return f'<_ProgramState(name={self.client.party_name})>'


# Filters that are applied on the full state tracked by a program.
#
# This is a function that takes one row of the full state of a program and returns whether the row
# should be considered part of the state.
StateFilter = Callable[[Dict[str, Tuple[Any, Any]]], bool]

# Filters that are applied before data is applied to the state tracked by a program over
# a subset of the data.
#
# This is a dictionary whose keys are aliases and values are functions that take a state, assumed
# to only contain one alias for the (cid, cdata) tuple and return whether the (cid, cdata) is valid
# to include in the state.
PreFilter = Dict[str, StateFilter]


def tautology(state):
    return True


def compute_filters(root_predicate: Any) -> Tuple[PreFilter, StateFilter]:
    if isinstance(root_predicate, AppExpr) and root_predicate.func == BUILTIN_AND:
        # We currently only compute pre-filters on top-level AND expressions that are functions
        # of exclusively one alias. All other expressions are pushed off to a post-filter,
        # which is more expensive.
        pre_filter_predicates = defaultdict(list)
        post_filter_predicates = []
        for child in root_predicate.args:
            aliases = get_distinct_aliases(child)
            if len(aliases) == 1:
                alias, = aliases
                pre_filter_predicates[alias].append(child)
            else:
                post_filter_predicates.append(child)

        pre_filters = {alias: generate_lambda(and_(*predicates))
                       for alias, predicates in pre_filter_predicates.items() if predicates}
        post_filter = generate_lambda(and_(*post_filter_predicates)) if post_filter_predicates else tautology
    else:
        # can't optimize this expression further
        pre_filters = dict()
        post_filter = generate_lambda(root_predicate)

    return pre_filters, post_filter


class Runner:
    """
    Manages processing events and dispatching commands on behalf of a program.
    """

    def __init__(self, loop, client, program, defined_aliases):
        self.pre_filters, self.post_filter = compute_filters(program.select.predicate)

        self._state = _ProgramState(loop, client, program, self.post_filter, defined_aliases)
        self._work_queue = asyncio.Queue(loop=loop)
        self._current_tx = None
        self.future = loop.create_future()

    def state_updater(self, aliases) -> Callable[[Any, Any], None]:
        """
        Return a function that is suitable as a callback to the underlying event stream. On each
        invocation, the (cid, cdata) tuple associated with the event is applied under the specified
        aliases.
        """
        # TODO: A future iteration of this could then selectively apply state updates that match
        # the filter instead of eagerly adding state for all aliases, always
        return partial(self.on_update, aliases)

    def start_transaction(self, _, tdata: TransactionStartEvent):
        # TODO: Framework support for more easily disconnecting event handlers
        if self.future.done():
            return

        self._current_tx = _TransactionBuilder()
        self._current_tx.bim = tdata.command_id

    def on_update(self, aliases, cid, cdata):
        # TODO: Framework support for more easily disconnecting event handlers
        if self.future.done():
            return

        # knock out any data that is not relevant for the resultant cross-product
        for alias in aliases:
            pre_filter_fn = self.pre_filters.get(alias)
            if pre_filter_fn is not None and cdata is not None:
                if not pre_filter_fn({alias: (cid, cdata)}):
                    return

        if self._current_tx is not None:
            self._current_tx.events.extend((alias, cid, cdata) for alias in aliases)
        else:
            LOG.warning('Received an event %s %s outside the context of a transaction!', cid, cdata)

    def end_transaction(self, _, __):
        # TODO: Framework support for more easily disconnecting event handlers
        if self.future.done():
            return

        if self._current_tx is None:
            raise Exception(f'Program {self._state._program.name} callbacks were called out of order!')

        tx = self._current_tx.build()
        self._current_tx = None
        if not self._state.apply_transaction(tx):
            if isinstance(self._state._error, Exception):
                self.future.set_exception(self._state._error)
            elif self._state._error is not None:
                self.future.set_exception(Exception(self._state._error))
            else:
                self.future.set_result(None)

        # self._work_queue.put_nowait(functools.partial(self._state.apply_transaction, tx))

    # def end_block(self, _, __):
    #     # TODO: Framework support for more easily disconnecting event handlers
    #     if self.future.done():
    #         return
    #
    #     # TODO: Why is this needed? _is_ this needed?
    #     self._state._attempt_submit()

    def log_post_checks(self):
        """
        Log warnings based on operations that have (or more helpfully, have NOT) been performed.
        """
        self._state.log_post_checks()

    def run(self) -> Future:
        """
        Return a ``Future`` that completes when the runner has fulfilled all of its work. This
        ``Future`` only completes naturally for `init()`-style programs.
        """
        return self.future


def compute_update(state, predicate_fn, update_fn):
    """
    Creates a list of Ledger API update commands on the given state, filtered by the predicate.

    :param state:
        A dictionary whose keys are aliases and values are dict of cid -> cdata.
    :param predicate_fn:
        A function that, given a state row, returns `True` if the state row is to be considered.
    :param update_fn:
        A function that, given a state row, returns a list of updates.
    """
    pred = functools.partial(filter, predicate_fn)
    cmder = functools.partial(map, update_fn)

    follow_ups = []
    for commands in cmder(pred(projection_iter(state))):
        follow_ups.extend(commands)
    return follow_ups


def projection_iter(state):
    """
    Project a state dict (aliases -> (cid -> cdata)) to the full cross product of all matching
    sub-records.

    :return:
        An iterator over `{alias:row}` for each possible result set derivable from the given state.
    """
    result_set = itertools.product(*[x.items() for x in state.values()])
    for result in result_set:
        yield dict(zip(state.keys(), result))
