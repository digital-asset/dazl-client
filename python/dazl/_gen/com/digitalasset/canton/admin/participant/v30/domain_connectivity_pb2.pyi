# Copyright (c) 2017-2024 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from ...time.v30 import time_tracker_config_pb2 as _time_tracker_config_pb2
from ...domain.v30 import sequencer_connection_pb2 as _sequencer_connection_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DomainConnectionConfig(_message.Message):
    __slots__ = ("domain_alias", "sequencer_connections", "manual_connect", "domain_id", "priority", "initial_retry_delay", "max_retry_delay", "time_tracker", "initialize_from_trusted_domain")
    DOMAIN_ALIAS_FIELD_NUMBER: _ClassVar[int]
    SEQUENCER_CONNECTIONS_FIELD_NUMBER: _ClassVar[int]
    MANUAL_CONNECT_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_ID_FIELD_NUMBER: _ClassVar[int]
    PRIORITY_FIELD_NUMBER: _ClassVar[int]
    INITIAL_RETRY_DELAY_FIELD_NUMBER: _ClassVar[int]
    MAX_RETRY_DELAY_FIELD_NUMBER: _ClassVar[int]
    TIME_TRACKER_FIELD_NUMBER: _ClassVar[int]
    INITIALIZE_FROM_TRUSTED_DOMAIN_FIELD_NUMBER: _ClassVar[int]
    domain_alias: str
    sequencer_connections: _sequencer_connection_pb2.SequencerConnections
    manual_connect: bool
    domain_id: str
    priority: int
    initial_retry_delay: _duration_pb2.Duration
    max_retry_delay: _duration_pb2.Duration
    time_tracker: _time_tracker_config_pb2.DomainTimeTrackerConfig
    initialize_from_trusted_domain: bool
    def __init__(self, domain_alias: _Optional[str] = ..., sequencer_connections: _Optional[_Union[_sequencer_connection_pb2.SequencerConnections, _Mapping]] = ..., manual_connect: bool = ..., domain_id: _Optional[str] = ..., priority: _Optional[int] = ..., initial_retry_delay: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., max_retry_delay: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., time_tracker: _Optional[_Union[_time_tracker_config_pb2.DomainTimeTrackerConfig, _Mapping]] = ..., initialize_from_trusted_domain: bool = ...) -> None: ...

class ReconnectDomainsRequest(_message.Message):
    __slots__ = ("ignore_failures",)
    IGNORE_FAILURES_FIELD_NUMBER: _ClassVar[int]
    ignore_failures: bool
    def __init__(self, ignore_failures: bool = ...) -> None: ...

class ReconnectDomainsResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class RegisterDomainRequest(_message.Message):
    __slots__ = ("add", "handshake_only", "sequencer_connection_validation")
    ADD_FIELD_NUMBER: _ClassVar[int]
    HANDSHAKE_ONLY_FIELD_NUMBER: _ClassVar[int]
    SEQUENCER_CONNECTION_VALIDATION_FIELD_NUMBER: _ClassVar[int]
    add: DomainConnectionConfig
    handshake_only: bool
    sequencer_connection_validation: _sequencer_connection_pb2.SequencerConnectionValidation
    def __init__(self, add: _Optional[_Union[DomainConnectionConfig, _Mapping]] = ..., handshake_only: bool = ..., sequencer_connection_validation: _Optional[_Union[_sequencer_connection_pb2.SequencerConnectionValidation, str]] = ...) -> None: ...

class RegisterDomainResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ModifyDomainRequest(_message.Message):
    __slots__ = ("modify", "sequencer_connection_validation")
    MODIFY_FIELD_NUMBER: _ClassVar[int]
    SEQUENCER_CONNECTION_VALIDATION_FIELD_NUMBER: _ClassVar[int]
    modify: DomainConnectionConfig
    sequencer_connection_validation: _sequencer_connection_pb2.SequencerConnectionValidation
    def __init__(self, modify: _Optional[_Union[DomainConnectionConfig, _Mapping]] = ..., sequencer_connection_validation: _Optional[_Union[_sequencer_connection_pb2.SequencerConnectionValidation, str]] = ...) -> None: ...

class ModifyDomainResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListConfiguredDomainsRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListConfiguredDomainsResponse(_message.Message):
    __slots__ = ("results",)
    class Result(_message.Message):
        __slots__ = ("config", "connected")
        CONFIG_FIELD_NUMBER: _ClassVar[int]
        CONNECTED_FIELD_NUMBER: _ClassVar[int]
        config: DomainConnectionConfig
        connected: bool
        def __init__(self, config: _Optional[_Union[DomainConnectionConfig, _Mapping]] = ..., connected: bool = ...) -> None: ...
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    results: _containers.RepeatedCompositeFieldContainer[ListConfiguredDomainsResponse.Result]
    def __init__(self, results: _Optional[_Iterable[_Union[ListConfiguredDomainsResponse.Result, _Mapping]]] = ...) -> None: ...

class ConnectDomainRequest(_message.Message):
    __slots__ = ("domain_alias", "retry")
    DOMAIN_ALIAS_FIELD_NUMBER: _ClassVar[int]
    RETRY_FIELD_NUMBER: _ClassVar[int]
    domain_alias: str
    retry: bool
    def __init__(self, domain_alias: _Optional[str] = ..., retry: bool = ...) -> None: ...

class ConnectDomainResponse(_message.Message):
    __slots__ = ("connected_successfully",)
    CONNECTED_SUCCESSFULLY_FIELD_NUMBER: _ClassVar[int]
    connected_successfully: bool
    def __init__(self, connected_successfully: bool = ...) -> None: ...

class DisconnectDomainRequest(_message.Message):
    __slots__ = ("domain_alias",)
    DOMAIN_ALIAS_FIELD_NUMBER: _ClassVar[int]
    domain_alias: str
    def __init__(self, domain_alias: _Optional[str] = ...) -> None: ...

class DisconnectDomainResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListConnectedDomainsRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListConnectedDomainsResponse(_message.Message):
    __slots__ = ("connected_domains",)
    class Result(_message.Message):
        __slots__ = ("domain_alias", "domain_id", "healthy")
        DOMAIN_ALIAS_FIELD_NUMBER: _ClassVar[int]
        DOMAIN_ID_FIELD_NUMBER: _ClassVar[int]
        HEALTHY_FIELD_NUMBER: _ClassVar[int]
        domain_alias: str
        domain_id: str
        healthy: bool
        def __init__(self, domain_alias: _Optional[str] = ..., domain_id: _Optional[str] = ..., healthy: bool = ...) -> None: ...
    CONNECTED_DOMAINS_FIELD_NUMBER: _ClassVar[int]
    connected_domains: _containers.RepeatedCompositeFieldContainer[ListConnectedDomainsResponse.Result]
    def __init__(self, connected_domains: _Optional[_Iterable[_Union[ListConnectedDomainsResponse.Result, _Mapping]]] = ...) -> None: ...

class GetDomainIdRequest(_message.Message):
    __slots__ = ("domain_alias",)
    DOMAIN_ALIAS_FIELD_NUMBER: _ClassVar[int]
    domain_alias: str
    def __init__(self, domain_alias: _Optional[str] = ...) -> None: ...

class GetDomainIdResponse(_message.Message):
    __slots__ = ("domain_id",)
    DOMAIN_ID_FIELD_NUMBER: _ClassVar[int]
    domain_id: str
    def __init__(self, domain_id: _Optional[str] = ...) -> None: ...
