# Copyright (c) 2017-2024 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from ....domain.api.v0 import sequencer_connection_pb2 as _sequencer_connection_pb2
from ....time.admin.v0 import time_tracker_config_pb2 as _time_tracker_config_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DomainConnectionConfig(_message.Message):
    __slots__ = ["domain_alias", "sequencerConnections", "manual_connect", "domain_id", "priority", "initialRetryDelay", "maxRetryDelay", "timeTracker", "sequencerTrustThreshold"]
    DOMAIN_ALIAS_FIELD_NUMBER: _ClassVar[int]
    SEQUENCERCONNECTIONS_FIELD_NUMBER: _ClassVar[int]
    MANUAL_CONNECT_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_ID_FIELD_NUMBER: _ClassVar[int]
    PRIORITY_FIELD_NUMBER: _ClassVar[int]
    INITIALRETRYDELAY_FIELD_NUMBER: _ClassVar[int]
    MAXRETRYDELAY_FIELD_NUMBER: _ClassVar[int]
    TIMETRACKER_FIELD_NUMBER: _ClassVar[int]
    SEQUENCERTRUSTTHRESHOLD_FIELD_NUMBER: _ClassVar[int]
    domain_alias: str
    sequencerConnections: _containers.RepeatedCompositeFieldContainer[_sequencer_connection_pb2.SequencerConnection]
    manual_connect: bool
    domain_id: str
    priority: int
    initialRetryDelay: _duration_pb2.Duration
    maxRetryDelay: _duration_pb2.Duration
    timeTracker: _time_tracker_config_pb2.DomainTimeTrackerConfig
    sequencerTrustThreshold: int
    def __init__(self, domain_alias: _Optional[str] = ..., sequencerConnections: _Optional[_Iterable[_Union[_sequencer_connection_pb2.SequencerConnection, _Mapping]]] = ..., manual_connect: bool = ..., domain_id: _Optional[str] = ..., priority: _Optional[int] = ..., initialRetryDelay: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., maxRetryDelay: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., timeTracker: _Optional[_Union[_time_tracker_config_pb2.DomainTimeTrackerConfig, _Mapping]] = ..., sequencerTrustThreshold: _Optional[int] = ...) -> None: ...

class ReconnectDomainsRequest(_message.Message):
    __slots__ = ["ignore_failures"]
    IGNORE_FAILURES_FIELD_NUMBER: _ClassVar[int]
    ignore_failures: bool
    def __init__(self, ignore_failures: bool = ...) -> None: ...

class ReconnectDomainsResponse(_message.Message):
    __slots__ = []  # type: ignore
    def __init__(self) -> None: ...

class RegisterDomainRequest(_message.Message):
    __slots__ = ["add"]
    ADD_FIELD_NUMBER: _ClassVar[int]
    add: DomainConnectionConfig
    def __init__(self, add: _Optional[_Union[DomainConnectionConfig, _Mapping]] = ...) -> None: ...

class RegisterDomainResponse(_message.Message):
    __slots__ = []  # type: ignore
    def __init__(self) -> None: ...

class ModifyDomainRequest(_message.Message):
    __slots__ = ["modify"]
    MODIFY_FIELD_NUMBER: _ClassVar[int]
    modify: DomainConnectionConfig
    def __init__(self, modify: _Optional[_Union[DomainConnectionConfig, _Mapping]] = ...) -> None: ...

class ModifyDomainResponse(_message.Message):
    __slots__ = []  # type: ignore
    def __init__(self) -> None: ...

class ListConfiguredDomainsRequest(_message.Message):
    __slots__ = []  # type: ignore
    def __init__(self) -> None: ...

class ListConfiguredDomainsResponse(_message.Message):
    __slots__ = ["results"]
    class Result(_message.Message):
        __slots__ = ["config", "connected"]
        CONFIG_FIELD_NUMBER: _ClassVar[int]
        CONNECTED_FIELD_NUMBER: _ClassVar[int]
        config: DomainConnectionConfig
        connected: bool
        def __init__(self, config: _Optional[_Union[DomainConnectionConfig, _Mapping]] = ..., connected: bool = ...) -> None: ...
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    results: _containers.RepeatedCompositeFieldContainer[ListConfiguredDomainsResponse.Result]
    def __init__(self, results: _Optional[_Iterable[_Union[ListConfiguredDomainsResponse.Result, _Mapping]]] = ...) -> None: ...

class ConnectDomainRequest(_message.Message):
    __slots__ = ["domain_alias", "retry"]
    DOMAIN_ALIAS_FIELD_NUMBER: _ClassVar[int]
    RETRY_FIELD_NUMBER: _ClassVar[int]
    domain_alias: str
    retry: bool
    def __init__(self, domain_alias: _Optional[str] = ..., retry: bool = ...) -> None: ...

class ConnectDomainResponse(_message.Message):
    __slots__ = ["connected_successfully"]
    CONNECTED_SUCCESSFULLY_FIELD_NUMBER: _ClassVar[int]
    connected_successfully: bool
    def __init__(self, connected_successfully: bool = ...) -> None: ...

class DisconnectDomainRequest(_message.Message):
    __slots__ = ["domain_alias"]
    DOMAIN_ALIAS_FIELD_NUMBER: _ClassVar[int]
    domain_alias: str
    def __init__(self, domain_alias: _Optional[str] = ...) -> None: ...

class DisconnectDomainResponse(_message.Message):
    __slots__ = []  # type: ignore
    def __init__(self) -> None: ...

class ListConnectedDomainsRequest(_message.Message):
    __slots__ = []  # type: ignore
    def __init__(self) -> None: ...

class ListConnectedDomainsResponse(_message.Message):
    __slots__ = ["connected_domains"]
    class Result(_message.Message):
        __slots__ = ["domain_alias", "domain_id", "healthy"]
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

class GetAgreementRequest(_message.Message):
    __slots__ = ["domain_alias"]
    DOMAIN_ALIAS_FIELD_NUMBER: _ClassVar[int]
    domain_alias: str
    def __init__(self, domain_alias: _Optional[str] = ...) -> None: ...

class GetAgreementResponse(_message.Message):
    __slots__ = ["domain_id", "agreement", "accepted"]
    DOMAIN_ID_FIELD_NUMBER: _ClassVar[int]
    AGREEMENT_FIELD_NUMBER: _ClassVar[int]
    ACCEPTED_FIELD_NUMBER: _ClassVar[int]
    domain_id: str
    agreement: Agreement
    accepted: bool
    def __init__(self, domain_id: _Optional[str] = ..., agreement: _Optional[_Union[Agreement, _Mapping]] = ..., accepted: bool = ...) -> None: ...

class Agreement(_message.Message):
    __slots__ = ["id", "text"]
    ID_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    id: str
    text: str
    def __init__(self, id: _Optional[str] = ..., text: _Optional[str] = ...) -> None: ...

class AcceptAgreementRequest(_message.Message):
    __slots__ = ["domain_alias", "agreement_id"]
    DOMAIN_ALIAS_FIELD_NUMBER: _ClassVar[int]
    AGREEMENT_ID_FIELD_NUMBER: _ClassVar[int]
    domain_alias: str
    agreement_id: str
    def __init__(self, domain_alias: _Optional[str] = ..., agreement_id: _Optional[str] = ...) -> None: ...

class AcceptAgreementResponse(_message.Message):
    __slots__ = []  # type: ignore
    def __init__(self) -> None: ...

class GetDomainIdRequest(_message.Message):
    __slots__ = ["domain_alias"]
    DOMAIN_ALIAS_FIELD_NUMBER: _ClassVar[int]
    domain_alias: str
    def __init__(self, domain_alias: _Optional[str] = ...) -> None: ...

class GetDomainIdResponse(_message.Message):
    __slots__ = ["domain_id"]
    DOMAIN_ID_FIELD_NUMBER: _ClassVar[int]
    domain_id: str
    def __init__(self, domain_id: _Optional[str] = ...) -> None: ...
