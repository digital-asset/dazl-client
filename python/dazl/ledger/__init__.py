# Copyright (c) 2017-2022 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
"""
This module contains the types needed to submit commands to and read events from a
Daml `gRPC Ledger API <https://docs.daml.com/app-dev/ledger-api.html>`_ or
`HTTP JSON API <https://docs.daml.com/json-api/index.html>`_.
"""
import sys

from .api_types import (
    ActAs,
    Admin,
    ArchiveEvent,
    Boundary,
    Command,
    CommandMeta,
    CreateAndExerciseCommand,
    CreateCommand,
    CreateEvent,
    Event,
    EventOrBoundary,
    ExerciseByKeyCommand,
    ExerciseCommand,
    ExerciseResponse,
    MeteringReport,
    PartyInfo,
    ReadAs,
    Right,
    SubmitResponse,
    User,
)

if sys.version_info >= (3, 8):
    from typing import Protocol, runtime_checkable
else:
    from typing_extensions import Protocol, runtime_checkable


__all__ = [
    "aio",
    "ActAs",
    "Admin",
    "ArchiveEvent",
    "Boundary",
    "Command",
    "CommandMeta",
    "CreateAndExerciseCommand",
    "CreateCommand",
    "CreateEvent",
    "Event",
    "EventOrBoundary",
    "ExerciseByKeyCommand",
    "ExerciseCommand",
    "ExerciseResponse",
    "MeteringReport",
    "PartyInfo",
    "PackageService",
    "ReadAs",
    "Connection",
    "QueryStream",
    "User",
]


# noinspection PyShadowingNames
def connect(*, blocking=False, **kwargs):
    """
    Create a connection from the supplied parameters.

    See the `documentation for this function
    <https://digital-asset.github.io/dazl-client/dazl.ledger.html#dazl.ledger.connect>`_ for more
    details on the parameters it takes and how values are defaulted.
    """
    from .config import Config
    from .grpc.conn_aio import Connection as GrpcConnection

    if blocking:
        from .blocking._aiowrapper import ConnectionThunk

        return ConnectionThunk(lambda: GrpcConnection(Config.create(**kwargs)))
    else:
        cfg = Config.create(**kwargs)
        conn = GrpcConnection(cfg)

    return conn


class PackageService(Protocol):
    """
    Protocol that describe a service that provides package information. The :class:`Connection`
    protocol extends this interface.
    """

    def get_package(self, __package_id):
        """
        Given a package ID, fetch the binary data for the corresponding DALF.

        :param __package_id:
            The package ID of the DALF to retrieve.

            Note that future versions reserve the right to rename this parameter name at any
            time; it should be passed in as a positional parameter and never by name.
        :return:
            The byte array contents of the DALF associated with the package ID.
        """
        raise NotImplementedError

    def list_package_ids(self):
        """
        Fetch a list of all known package IDs.
        """
        raise NotImplementedError


@runtime_checkable
class Connection(PackageService, Protocol):
    """
    Protocol that describes a connection to a ledger. You will typically work with the more specific
    protocols :class:`dazl.ledger.aio.Connection` or :class:`dazl.ledger.blocking.Connection` that
    are tailored towards connections with ``asyncio`` or thread-blocking semantics, respectively.
    """

    @property
    def config(self):
        """
        Get the configuration that created this connection.

        Under certain circumstances (notably, OAuth token refreshing), fields of this configuration
        object are modifiable after the connection has been created; see the documentation for
        :class:`dazl.ledger.config.Config` for more information.
        """
        raise NotImplementedError

    @property
    def codec(self):
        """
        Get the object that provides conversion to over-the-wire types for this connection.

        The specific object here is transport-specific.
        """
        raise NotImplementedError

    @property
    def is_closed(self):
        """
        Return whether the connection is closed.
        """
        raise NotImplementedError

    def open(self):
        """
        Prepares the connection for being used, including possibly fetching the ledger ID if it is
        not yet known.

        On *asynchronous* connections, this method is a coroutine.

        On *blocking* connections, this method blocks the current thread until a connection is
        ready.
        """
        raise NotImplementedError

    def close(self):
        """
        Close the connection.

        On _asynchronous_ connections, this method is a coroutine.

        On _blocking_ connections, this method blocks the current thread until the connection is
        closed and all network activity has stopped.
        """
        raise NotImplementedError

    def submit(
        self,
        __commands,
        *,
        workflow_id=None,
        command_id=None,
        read_as=None,
        act_as=None,
    ):
        """
        Submit one or more commands to the Ledger API.

        You should generally prefer trying to use :meth:`create`, :meth:`exercise`,
        :meth:`exercise_by_key`, or :meth:`create_and_exercise`, as they are available over both
        the gRPC Ledger API and HTTP JSON API; additionally those methods can provide more
        information about what happened.

        This method can be used to submit multiple disparate commands as a single transaction, but
        if you find yourself needing to do this, you may want to consider moving more of your logic
        into Daml so that only a single command is needed from the outside in order to satisfy your
        use case.

        On *asynchronous* connections, this method is a coroutine.

        On *blocking* connections, this method blocks the current thread until the connection is
        closed and all network activity has stopped.

        :param __commands:
            A command or sequence of commands to submit to the ledger.

            Note that future versions reserve the right to rename this parameter name at any
            time; it should be passed in as a positional parameter and never by name.
        :param workflow_id:
            An optional workflow ID.
        :param command_id:
            An optional command ID. If unspecified, a random one will be created.
        :param read_as:
            An optional set of read-as parties to use to submit this command. Note that for a
            ledger with authorization, these parties must be a subset of the parties in the token.
        :param act_as:
            An optional set of act-as parties to use to submit this command. Note that for a
            ledger with authorization, these parties must be a subset of the parties in the token.
        """
        raise NotImplementedError

    def create(
        self,
        __template_id,
        __payload,
        *,
        workflow_id=None,
        command_id=None,
        read_as=None,
        act_as=None,
    ):
        """
        Create a contract for a given template.

        :param __template_id:
            The template of the contract to be created.

            Note that future versions reserve the right to rename this parameter name at any
            time; it should be passed in as a positional parameter and never by name.
        :param __payload:
            Template arguments for the contract to be created.

            Note that future versions reserve the right to rename this parameter name at any
            time; it should be passed in as a positional parameter and never by name.
        :param workflow_id:
            An optional workflow ID.
        :param command_id:
            An optional command ID. If unspecified, a random one will be created.
        :param read_as:
            An optional set of read-as parties to use to submit this command. Note that for a
            ledger with authorization, these parties must be a subset of the parties in the token.
        :param act_as:
            An optional set of act-as parties to use to submit this command. Note that for a
            ledger with authorization, these parties must be a subset of the parties in the token.
        :return:
            The :class:`CreateEvent` that represents the contract that was successfully created.
        """
        raise NotImplementedError

    def exercise(
        self,
        __contract_id,
        __choice_name,
        __argument,
        *,
        workflow_id=None,
        command_id=None,
        read_as=None,
        act_as=None,
    ):
        """
        Exercise a choice on a contract identified by its contract ID.

        :param __contract_id:
            The contract ID of the contract to exercise.

            Note that future versions reserve the right to rename this parameter name at any
            time; it should be passed in as a positional parameter and never by name.
        :param __choice_name:
            The name of the choice to exercise.

            Note that future versions reserve the right to rename this parameter name at any
            time; it should be passed in as a positional parameter and never by name.
        :param __argument:
            The choice arguments. Can be omitted for choices that take no argument.

            Note that future versions reserve the right to rename this parameter name at any
            time; it should be passed in as a positional parameter and never by name.
        :param workflow_id:
            An optional workflow ID.
        :param command_id:
            An optional command ID. If unspecified, a random one will be created.
        :param read_as:
            An optional set of read-as parties to use to submit this command. Note that for a
            ledger with authorization, these parties must be a subset of the parties in the token.
        :param act_as:
            An optional set of act-as parties to use to submit this command. Note that for a
            ledger with authorization, these parties must be a subset of the parties in the token.
        :return:
            The return value of the choice, together with a list of events that occurred as a result
            of exercising the choice.
        """
        raise NotImplementedError

    def create_and_exercise(
        self,
        __template_id,
        __payload,
        __choice_name,
        __argument=None,
        *,
        workflow_id=None,
        command_id=None,
        read_as=None,
        act_as=None,
    ):
        """
        Exercise a choice on a newly-created contract, in a single transaction.

        :param __template_id:
            The template of the contract to be created (positional argument only).

            Note that future versions reserve the right to rename this parameter name at any
            time; it should be passed in as a positional parameter and never by name.
        :param __payload:
            Template arguments for the contract to be created (positional argument only).

            Note that future versions reserve the right to rename this parameter name at any
            time; it should be passed in as a positional parameter and never by name.
        :param __choice_name:
            The name of the choice to exercise (positional argument only).

            Note that future versions reserve the right to rename this parameter name at any
            time; it should be passed in as a positional parameter and never by name.
        :param __argument:
            The choice arguments. Can be omitted for choices that take no argument (positional
            argument only).

            Note that future versions reserve the right to rename this parameter name at any
            time; it should be passed in as a positional parameter and never by name.
        :param workflow_id:
            An optional workflow ID.
        :param command_id:
            An optional command ID. If unspecified, a random one will be created.
        :param read_as:
            An optional set of read-as parties to use to submit this command. Note that for a
            ledger with authorization, these parties must be a subset of the parties in the token.
        :param act_as:
            An optional set of act-as parties to use to submit this command. Note that for a
            ledger with authorization, these parties must be a subset of the parties in the token.
        :return:
            The return value of the choice, together with a list of events that occurred as a result
            of exercising the choice.
        """
        raise NotImplementedError

    def exercise_by_key(
        self,
        __template_id,
        __choice_name,
        __key,
        __argument,
        *,
        workflow_id=None,
        command_id=None,
        read_as=None,
        act_as=None,
    ):
        """
        Exercise a choice on a contract identified by its contract key.

        :param __template_id:
            The template of the contract to be created (positional argument only).

            Note that future versions reserve the right to rename this parameter name at any
            time; it should be passed in as a positional parameter and never by name.
        :param __choice_name:
            The name of the choice to exercise.

            Note that future versions reserve the right to rename this parameter name at any
            time; it should be passed in as a positional parameter and never by name.
        :param __key:
            The key of the contract to exercise.

            Note that future versions reserve the right to rename this parameter name at any
            time; it should be passed in as a positional parameter and never by name.
        :param __argument:
            The choice arguments. Can be omitted for choices that take no argument.

            Note that future versions reserve the right to rename this parameter name at any
            time; it should be passed in as a positional parameter and never by name.
        :param workflow_id:
            An optional workflow ID.
        :param command_id:
            An optional command ID. If unspecified, a random one will be created.
        :param read_as:
            An optional set of read-as parties to use to submit this command. Note that for a
            ledger with authorization, these parties must be a subset of the parties in the token.
        :param act_as:
            An optional set of act-as parties to use to submit this command. Note that for a
            ledger with authorization, these parties must be a subset of the parties in the token.
        :return:
            The return value of the choice, together with a list of events that occurred as a result
            of exercising the choice.
        """
        raise NotImplementedError

    def archive(
        self,
        __contract_id,
        *,
        workflow_id=None,
        command_id=None,
        read_as=None,
        act_as=None,
    ):
        """
        Archive a choice on a contract identified by its contract ID.

        :param __contract_id:
            The contract ID of the contract to exercise.

            Note that future versions reserve the right to rename this parameter name at any
            time; it should be passed in as a positional parameter and never by name.
        :param workflow_id:
            An optional workflow ID.
        :param command_id:
            An optional command ID. If unspecified, a random one will be created.
        :param read_as:
            An optional set of read-as parties to use to submit this command. Note that for a
            ledger with authorization, these parties must be a subset of the parties in the token.
        :param act_as:
            An optional set of act-as parties to use to submit this command. Note that for a
            ledger with authorization, these parties must be a subset of the parties in the token.
        :return:
            The return value of the choice, together with a list of events that occurred as a result
            of exercising the choice.
        """
        raise NotImplementedError

    def archive_by_key(
        self,
        __template_id,
        __key,
        *,
        workflow_id=None,
        command_id=None,
        read_as=None,
        act_as=None,
    ):
        """
        Exercise a choice on a contract identified by its contract key.

        :param __template_id:
            The template of the contract to be created (positional argument only).

            Note that future versions reserve the right to rename this parameter name at any
            time; it should be passed in as a positional parameter and never by name.
        :param __key:
            The key of the contract to exercise.

            Note that future versions reserve the right to rename this parameter name at any
            time; it should be passed in as a positional parameter and never by name.
        :param workflow_id:
            An optional workflow ID.
        :param command_id:
            An optional command ID. If unspecified, a random one will be created.
        :param read_as:
            An optional set of read-as parties to use to submit this command. Note that for a
            ledger with authorization, these parties must be a subset of the parties in the token.
        :param act_as:
            An optional set of act-as parties to use to submit this command. Note that for a
            ledger with authorization, these parties must be a subset of the parties in the token.
        :return:
            The return value of the choice, together with a list of events that occurred as a result
            of exercising the choice.
        """
        raise NotImplementedError

    def query(self, __template_id="*", __query=None, *, read_as=None):
        """
        Return the create events from the active contract set service as a stream.

        If you find yourself repeatedly calling :meth:`query` or :meth:`query_many` over the same
        set of templates, you may want to consider :class:`ACS` instead, which is a utility class
        that helps you maintain a "live" state of the ACS.

        :param __template_id:
            The name of the template for which to fetch contracts.

            Note that future versions reserve the right to rename this parameter name at any
            time; it should be passed in as a positional parameter and never by name.
        :param __query:
            A filter to apply to the set of returned contracts.

            Note that future versions reserve the right to rename this parameter name at any
            time; it should be passed in as a positional parameter and never by name.
        :param read_as:
            An optional set of read-as parties to use to submit this query. Note that for a
            ledger with authorization, these parties must be a subset of the parties in the token.
        :return:
            A query stream that iterates over the :class:`CreateEvent` objects of the Active
            Contract Set, and terminates.
        """
        raise NotImplementedError

    def query_many(self, *q, read_as=None):
        """
        Return the create events from the active contract set service as a stream.

        If you find yourself repeatedly calling :meth:`query` or :meth:`query_many` over the same
        set of templates, you may want to consider :class:`ACS` instead, which is a utility class
        that helps you maintain a "live" state of the ACS.

        Examples:

            # Return a stream that returns a snapshot of the complete ACS
            stream = conn.query_many()

            # Return a stream that iterates over the Magic template in the So.Much module
            stream = conn.query_many("So.Much:Magic")

            # Return a stream that iterates over two templates
            # (can either be called with multiple parameters or as a single list)
            stream = conn.query_many("So.Much:Magic", "So.Much:Awesome")
            stream = conn.query_many(["So.Much:Magic", "So.Much:Awesome"])

            # Return a stream that iterates over Magic templates
            # with a field `power` having a value of 100
            stream = conn.query_many({"So.Much:Magic": {"power": 100}})
        """
        raise NotImplementedError

    def stream(self, __template_id="*", __query=None, *, offset=None, read_as=None):
        """
        Stream create/archive events.

        When ``offset`` is ``None``, create events from the active contract set are returned first,
        followed by a continuous stream of updates (creates/archives).

        Otherwise, ``offset`` can be supplied to resume a stream from a prior point where a
        ``Boundary`` was returned from a previous stream.

        :param __template_id:
            The name of the template for which to fetch contracts.

            Note that future versions reserve the right to rename this parameter name at any
            time; it should be passed in as a positional parameter and never by name.
        :param __query:
            A filter to apply to the set of returned contracts. Note that this does not filter
            :class:`ArchiveEvent`; readers of the stream MUST be able to cope with "mismatched"
            archives that come from the result of applying a filter.

            Note that future versions reserve the right to rename this parameter name at any
            time; it should be passed in as a positional parameter and never by name.
        :param offset:
            An optional offset at which to start receiving events. If ``None``, start from the
            beginning.
        :param read_as:
            An optional set of read-as parties to use to submit this query. Note that for a
            ledger with authorization, these parties must be a subset of the parties in the token.
        """
        raise NotImplementedError

    def stream_many(self, *q, offset=None, read_as=None):
        """
        Stream create/archive events from more than one template ID in the same stream.

        When ``offset`` is ``None``, create events from the active contract set are returned first,
        followed by a continuous stream of updates (creates/archives).

        Otherwise, ``offset`` can be supplied to resume a stream from a prior point where a
        ``Boundary`` was returned from a previous stream.

        Examples:

            # Return a stream that returns a snapshot of the complete ACS
            stream = conn.stream_many()

            # Return a stream that iterates over the Magic template in the So.Much module
            stream = conn.stream_many("So.Much:Magic")

            # Return a stream that iterates over two templates
            # (can either be called with multiple parameters or as a single list)
            stream = conn.stream_many("So.Much:Magic", "So.Much:Awesome")
            stream = conn.stream_many(["So.Much:Magic", "So.Much:Awesome"])

            # Return a stream that iterates over Magic templates
            # with a field `power` having a value of 100
            stream = conn.stream_many({"So.Much:Magic": {"power": 100}})
        """
        raise NotImplementedError

    def get_user(self, user_id=None):
        """
        Get the user data of a specific user or the authenticated user.

        :param user_id:
            If supplied, the user whose data to retrieve. If unspecified, then the data for the
            currently authenticated user will be retrieved.
        :return:
            Information about the specified :class:`User`.
        """
        raise NotImplementedError

    def list_users(self):
        """
        List all existing users.

        :return:
            Information about all :class:`User`'s on the backing participant.
        """
        raise NotImplementedError

    def allocate_party(self, *, identifier_hint=None, display_name=None):
        """
        Allocate a new party.

        This method requires that the connection be created with ``admin=true``, or a token that
        contains an ``admin=true`` claim.

        :param identifier_hint:
            A hint to the backing participant. Note that the Daml ledger is free to ignore this
            hint entirely.
        :type identifier_hint: str
        :param display_name:
            A human-readable name that corresponds to the allocated ``Party``.
        :type display_name: str
        :return:
            Information about the allocated ``Party``.
        """
        raise NotImplementedError

    def list_known_parties(self):
        """
        Return a list of :class:`PartyInfo` for all parties on the ledger.
        """
        raise NotImplementedError

    def upload_package(self, __contents):
        """
        Upload a byte array as a DAR file to the remote Daml ledger.

        This method requires that the connection be created with ``admin=true``, or a token that
        contains an ``admin=true`` claim.

        :param __contents:
            The contents of a DAR file (for example, as obtained from running ``daml build``).

            Note that future versions reserve the right to rename this parameter name at any
            time; it should be passed in as a positional parameter and never by name.
        """
        raise NotImplementedError

    def get_metering_report(self, from_, to=None, application_id=None):
        """
        Retrieve a metering report.

        :param from_:
            The from timestamp (inclusive).
        :param to:
            If specified, the to timestamp (exclusive). If not provided, the server will default to
            its current time.
        :param application_id:
            If specified, the report will only be generated for the specified application.
        :return:
            A :class:`ParticipantMeteringReport`.
        """
        raise NotImplementedError


class QueryStream(Protocol):
    """
    Protocol for classes that provide for reading from a stream of events from a Daml ledger. Like
    :class:`Connection`, there are async query streams (:class:`dazl.ledger.aio.QueryStream`) and
    blocking query streams (:class:`dazl.ledger.blocking.QueryStream`).
    """

    def on_create(self, *args):
        """
        Register a callback that is triggered whenever a :class:`CreateEvent` is read through the
        stream.
        """
        raise NotImplementedError

    def on_archive(self, *args):
        """
        Register a callback that is triggered whenever a :class:`ArchiveEvent` is read through the
        stream.
        """
        raise NotImplementedError

    def on_boundary(self, *args):
        """
        Register a callback that is triggered whenever a :class:`Boundary` is read through the
        stream.
        """
        raise NotImplementedError

    def close(self):
        """
        Close and dispose of any resources used by this stream.

        This can be called at any time to end a stream prematurely, and is the only way to abort
        a stream returned by :meth:`Connection.stream`/:meth:`Connection.stream_many`.
        """
        raise NotImplementedError

    def run(self):
        """
        Consume the stream without returning any values.

        This method is useful if you use :meth:`on_create`, :meth:`on_archive`, or
        :meth:`on_boundary` to register callbacks for events.

        On _asynchronous_ connections, this method is a coroutine that terminates once the stream
        has ended. For streams returned by :meth:`Connection.stream`/:meth:`Connection.stream_many`,
        the stream is only ended by :meth:`close`.

        On _blocking_ connections, this method blocks until the stream has ended.

        For streams returned by :meth:`Connection.stream`/:meth:`Connection.stream_many`, the
        method blocks indefinitely, and is only closed if :meth:`close` is called or the
        server disconnects.
        """
        raise NotImplementedError

    def creates(self):
        """
        Return a stream of :class:`CreateEvent` objects. This will include the contracts of the
        Active Contract Set, as well as create events over subsequent transactions.

        On _asynchronous_ connections, this method is an asynchronous iterator: use ``async for``
        to iterate over its contents.

        On _blocking_ connections, this method a blocking iterator: use ``for`` to iterate over its
        contents.

        For streams returned by :meth:`Connection.stream`/:meth:`Connection.stream_many`, the
        iterator remains open indefinitely, and is only closed if :meth:`close` is called or the
        server disconnects.
        """
        raise NotImplementedError

    def events(self):
        """
        Return a stream of :class:`CreateEvent` and :class:`ArchiveEvent` objects. This will include
        the initial contracts of the Active Contract Set, as well as create and archive events over
        subsequent transactions. You may see :class:`ArchiveEvent` objects that had no
        :class:`CreateEvent`s predecessor; this will typically happen with event filtering (which
        can only effectively filter over :class:`CreateEvent`

        On _asynchronous_ connections, this method is an asynchronous iterator: use ``async for``
        to iterate over its contents.

        On _blocking_ connections, this method a blocking iterator: use ``for`` to iterate over its
        contents.

        For streams returned by :meth:`Connection.stream`/:meth:`Connection.stream_many`, the
        iterator remains open indefinitely, and is only closed if :meth:`close` is called or the
        server disconnects.
        """
        raise NotImplementedError

    def items(self):
        """
        Return a stream of :class:`CreateEvent`, :class:`ArchiveEvent`, and :class:`Boundary`
        objects. This will include the initial contracts of the Active Contract Set, as well as
        create and archive events over subsequent transactions, and :class:`Boundary` objects that
        describe offsets where an interrupted stream can be resumed without having to re-read the
        initial contracts of the Active Contract Set.

        On _asynchronous_ connections, this method is an asynchronous iterator: use ``async for``
        to iterate over its contents.

        On _blocking_ connections, this method a blocking iterator: use ``for`` to iterate over its
        contents.

        For streams returned by :meth:`Connection.stream`/:meth:`Connection.stream_many`, the
        iterator remains open indefinitely, and is only closed if :meth:`close` is called or the
        server disconnects.
        """
        raise NotImplementedError
