# Copyright (c) 2019 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""
Write-Side types
----------------

The :mod:`dazl.model.writing` module contains the Python classes used on the write-side of the
Ledger API.

.. autoclass:: Command
   :members:

.. autoclass:: CreateCommand
   :members:

.. autoclass:: ExerciseCommand
   :members:
"""
import uuid
import warnings
from datetime import datetime, timedelta
from typing import Any, Collection, Dict, Generic, List, Mapping, Optional, Sequence, TypeVar, Union

from dataclasses import dataclass, fields

from .. import LOG
from .core import ContractId, Party
from .types import Type, TypeReference, UnresolvedTypeReference, TemplateChoice, \
    RecordType, UnsupportedType, VariantType, ContractIdType, ListType, OptionalType, TextMapType, \
    EnumType, scalar_type_dispatch_table, TypeEvaluationContext, type_evaluate_dispatch, \
    TemplateMeta, ChoiceMeta
from .types_store import PackageStore
from ..util.prim_types import DEFAULT_TYPE_CONVERTER
from ..util.typing import safe_cast, safe_optional_cast

TCommand = TypeVar('TCommand')
TValue = TypeVar('TValue')


CommandsOrCommandSequence = Union[None, 'Command', List[Optional['Command']]]
EventHandlerResponse = Union[CommandsOrCommandSequence, 'CommandBuilder', 'CommandPayload']


class Command:
    """
    Base class for write-side commands.
    """


@dataclass(init=False, frozen=True)
class CreateCommand(Command):
    """
    A command that creates a contract without any predecessors.

    .. attribute:: CreateCommand.template

        Refers to the type of a template. This can be passed in as a ``str`` to the constructor,
        where it assumed to represent the ID or name of a template.

    .. attribute:: CreateCommand.arguments

        The arguments to the create (as a ``dict``).
    """
    __slots__ = ('template', 'arguments')

    template: Type
    arguments: Dict[str, Any]

    def __init__(self, template: 'Union[str, Type]', arguments=None):
        object.__setattr__(self, 'template', template if isinstance(template, Type)
                           else UnresolvedTypeReference(template))
        object.__setattr__(self, 'arguments', arguments or dict())

    def replace(self, template: Union[None, str, Type] = None, arguments=None):
        """
        Create a new :class:`CreateCommand` with the same identifier as this command, but with new
        values for its parameters.

        :param template:
            The new value of the `template` field, or `None` to reuse the existing value.
        :param arguments:
            The new value of the `arguments` field, or `None` to reuse the existing value.
        """
        if template is not None:
            template = template if isinstance(template, Type) \
                else UnresolvedTypeReference(template)
        return CreateCommand(
            template if template is not None else self.template,
            arguments if arguments is not None else self.arguments)

    def __repr__(self):
        return f'<create {self.template} {self.arguments}>'


@dataclass(init=False, frozen=True)
class ExerciseCommand(Command):
    """
    A command that exercises a choice on a pre-existing contract.

    .. attribute:: ExerciseCommand.contract

        The :class:`ContractId` on which a choice is being exercised.

    .. attribute:: ExerciseCommand.choice

        Refers to a choice (either a :class:`ChoiceRef` or a :class:`ChoiceMetadata`).
        This can be passed in as a ``str`` to the constructor, where it assumed to represent the
        name of a choice.

    .. attribute:: ExerciseCommand.arguments

        The arguments to the exercise choice (as a ``dict``).

    Note that when an ``ExerciseCommand`` is created, an additional ``template_id`` parameter can
    be supplied to the constructor to aid in disambiguation of the specific choice being invoked.
    In some situations involving composite commands, a ``template_id`` must eventually be supplied
    before a choice can be exercised. If this ``template_id`` is specified, the ``contract`` and
    ``choice`` are both tagged with this ID.

    Instance methods:

    .. automethod:: replace
    """
    __slots__ = ('contract', 'choice', 'arguments')

    def __init__(
            self,
            contract: 'Union[str, ContractId]',
            choice: str,
            arguments=None,
            template_id=None):
        if isinstance(contract, str):
            warnings.warn('Untyped ContractId support will be removed with the removal of '
                          'the deprecated REST API.', DeprecationWarning, stacklevel=2)
            with warnings.catch_warnings():
                warnings.simplefilter('ignore')
                contract = ContractId(contract, template_id=template_id)
        elif template_id is not None:
            warnings.warn(
                'Specifying template_id in an ExerciseChoice is no longer necessary. ' +
                'Please avoid specifying it, as this parameter will be removed in the future.',
                DeprecationWarning, stacklevel=2)
        elif not isinstance(contract, ContractId):
            raise ValueError('ContractId expected here')

        object.__setattr__(self, 'contract', contract)
        object.__setattr__(self, 'choice', choice)
        object.__setattr__(self, 'arguments', dict(arguments) if arguments is not None else dict())

    def replace(self, contract=None, choice=None, arguments=None, template_id=None):
        """
        Create a new :class:`ExerciseCommand` with the same identifier as this command, but with new
        values for its parameters.

        :param contract:
            The new value of the `contract` field, or `None` to reuse the existing value.
            The same type coercion rules used in the constructor apply here.
        :param choice:
            The new value of the `choice` field, or `None` to reuse the existing value.
            The same type coercion rules used in the constructor apply here.
        :param arguments:
            The new value of the `choice` field, or `None` to reuse the existing value.
        :param template_id:
            The expected template type.
        """
        return ExerciseCommand(
            contract if contract is not None else self.contract,
            choice if choice is not None else self.choice,
            arguments if arguments is not None else self.arguments,
            template_id)

    def __repr__(self):
        return '<exercise \"{}\" with {} on {}>'.format(
            self.choice,
            self.arguments,
            self.contract.contract_id if hasattr(self.contract, 'contract_id') else self.contract)


@dataclass(frozen=True)
class ExerciseByKeyCommand(Command):
    template: Type
    contract_key: Any
    choice: str
    choice_argument: Mapping[str, Any]


@dataclass(frozen=True)
class CreateAndExerciseCommand(Command):
    template: Type
    arguments: Mapping[str, Any]
    choice: str
    choice_argument: Mapping[str, Any]


class CommandBuilder:
    """
    Builder class for generating commands to be sent to the ledger.
    """

    @classmethod
    def coerce(cls, obj, atomic_default=False) -> 'CommandBuilder':
        """
        Create a :class:`CommandBuilder` from the objects that an event handler is allowed to
        return.

        :param obj:
        :param atomic_default:
        :return:
        """
        if isinstance(obj, CommandBuilder):
            return obj

        builder = CommandBuilder(atomic_default=atomic_default)
        if obj is not None:
            builder.append(obj)
        return builder

    def __init__(self, atomic_default=False):
        self._atomic_default = atomic_default
        self._commands = [[]]  # type: List[List[Command]]
        self._defaults = CommandDefaults()

    def defaults(self,
                 party: Optional[Party] = None,
                 ledger_id: Optional[str] = None,
                 workflow_id: Optional[str] = None,
                 application_id: Optional[str] = None,
                 command_id: Optional[str] = None) -> None:
        if party is not None:
            self._defaults.default_party = party
        if ledger_id is not None:
            self._defaults.ledger_id = ledger_id
        if workflow_id is not None:
            self._defaults.default_workflow_id = workflow_id
        if application_id is not None:
            self._defaults.default_application_id = application_id
        if command_id is not None:
            self._defaults.default_command_id = command_id

    def create(self, template, arguments=None) -> 'CommandBuilder':
        return self.append(create(template, arguments=arguments))

    def exercise(self, contract, choice, arguments=None) -> 'CommandBuilder':
        return self.append(exercise(contract, choice, arguments=arguments))

    def create_and_exercise(self, template, create_arguments, choice_name, choice_arguments=None) \
            -> 'CommandBuilder':
        return self.append(create_and_exercise(
            template, create_arguments, choice_name, choice_arguments))

    def append(self, *commands: CommandsOrCommandSequence) -> 'CommandBuilder':
        """
        Append one or more commands, or list of commands to the :class:`CommandBuilder` in flight.
        This method respects the value of ``atomic_default`` that this object was constructed with.
        In order to force commands to be submitted either atomically, use :meth:`append_atomically`.
        To allow these commands to be submitted in parallel use :meth:`append_nonatomically`.

        :param commands: One or more commands, or list of commands to be submitted to the ledger.
        :return: This object.
        """
        if self._atomic_default:
            # a command builder that defaults to being atomic will put all commands in a single
            # transaction; build on the very first transaction
            self._commands[0].extend(flatten_command_sequence(commands))
            return self
        else:
            return self.append_nonatomically(*commands)

    def append_atomically(self, *commands: Union[Command, Sequence[Command]]) -> 'CommandBuilder':
        self._commands.extend([flatten_command_sequence(commands)])
        return self

    def append_nonatomically(self, *commands: Union[Command, Sequence[Command]]) -> \
            'CommandBuilder':
        self._commands.extend([[cmd] for cmd in flatten_command_sequence(commands)])
        return self

    def build(self, defaults: 'Optional[CommandDefaults]' = None, now: Optional[datetime] = None) \
            -> 'Collection[CommandPayload]':
        """
        Return a collection of commands.
        """
        if defaults is None:
            raise ValueError('defaults must currently be specified')

        command_id = defaults.default_command_id or self._defaults.default_command_id or \
            uuid.uuid4().hex

        return [CommandPayload(
            party=defaults.default_party or self._defaults.default_party,
            ledger_id=defaults.default_ledger_id or self._defaults.default_ledger_id,
            workflow_id=defaults.default_workflow_id or self._defaults.default_workflow_id,
            application_id=defaults.default_application_id or self._defaults.default_application_id,
            command_id=command_id,
            ledger_effective_time=now,
            maximum_record_time=now + (defaults.default_ttl or self._defaults.default_ttl),
            commands=commands
        ) for i, commands in enumerate(self._commands) if commands]

    def __format__(self, format_spec):
        if format_spec == 'c':
            return str(self._commands)
        else:
            return repr(self)

    def __repr__(self):
        return f'CommandBuilder({self._commands})'


def flatten_command_sequence(commands: Sequence[CommandsOrCommandSequence]) -> List[Command]:
    """
    Convert a list of mixed commands, ``None``, and list of commands into an ordered sequence of
    non-``None`` commands.
    """
    ret = []  # type: List[Command]
    errors = []

    for i, obj in enumerate(commands):
        if obj is not None:
            if isinstance(obj, Command):
                ret.append(obj)
            else:
                try:
                    cmd_iter = iter(obj)
                except TypeError:
                    errors.append(((i,), obj))
                    continue
                for j, cmd in enumerate(cmd_iter):
                    if isinstance(cmd, Command):
                        ret.append(cmd)
                    else:
                        errors.append(((i, j), cmd))
    if errors:
        raise ValueError(f'Failed to interpret some elements as Commands in the list: '
                         f'$[{index}] = {command}' for index, command in errors)
    return ret


@dataclass
class CommandDefaults:
    """
    Values to use for a :class:`Command` when no value is specified with the creation of the
    command.
    """

    default_party: Optional[Party] = None
    default_ledger_id: Optional[str] = None
    default_workflow_id: Optional[str] = None
    default_application_id: Optional[str] = None
    default_command_id: Optional[str] = None
    default_ttl: Optional[timedelta] = None


@dataclass(frozen=True)
class CommandPayload:
    """
    A request to mutate active state of the ledger.

    .. attribute:: CommandPayload.party
        The party submitting the request.
    .. attribute:: CommandPayload.application_id:
        An optional application ID to accompany the request.
    .. attribute:: CommandPayload.command_id:
        A hash that represents the BIM commitment.
    .. attribute:: CommandPayload.ledger_effective_time:
        The effective time of this command. Should usually be set to ``datetime.now()``, but
        may have a different value when the server is operating in static time mode.
    .. attribute:: CommandPayload.maximum_record_time:
        The maximum time before the client should consider this command expired.
    .. attribute:: CommandPayload.commands
        A sequence of commands to submit to the ledger. These commands are submitted atomically
        (in other words, they all succeed or they all fail).
    """
    party: Party
    ledger_id: str
    workflow_id: str
    application_id: str
    command_id: str
    ledger_effective_time: datetime
    maximum_record_time: datetime
    commands: Sequence[Command]

    def __post_init__(self):
        missing_fields = [field.name for field in fields(self) if getattr(self, field.name) is None]
        if missing_fields:
            raise ValueError(f'Some fields are set to None when they are required: '
                             f'{missing_fields}')


def create(template, arguments=None):
    from .types_dynamic import NamedRecord, ProxyMeta

    template_type = type(template)
    if isinstance(template_type, TemplateMeta):
        # static codegen, instantiated type
        if arguments is not None:
            raise ValueError('arguments cannot be specified with an instantiated template')
        arguments = template._asdict()
        template = str(template_type)

    elif isinstance(template, NamedRecord):
        # dynamic "codegen", instantiated type
        if arguments is not None:
            raise ValueError('arguments cannot be specified with an instantiated template')
        template, arguments = template.name, template.arguments

    elif template_type == TemplateMeta:
        # static codegen, non-instantiated
        template = str(template)

    elif isinstance(template_type, ProxyMeta):
        # dynamic codegen, non-instantiated
        template = str(template_type)

    elif not isinstance(template, str):
        raise ValueError(
            'template must be a string name, a template type, or an instantiated template')

    return CreateCommand(template, arguments)


def exercise(contract, choice, arguments=None):
    from .types_dynamic import NamedRecord, ProxyMeta

    choice_type = type(choice)
    if isinstance(choice_type, ChoiceMeta):
        # static codegen, instantiated type
        if arguments is not None:
            raise ValueError('arguments cannot be specified with an instantiated template')
        arguments = choice._asdict()
        choice = str(choice_type)

    elif isinstance(choice, NamedRecord):
        # dynamic "codegen", instantiated type
        if arguments is not None:
            raise ValueError('arguments cannot be specified with an instantiated template')
        choice, arguments = choice.name, choice.arguments
        choice_start_idx = choice.rfind('.')
        if choice_start_idx >= 0:
            choice = choice[choice_start_idx + 1:]

    elif choice_type == ChoiceMeta:
        # static codegen, non-instantiated
        choice = str(choice)

    elif isinstance(choice_type, ProxyMeta):
        # dynamic codegen, non-instantiated
        choice = str(choice_type)
        choice_start_idx = choice.rfind('.')
        if choice_start_idx >= 0:
            choice = choice[choice_start_idx + 1:]

    elif not isinstance(choice, str):
        raise ValueError('choice must be a string name, a template type, '
                         'or an instantiated template')

    return ExerciseCommand(contract, choice, arguments)


def exercise_by_key(template, contract_key, choice_name, choice_argument):
    return ExerciseByKeyCommand(template, contract_key, choice_name, choice_argument)


def create_and_exercise(template, create_arguments, choice_name, choice_argument):
    return CreateAndExerciseCommand(template, create_arguments, choice_name, choice_argument)


####################################################################################################
# argument iteration support
####################################################################################################


def arg_iter(value):
    """
    Produce an iterator that walks over an argument tree and all of its values, recursing into
    lists and record/variant fields.
    """
    if isinstance(value, str):
        # str is a common case, and it's also iterable (which we don't want to exploit here)
        yield value
    elif isinstance(value, dict):
        for sub_value in value.values():
            yield sub_value
    elif hasattr(value, '__iter__'):
        for sub_value in value:
            yield sub_value
    else:
        yield value


class Serializer(Generic[TCommand, TValue]):
    """
    Serializer interface for objects on the write-side of the API.
    """

    def serialize_value(self, type_token: Type, obj: Any) -> TValue:
        raise NotImplementedError('serialize_value requires an implementation')

    def serialize_command(self, command: Command) -> TCommand:
        raise NotImplementedError('serialize_command requires an implementation')


class AbstractSerializer(Serializer[TCommand, TValue]):
    """
    Implementation of :class:`Serializer` that helps enforce that all possible cases of type
    serialization have been implemented.
    """
    def __init__(self, store: PackageStore, type_context: 'Optional[TypeEvaluationContext]' = None):
        self.store = safe_cast(PackageStore, store)
        self.type_context = safe_optional_cast(TypeEvaluationContext, type_context) or \
            DEFAULT_TYPE_CONVERTER

    def serialize_value(self, tt: Type, obj: Any) -> TValue:
        context = TypeEvaluationContext.from_store(self.store)
        try:
            return self._serialize_dispatch(context, tt, obj)
        except:
            from ..util.fmt_py import python_example_object

            LOG.warning("Expected something like:")
            for line in str.splitlines(python_example_object(self.store, tt)):
                LOG.warning('    %s', line)

            LOG.warning("But got this instead:")
            LOG.warning('    %r', obj)
            raise

    def serialize_commands(self, commands: Sequence[Command]) -> Sequence[TCommand]:
        return [self.serialize_command(cmd) for cmd in commands]

    def serialize_command(self, command: Command) -> TCommand:
        if isinstance(command, CreateCommand):
            tt = _resolve_template_type(self.store, command.template)
            value = self.serialize_value(tt, command.arguments)
            return self.serialize_create_command(tt, value)
        elif isinstance(command, ExerciseCommand):
            template_type_ref = command.contract.template_id
            choice_name = command.choice
            choice_opts = self.store.resolve_choice(template_type_ref, choice_name)
            if len(choice_opts) == 0:
                msg = f'Could not resolve {template_type_ref} {choice_name} to any valid choices'
                LOG.error(msg)
                raise ValueError(msg)
            if len(choice_opts) > 1:
                msg = f'Could not uniquely resolve {template_type_ref} {choice_name} ' \
                    f'to a single valid choice'
                LOG.error(msg)
                raise ValueError(msg)
            tt, choice = next(iter(choice_opts.items()))

            args = self.serialize_value(choice.type, command.arguments)
            return self.serialize_exercise_command(command.contract, choice, args)
        elif isinstance(command, CreateAndExerciseCommand):
            tt = _resolve_template_type(self.store, command.template)
            create_value = self.serialize_value(tt, command.arguments)
            _, choice_info = next(iter(self.store.resolve_choice(tt, command.choice).items()))
            choice_args = self.serialize_value(choice_info.type, command.choice_argument)
            return self.serialize_create_and_exercise_command(
                tt, create_value, choice_info, choice_args)
        elif isinstance(command, ExerciseByKeyCommand):
            template, = self.store.resolve_template(command.template)
            key_value = self.serialize_value(template.key_type, command.contract_key)
            choices = self.store.resolve_choice(template, command.choice)
            _, choice_info = next(iter(choices.items()))
            choice_args = self.serialize_value(choice_info.type, command.choice_argument)
            return self.serialize_exercise_by_key_command(
                template.data_type.name, key_value, choice_info, choice_args)
        else:
            raise ValueError(f'unknown Command type: {command!r}')

    def serialize_create_command(
            self, template_type: RecordType, template_args: TValue) \
            -> TCommand:
        raise NotImplementedError('serialize_create_command requires an implementation')

    def serialize_exercise_command(
            self, contract_id: ContractId, choice_info: TemplateChoice, choice_args: TValue) \
            -> TCommand:
        raise NotImplementedError('serialize_exercise_command requires an implementation')

    def serialize_exercise_by_key_command(
            self, template_ref: TypeReference, key_arguments: Any,
            choice_info: TemplateChoice, choice_arguments: Any) -> TCommand:
        raise NotImplementedError(
            'serialize_exercise_by_key_command requires an implementation')

    def serialize_create_and_exercise_command(
            self, template_type: RecordType, create_arguments: Any,
            choice_info: TemplateChoice, choice_arguments: Any) -> TCommand:
        raise NotImplementedError(
            'serialize_create_and_exercise_command requires an implementation')

    def serialize_unit(self, context: TypeEvaluationContext, obj: Any) -> TValue:
        raise NotImplementedError('serialize_unit requires an implementation')

    def serialize_bool(self, context: TypeEvaluationContext, obj: Any) -> TValue:
        raise NotImplementedError('serialize_bool requires an implementation')

    def serialize_text(self, context: TypeEvaluationContext, obj: Any) -> TValue:
        raise NotImplementedError('serialize_bool requires an implementation')

    def serialize_int(self, context: TypeEvaluationContext, obj: Any) -> TValue:
        raise NotImplementedError('serialize_bool requires an implementation')

    def serialize_decimal(self, context: TypeEvaluationContext, obj: Any) -> TValue:
        raise NotImplementedError('serialize_bool requires an implementation')

    def serialize_party(self, context: TypeEvaluationContext, obj: Any) -> TValue:
        raise NotImplementedError('serialize_bool requires an implementation')

    def serialize_date(self, context: TypeEvaluationContext, obj: Any) -> TValue:
        raise NotImplementedError('serialize_bool requires an implementation')

    def serialize_datetime(self, context: TypeEvaluationContext, obj: Any) -> TValue:
        raise NotImplementedError('serialize_bool requires an implementation')

    def serialize_timedelta(self, context: TypeEvaluationContext, obj: Any) -> TValue:
        raise NotImplementedError('serialize_bool requires an implementation')

    def serialize_contract_id(self, context: TypeEvaluationContext, tt: ContractIdType, obj: Any) \
            -> TValue:
        raise NotImplementedError('serialize_contract_id requires an implementation')

    def serialize_optional(self, context: TypeEvaluationContext, tt: OptionalType, obj: Any) \
            -> TValue:
        raise NotImplementedError('serialize_optional requires an implementation')

    def serialize_list(self, context: TypeEvaluationContext, tt: ListType, obj: Any) -> TValue:
        raise NotImplementedError('serialize_list requires an implementation')

    def serialize_map(self, context: TypeEvaluationContext, tt: TextMapType, obj: Any) -> TValue:
        raise NotImplementedError('serialize_map requires an implementation')

    def serialize_record(self, context: TypeEvaluationContext, tt: RecordType, obj: Any) -> TValue:
        raise NotImplementedError('serialize_record requires an implementation')

    def serialize_variant(self, context: TypeEvaluationContext, tt: VariantType, obj: Any) \
            -> TValue:
        raise NotImplementedError('serialize_variant requires an implementation')

    def serialize_enum(self, context: TypeEvaluationContext, tt: EnumType, obj: Any) -> TValue:
        raise NotImplementedError('serialize_enum requires an implementation')

    def serialize_unsupported(self, context: TypeEvaluationContext, tt: UnsupportedType, obj: Any) \
            -> TValue:
        raise NotImplementedError('serialize_unsupported requires an implementation')

    def _serialize_dispatch(self, context: TypeEvaluationContext, tt: Type, obj: Any) -> TValue:
        eval_fn = type_evaluate_dispatch(
            lambda c, st: scalar_type_dispatch_table(
                lambda: self.serialize_unit(c, obj),
                lambda: self.serialize_bool(c, obj),
                lambda: self.serialize_text(c, obj),
                lambda: self.serialize_int(c, obj),
                lambda: self.serialize_decimal(c, obj),
                lambda: self.serialize_party(c, obj),
                lambda: self.serialize_date(c, obj),
                lambda: self.serialize_datetime(c, obj),
                lambda: self.serialize_timedelta(c, obj))(st),
            lambda c, ct: self.serialize_contract_id(c, ct, obj),
            lambda c, ot: self.serialize_optional(c, ot, obj),
            lambda c, lt: self.serialize_list(c, lt, obj),
            lambda c, mt: self.serialize_map(c, mt, obj),
            lambda c, rt: self.serialize_record(c, rt, obj),
            lambda c, vt: self.serialize_variant(c, vt, obj),
            lambda c, et: self.serialize_enum(c, et, obj),
            lambda c, ut: self.serialize_unsupported(c, ut, obj))
        return eval_fn(context, tt)


def _resolve_template_type(store: 'PackageStore', template) -> 'RecordType':
    candidates = store.resolve_template_type(template)
    if len(candidates) == 0:
        msg = f'Could not resolve {template} to any valid types'
        LOG.error(msg)
        raise ValueError(msg)
    elif len(candidates) > 1:
        msg = f'Could not uniquely resolve {template} to a single valid type'
        LOG.error(msg)
        raise ValueError(msg)

    tt, = candidates.values()
    if not isinstance(tt, RecordType):
        msg = f'CreateCommand requires a type that is a record (got {tt} instead)'
        LOG.error(msg)
        raise ValueError(msg)

    return tt
