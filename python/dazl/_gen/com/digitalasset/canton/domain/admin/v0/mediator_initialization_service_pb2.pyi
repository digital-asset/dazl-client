# Copyright (c) 2017-2024 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from ....crypto.v0 import crypto_pb2 as _crypto_pb2
from ...api.v0 import sequencer_connection_pb2 as _sequencer_connection_pb2
from ....protocol.v0 import sequencing_pb2 as _sequencing_pb2
from ....protocol.v0 import topology_ext_pb2 as _topology_ext_pb2
from google.protobuf import wrappers_pb2 as _wrappers_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class InitializeMediatorRequest(_message.Message):
    __slots__ = ["domain_id", "mediator_id", "current_identity_state", "domain_parameters", "sequencer_connection", "signing_key_fingerprint"]
    DOMAIN_ID_FIELD_NUMBER: _ClassVar[int]
    MEDIATOR_ID_FIELD_NUMBER: _ClassVar[int]
    CURRENT_IDENTITY_STATE_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    SEQUENCER_CONNECTION_FIELD_NUMBER: _ClassVar[int]
    SIGNING_KEY_FINGERPRINT_FIELD_NUMBER: _ClassVar[int]
    domain_id: str
    mediator_id: str
    current_identity_state: _topology_ext_pb2.TopologyTransactions
    domain_parameters: _sequencing_pb2.StaticDomainParameters
    sequencer_connection: _sequencer_connection_pb2.SequencerConnection
    signing_key_fingerprint: _wrappers_pb2.StringValue
    def __init__(self, domain_id: _Optional[str] = ..., mediator_id: _Optional[str] = ..., current_identity_state: _Optional[_Union[_topology_ext_pb2.TopologyTransactions, _Mapping]] = ..., domain_parameters: _Optional[_Union[_sequencing_pb2.StaticDomainParameters, _Mapping]] = ..., sequencer_connection: _Optional[_Union[_sequencer_connection_pb2.SequencerConnection, _Mapping]] = ..., signing_key_fingerprint: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ...) -> None: ...

class InitializeMediatorResponse(_message.Message):
    __slots__ = ["success", "failure"]
    class Success(_message.Message):
        __slots__ = ["mediator_key"]
        MEDIATOR_KEY_FIELD_NUMBER: _ClassVar[int]
        mediator_key: _crypto_pb2.SigningPublicKey
        def __init__(self, mediator_key: _Optional[_Union[_crypto_pb2.SigningPublicKey, _Mapping]] = ...) -> None: ...
    class Failure(_message.Message):
        __slots__ = ["reason"]
        REASON_FIELD_NUMBER: _ClassVar[int]
        reason: str
        def __init__(self, reason: _Optional[str] = ...) -> None: ...
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: InitializeMediatorResponse.Success
    failure: InitializeMediatorResponse.Failure
    def __init__(self, success: _Optional[_Union[InitializeMediatorResponse.Success, _Mapping]] = ..., failure: _Optional[_Union[InitializeMediatorResponse.Failure, _Mapping]] = ...) -> None: ...
