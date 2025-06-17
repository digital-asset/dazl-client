# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from ...sequencer.v30 import sequencer_connection_pb2 as _sequencer_connection_pb2
from ...time.v30 import time_tracker_config_pb2 as _time_tracker_config_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SynchronizerConnectionConfig(_message.Message):
    __slots__ = ("synchronizer_alias", "sequencer_connections", "manual_connect", "synchronizer_id", "priority", "initial_retry_delay", "max_retry_delay", "time_tracker", "initialize_from_trusted_synchronizer")
    SYNCHRONIZER_ALIAS_FIELD_NUMBER: _ClassVar[int]
    SEQUENCER_CONNECTIONS_FIELD_NUMBER: _ClassVar[int]
    MANUAL_CONNECT_FIELD_NUMBER: _ClassVar[int]
    SYNCHRONIZER_ID_FIELD_NUMBER: _ClassVar[int]
    PRIORITY_FIELD_NUMBER: _ClassVar[int]
    INITIAL_RETRY_DELAY_FIELD_NUMBER: _ClassVar[int]
    MAX_RETRY_DELAY_FIELD_NUMBER: _ClassVar[int]
    TIME_TRACKER_FIELD_NUMBER: _ClassVar[int]
    INITIALIZE_FROM_TRUSTED_SYNCHRONIZER_FIELD_NUMBER: _ClassVar[int]
    synchronizer_alias: str
    sequencer_connections: _sequencer_connection_pb2.SequencerConnections
    manual_connect: bool
    synchronizer_id: str
    priority: int
    initial_retry_delay: _duration_pb2.Duration
    max_retry_delay: _duration_pb2.Duration
    time_tracker: _time_tracker_config_pb2.SynchronizerTimeTrackerConfig
    initialize_from_trusted_synchronizer: bool
    def __init__(self, synchronizer_alias: _Optional[str] = ..., sequencer_connections: _Optional[_Union[_sequencer_connection_pb2.SequencerConnections, _Mapping]] = ..., manual_connect: bool = ..., synchronizer_id: _Optional[str] = ..., priority: _Optional[int] = ..., initial_retry_delay: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., max_retry_delay: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., time_tracker: _Optional[_Union[_time_tracker_config_pb2.SynchronizerTimeTrackerConfig, _Mapping]] = ..., initialize_from_trusted_synchronizer: bool = ...) -> None: ...

class ReconnectSynchronizersRequest(_message.Message):
    __slots__ = ("ignore_failures",)
    IGNORE_FAILURES_FIELD_NUMBER: _ClassVar[int]
    ignore_failures: bool
    def __init__(self, ignore_failures: bool = ...) -> None: ...

class ReconnectSynchronizersResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class RegisterSynchronizerRequest(_message.Message):
    __slots__ = ("config", "synchronizer_connection", "sequencer_connection_validation")
    class SynchronizerConnection(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SYNCHRONIZER_CONNECTION_UNSPECIFIED: _ClassVar[RegisterSynchronizerRequest.SynchronizerConnection]
        SYNCHRONIZER_CONNECTION_NONE: _ClassVar[RegisterSynchronizerRequest.SynchronizerConnection]
        SYNCHRONIZER_CONNECTION_HANDSHAKE: _ClassVar[RegisterSynchronizerRequest.SynchronizerConnection]
    SYNCHRONIZER_CONNECTION_UNSPECIFIED: RegisterSynchronizerRequest.SynchronizerConnection
    SYNCHRONIZER_CONNECTION_NONE: RegisterSynchronizerRequest.SynchronizerConnection
    SYNCHRONIZER_CONNECTION_HANDSHAKE: RegisterSynchronizerRequest.SynchronizerConnection
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    SYNCHRONIZER_CONNECTION_FIELD_NUMBER: _ClassVar[int]
    SEQUENCER_CONNECTION_VALIDATION_FIELD_NUMBER: _ClassVar[int]
    config: SynchronizerConnectionConfig
    synchronizer_connection: RegisterSynchronizerRequest.SynchronizerConnection
    sequencer_connection_validation: _sequencer_connection_pb2.SequencerConnectionValidation
    def __init__(self, config: _Optional[_Union[SynchronizerConnectionConfig, _Mapping]] = ..., synchronizer_connection: _Optional[_Union[RegisterSynchronizerRequest.SynchronizerConnection, str]] = ..., sequencer_connection_validation: _Optional[_Union[_sequencer_connection_pb2.SequencerConnectionValidation, str]] = ...) -> None: ...

class RegisterSynchronizerResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ModifySynchronizerRequest(_message.Message):
    __slots__ = ("new_config", "sequencer_connection_validation")
    NEW_CONFIG_FIELD_NUMBER: _ClassVar[int]
    SEQUENCER_CONNECTION_VALIDATION_FIELD_NUMBER: _ClassVar[int]
    new_config: SynchronizerConnectionConfig
    sequencer_connection_validation: _sequencer_connection_pb2.SequencerConnectionValidation
    def __init__(self, new_config: _Optional[_Union[SynchronizerConnectionConfig, _Mapping]] = ..., sequencer_connection_validation: _Optional[_Union[_sequencer_connection_pb2.SequencerConnectionValidation, str]] = ...) -> None: ...

class ModifySynchronizerResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListRegisteredSynchronizersRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListRegisteredSynchronizersResponse(_message.Message):
    __slots__ = ("results",)
    class Result(_message.Message):
        __slots__ = ("config", "connected")
        CONFIG_FIELD_NUMBER: _ClassVar[int]
        CONNECTED_FIELD_NUMBER: _ClassVar[int]
        config: SynchronizerConnectionConfig
        connected: bool
        def __init__(self, config: _Optional[_Union[SynchronizerConnectionConfig, _Mapping]] = ..., connected: bool = ...) -> None: ...
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    results: _containers.RepeatedCompositeFieldContainer[ListRegisteredSynchronizersResponse.Result]
    def __init__(self, results: _Optional[_Iterable[_Union[ListRegisteredSynchronizersResponse.Result, _Mapping]]] = ...) -> None: ...

class ReconnectSynchronizerRequest(_message.Message):
    __slots__ = ("synchronizer_alias", "retry")
    SYNCHRONIZER_ALIAS_FIELD_NUMBER: _ClassVar[int]
    RETRY_FIELD_NUMBER: _ClassVar[int]
    synchronizer_alias: str
    retry: bool
    def __init__(self, synchronizer_alias: _Optional[str] = ..., retry: bool = ...) -> None: ...

class ReconnectSynchronizerResponse(_message.Message):
    __slots__ = ("connected_successfully",)
    CONNECTED_SUCCESSFULLY_FIELD_NUMBER: _ClassVar[int]
    connected_successfully: bool
    def __init__(self, connected_successfully: bool = ...) -> None: ...

class ConnectSynchronizerRequest(_message.Message):
    __slots__ = ("config", "sequencer_connection_validation")
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    SEQUENCER_CONNECTION_VALIDATION_FIELD_NUMBER: _ClassVar[int]
    config: SynchronizerConnectionConfig
    sequencer_connection_validation: _sequencer_connection_pb2.SequencerConnectionValidation
    def __init__(self, config: _Optional[_Union[SynchronizerConnectionConfig, _Mapping]] = ..., sequencer_connection_validation: _Optional[_Union[_sequencer_connection_pb2.SequencerConnectionValidation, str]] = ...) -> None: ...

class ConnectSynchronizerResponse(_message.Message):
    __slots__ = ("connected_successfully",)
    CONNECTED_SUCCESSFULLY_FIELD_NUMBER: _ClassVar[int]
    connected_successfully: bool
    def __init__(self, connected_successfully: bool = ...) -> None: ...

class DisconnectSynchronizerRequest(_message.Message):
    __slots__ = ("synchronizer_alias",)
    SYNCHRONIZER_ALIAS_FIELD_NUMBER: _ClassVar[int]
    synchronizer_alias: str
    def __init__(self, synchronizer_alias: _Optional[str] = ...) -> None: ...

class DisconnectSynchronizerResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DisconnectAllSynchronizersRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DisconnectAllSynchronizersResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListConnectedSynchronizersRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListConnectedSynchronizersResponse(_message.Message):
    __slots__ = ("connected_synchronizers",)
    class Result(_message.Message):
        __slots__ = ("synchronizer_alias", "synchronizer_id", "healthy")
        SYNCHRONIZER_ALIAS_FIELD_NUMBER: _ClassVar[int]
        SYNCHRONIZER_ID_FIELD_NUMBER: _ClassVar[int]
        HEALTHY_FIELD_NUMBER: _ClassVar[int]
        synchronizer_alias: str
        synchronizer_id: str
        healthy: bool
        def __init__(self, synchronizer_alias: _Optional[str] = ..., synchronizer_id: _Optional[str] = ..., healthy: bool = ...) -> None: ...
    CONNECTED_SYNCHRONIZERS_FIELD_NUMBER: _ClassVar[int]
    connected_synchronizers: _containers.RepeatedCompositeFieldContainer[ListConnectedSynchronizersResponse.Result]
    def __init__(self, connected_synchronizers: _Optional[_Iterable[_Union[ListConnectedSynchronizersResponse.Result, _Mapping]]] = ...) -> None: ...

class GetSynchronizerIdRequest(_message.Message):
    __slots__ = ("synchronizer_alias",)
    SYNCHRONIZER_ALIAS_FIELD_NUMBER: _ClassVar[int]
    synchronizer_alias: str
    def __init__(self, synchronizer_alias: _Optional[str] = ...) -> None: ...

class GetSynchronizerIdResponse(_message.Message):
    __slots__ = ("synchronizer_id",)
    SYNCHRONIZER_ID_FIELD_NUMBER: _ClassVar[int]
    synchronizer_id: str
    def __init__(self, synchronizer_id: _Optional[str] = ...) -> None: ...

class LogoutRequest(_message.Message):
    __slots__ = ("synchronizer_alias",)
    SYNCHRONIZER_ALIAS_FIELD_NUMBER: _ClassVar[int]
    synchronizer_alias: str
    def __init__(self, synchronizer_alias: _Optional[str] = ...) -> None: ...

class LogoutResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
