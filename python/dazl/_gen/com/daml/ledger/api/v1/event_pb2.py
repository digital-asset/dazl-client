# Copyright (c) 2017-2022 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: com/daml/ledger/api/v1/event.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import value_pb2 as com_dot_daml_dot_ledger_dot_api_dot_v1_dot_value__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='com/daml/ledger/api/v1/event.proto',
  package='com.daml.ledger.api.v1',
  syntax='proto3',
  serialized_options=b'\n\026com.daml.ledger.api.v1B\017EventOuterClassZOgithub.com/digital-asset/dazl-client/go/v7/pkg/generated/com/daml/ledger/api/v1\252\002\026Com.Daml.Ledger.Api.V1',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\"com/daml/ledger/api/v1/event.proto\x12\x16\x63om.daml.ledger.api.v1\x1a\"com/daml/ledger/api/v1/value.proto\x1a\x1egoogle/protobuf/wrappers.proto\"\xa8\x01\n\x05\x45vent\x12@\n\x07\x63reated\x18\x01 \x01(\x0b\x32$.com.daml.ledger.api.v1.CreatedEventH\x00R\x07\x63reated\x12\x43\n\x08\x61rchived\x18\x03 \x01(\x0b\x32%.com.daml.ledger.api.v1.ArchivedEventH\x00R\x08\x61rchivedB\x07\n\x05\x65ventJ\x04\x08\x02\x10\x03R\texercised\"\xca\x03\n\x0c\x43reatedEvent\x12\x19\n\x08\x65vent_id\x18\x01 \x01(\tR\x07\x65ventId\x12\x1f\n\x0b\x63ontract_id\x18\x02 \x01(\tR\ncontractId\x12\x43\n\x0btemplate_id\x18\x03 \x01(\x0b\x32\".com.daml.ledger.api.v1.IdentifierR\ntemplateId\x12@\n\x0c\x63ontract_key\x18\x07 \x01(\x0b\x32\x1d.com.daml.ledger.api.v1.ValueR\x0b\x63ontractKey\x12I\n\x10\x63reate_arguments\x18\x04 \x01(\x0b\x32\x1e.com.daml.ledger.api.v1.RecordR\x0f\x63reateArguments\x12\'\n\x0fwitness_parties\x18\x05 \x03(\tR\x0ewitnessParties\x12 \n\x0bsignatories\x18\x08 \x03(\tR\x0bsignatories\x12\x1c\n\tobservers\x18\t \x03(\tR\tobservers\x12\x43\n\x0e\x61greement_text\x18\x06 \x01(\x0b\x32\x1c.google.protobuf.StringValueR\ragreementText\"\xb9\x01\n\rArchivedEvent\x12\x19\n\x08\x65vent_id\x18\x01 \x01(\tR\x07\x65ventId\x12\x1f\n\x0b\x63ontract_id\x18\x02 \x01(\tR\ncontractId\x12\x43\n\x0btemplate_id\x18\x03 \x01(\x0b\x32\".com.daml.ledger.api.v1.IdentifierR\ntemplateId\x12\'\n\x0fwitness_parties\x18\x04 \x03(\tR\x0ewitnessParties\"\xdb\x03\n\x0e\x45xercisedEvent\x12\x19\n\x08\x65vent_id\x18\x01 \x01(\tR\x07\x65ventId\x12\x1f\n\x0b\x63ontract_id\x18\x02 \x01(\tR\ncontractId\x12\x43\n\x0btemplate_id\x18\x03 \x01(\x0b\x32\".com.daml.ledger.api.v1.IdentifierR\ntemplateId\x12\x16\n\x06\x63hoice\x18\x05 \x01(\tR\x06\x63hoice\x12\x46\n\x0f\x63hoice_argument\x18\x06 \x01(\x0b\x32\x1d.com.daml.ledger.api.v1.ValueR\x0e\x63hoiceArgument\x12%\n\x0e\x61\x63ting_parties\x18\x07 \x03(\tR\ractingParties\x12\x1c\n\tconsuming\x18\x08 \x01(\x08R\tconsuming\x12\'\n\x0fwitness_parties\x18\n \x03(\tR\x0ewitnessParties\x12&\n\x0f\x63hild_event_ids\x18\x0b \x03(\tR\rchildEventIds\x12\x46\n\x0f\x65xercise_result\x18\x0c \x01(\x0b\x32\x1d.com.daml.ledger.api.v1.ValueR\x0e\x65xerciseResultJ\x04\x08\x04\x10\x05J\x04\x08\t\x10\nB\x93\x01\n\x16\x63om.daml.ledger.api.v1B\x0f\x45ventOuterClassZOgithub.com/digital-asset/dazl-client/go/v7/pkg/generated/com/daml/ledger/api/v1\xaa\x02\x16\x43om.Daml.Ledger.Api.V1b\x06proto3'
  ,
  dependencies=[com_dot_daml_dot_ledger_dot_api_dot_v1_dot_value__pb2.DESCRIPTOR,google_dot_protobuf_dot_wrappers__pb2.DESCRIPTOR,])




_EVENT = _descriptor.Descriptor(
  name='Event',
  full_name='com.daml.ledger.api.v1.Event',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='created', full_name='com.daml.ledger.api.v1.Event.created', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='created', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='archived', full_name='com.daml.ledger.api.v1.Event.archived', index=1,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='archived', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='event', full_name='com.daml.ledger.api.v1.Event.event',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=131,
  serialized_end=299,
)


_CREATEDEVENT = _descriptor.Descriptor(
  name='CreatedEvent',
  full_name='com.daml.ledger.api.v1.CreatedEvent',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='event_id', full_name='com.daml.ledger.api.v1.CreatedEvent.event_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='eventId', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='contract_id', full_name='com.daml.ledger.api.v1.CreatedEvent.contract_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='contractId', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='template_id', full_name='com.daml.ledger.api.v1.CreatedEvent.template_id', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='templateId', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='contract_key', full_name='com.daml.ledger.api.v1.CreatedEvent.contract_key', index=3,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='contractKey', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='create_arguments', full_name='com.daml.ledger.api.v1.CreatedEvent.create_arguments', index=4,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='createArguments', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='witness_parties', full_name='com.daml.ledger.api.v1.CreatedEvent.witness_parties', index=5,
      number=5, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='witnessParties', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='signatories', full_name='com.daml.ledger.api.v1.CreatedEvent.signatories', index=6,
      number=8, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='signatories', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='observers', full_name='com.daml.ledger.api.v1.CreatedEvent.observers', index=7,
      number=9, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='observers', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='agreement_text', full_name='com.daml.ledger.api.v1.CreatedEvent.agreement_text', index=8,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='agreementText', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=302,
  serialized_end=760,
)


_ARCHIVEDEVENT = _descriptor.Descriptor(
  name='ArchivedEvent',
  full_name='com.daml.ledger.api.v1.ArchivedEvent',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='event_id', full_name='com.daml.ledger.api.v1.ArchivedEvent.event_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='eventId', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='contract_id', full_name='com.daml.ledger.api.v1.ArchivedEvent.contract_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='contractId', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='template_id', full_name='com.daml.ledger.api.v1.ArchivedEvent.template_id', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='templateId', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='witness_parties', full_name='com.daml.ledger.api.v1.ArchivedEvent.witness_parties', index=3,
      number=4, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='witnessParties', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=763,
  serialized_end=948,
)


_EXERCISEDEVENT = _descriptor.Descriptor(
  name='ExercisedEvent',
  full_name='com.daml.ledger.api.v1.ExercisedEvent',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='event_id', full_name='com.daml.ledger.api.v1.ExercisedEvent.event_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='eventId', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='contract_id', full_name='com.daml.ledger.api.v1.ExercisedEvent.contract_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='contractId', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='template_id', full_name='com.daml.ledger.api.v1.ExercisedEvent.template_id', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='templateId', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='choice', full_name='com.daml.ledger.api.v1.ExercisedEvent.choice', index=3,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='choice', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='choice_argument', full_name='com.daml.ledger.api.v1.ExercisedEvent.choice_argument', index=4,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='choiceArgument', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='acting_parties', full_name='com.daml.ledger.api.v1.ExercisedEvent.acting_parties', index=5,
      number=7, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='actingParties', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='consuming', full_name='com.daml.ledger.api.v1.ExercisedEvent.consuming', index=6,
      number=8, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='consuming', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='witness_parties', full_name='com.daml.ledger.api.v1.ExercisedEvent.witness_parties', index=7,
      number=10, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='witnessParties', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='child_event_ids', full_name='com.daml.ledger.api.v1.ExercisedEvent.child_event_ids', index=8,
      number=11, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='childEventIds', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='exercise_result', full_name='com.daml.ledger.api.v1.ExercisedEvent.exercise_result', index=9,
      number=12, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='exerciseResult', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=951,
  serialized_end=1426,
)

_EVENT.fields_by_name['created'].message_type = _CREATEDEVENT
_EVENT.fields_by_name['archived'].message_type = _ARCHIVEDEVENT
_EVENT.oneofs_by_name['event'].fields.append(
  _EVENT.fields_by_name['created'])
_EVENT.fields_by_name['created'].containing_oneof = _EVENT.oneofs_by_name['event']
_EVENT.oneofs_by_name['event'].fields.append(
  _EVENT.fields_by_name['archived'])
_EVENT.fields_by_name['archived'].containing_oneof = _EVENT.oneofs_by_name['event']
_CREATEDEVENT.fields_by_name['template_id'].message_type = com_dot_daml_dot_ledger_dot_api_dot_v1_dot_value__pb2._IDENTIFIER
_CREATEDEVENT.fields_by_name['contract_key'].message_type = com_dot_daml_dot_ledger_dot_api_dot_v1_dot_value__pb2._VALUE
_CREATEDEVENT.fields_by_name['create_arguments'].message_type = com_dot_daml_dot_ledger_dot_api_dot_v1_dot_value__pb2._RECORD
_CREATEDEVENT.fields_by_name['agreement_text'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_ARCHIVEDEVENT.fields_by_name['template_id'].message_type = com_dot_daml_dot_ledger_dot_api_dot_v1_dot_value__pb2._IDENTIFIER
_EXERCISEDEVENT.fields_by_name['template_id'].message_type = com_dot_daml_dot_ledger_dot_api_dot_v1_dot_value__pb2._IDENTIFIER
_EXERCISEDEVENT.fields_by_name['choice_argument'].message_type = com_dot_daml_dot_ledger_dot_api_dot_v1_dot_value__pb2._VALUE
_EXERCISEDEVENT.fields_by_name['exercise_result'].message_type = com_dot_daml_dot_ledger_dot_api_dot_v1_dot_value__pb2._VALUE
DESCRIPTOR.message_types_by_name['Event'] = _EVENT
DESCRIPTOR.message_types_by_name['CreatedEvent'] = _CREATEDEVENT
DESCRIPTOR.message_types_by_name['ArchivedEvent'] = _ARCHIVEDEVENT
DESCRIPTOR.message_types_by_name['ExercisedEvent'] = _EXERCISEDEVENT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Event = _reflection.GeneratedProtocolMessageType('Event', (_message.Message,), {
  'DESCRIPTOR' : _EVENT,
  '__module__' : 'com.daml.ledger.api.v1.event_pb2'
  # @@protoc_insertion_point(class_scope:com.daml.ledger.api.v1.Event)
  })
_sym_db.RegisterMessage(Event)

CreatedEvent = _reflection.GeneratedProtocolMessageType('CreatedEvent', (_message.Message,), {
  'DESCRIPTOR' : _CREATEDEVENT,
  '__module__' : 'com.daml.ledger.api.v1.event_pb2'
  # @@protoc_insertion_point(class_scope:com.daml.ledger.api.v1.CreatedEvent)
  })
_sym_db.RegisterMessage(CreatedEvent)

ArchivedEvent = _reflection.GeneratedProtocolMessageType('ArchivedEvent', (_message.Message,), {
  'DESCRIPTOR' : _ARCHIVEDEVENT,
  '__module__' : 'com.daml.ledger.api.v1.event_pb2'
  # @@protoc_insertion_point(class_scope:com.daml.ledger.api.v1.ArchivedEvent)
  })
_sym_db.RegisterMessage(ArchivedEvent)

ExercisedEvent = _reflection.GeneratedProtocolMessageType('ExercisedEvent', (_message.Message,), {
  'DESCRIPTOR' : _EXERCISEDEVENT,
  '__module__' : 'com.daml.ledger.api.v1.event_pb2'
  # @@protoc_insertion_point(class_scope:com.daml.ledger.api.v1.ExercisedEvent)
  })
_sym_db.RegisterMessage(ExercisedEvent)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
