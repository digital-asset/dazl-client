# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from . import traffic_control_parameters_pb2 as _traffic_control_parameters_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class OnboardingRestriction(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ONBOARDING_RESTRICTION_UNSPECIFIED: _ClassVar[OnboardingRestriction]
    ONBOARDING_RESTRICTION_UNRESTRICTED_OPEN: _ClassVar[OnboardingRestriction]
    ONBOARDING_RESTRICTION_UNRESTRICTED_LOCKED: _ClassVar[OnboardingRestriction]
    ONBOARDING_RESTRICTION_RESTRICTED_OPEN: _ClassVar[OnboardingRestriction]
    ONBOARDING_RESTRICTION_RESTRICTED_LOCKED: _ClassVar[OnboardingRestriction]
ONBOARDING_RESTRICTION_UNSPECIFIED: OnboardingRestriction
ONBOARDING_RESTRICTION_UNRESTRICTED_OPEN: OnboardingRestriction
ONBOARDING_RESTRICTION_UNRESTRICTED_LOCKED: OnboardingRestriction
ONBOARDING_RESTRICTION_RESTRICTED_OPEN: OnboardingRestriction
ONBOARDING_RESTRICTION_RESTRICTED_LOCKED: OnboardingRestriction

class AcsCommitmentsCatchUpConfig(_message.Message):
    __slots__ = ("catchup_interval_skip", "nr_intervals_to_trigger_catchup")
    CATCHUP_INTERVAL_SKIP_FIELD_NUMBER: _ClassVar[int]
    NR_INTERVALS_TO_TRIGGER_CATCHUP_FIELD_NUMBER: _ClassVar[int]
    catchup_interval_skip: int
    nr_intervals_to_trigger_catchup: int
    def __init__(self, catchup_interval_skip: _Optional[int] = ..., nr_intervals_to_trigger_catchup: _Optional[int] = ...) -> None: ...

class ParticipantDomainLimits(_message.Message):
    __slots__ = ("confirmation_requests_max_rate", "max_num_parties", "max_num_packages")
    CONFIRMATION_REQUESTS_MAX_RATE_FIELD_NUMBER: _ClassVar[int]
    MAX_NUM_PARTIES_FIELD_NUMBER: _ClassVar[int]
    MAX_NUM_PACKAGES_FIELD_NUMBER: _ClassVar[int]
    confirmation_requests_max_rate: int
    max_num_parties: int
    max_num_packages: int
    def __init__(self, confirmation_requests_max_rate: _Optional[int] = ..., max_num_parties: _Optional[int] = ..., max_num_packages: _Optional[int] = ...) -> None: ...

class DynamicDomainParameters(_message.Message):
    __slots__ = ("confirmation_response_timeout", "mediator_reaction_timeout", "transfer_exclusivity_timeout", "topology_change_delay", "ledger_time_record_time_tolerance", "reconciliation_interval", "mediator_deduplication_timeout", "max_request_size", "onboarding_restriction", "required_packages", "only_required_packages_permitted", "default_participant_limits", "default_max_hosting_participants_per_party", "sequencer_aggregate_submission_timeout", "traffic_control_parameters", "acs_commitments_catchup_config")
    CONFIRMATION_RESPONSE_TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    MEDIATOR_REACTION_TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    TRANSFER_EXCLUSIVITY_TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    TOPOLOGY_CHANGE_DELAY_FIELD_NUMBER: _ClassVar[int]
    LEDGER_TIME_RECORD_TIME_TOLERANCE_FIELD_NUMBER: _ClassVar[int]
    RECONCILIATION_INTERVAL_FIELD_NUMBER: _ClassVar[int]
    MEDIATOR_DEDUPLICATION_TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    MAX_REQUEST_SIZE_FIELD_NUMBER: _ClassVar[int]
    ONBOARDING_RESTRICTION_FIELD_NUMBER: _ClassVar[int]
    REQUIRED_PACKAGES_FIELD_NUMBER: _ClassVar[int]
    ONLY_REQUIRED_PACKAGES_PERMITTED_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_PARTICIPANT_LIMITS_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_MAX_HOSTING_PARTICIPANTS_PER_PARTY_FIELD_NUMBER: _ClassVar[int]
    SEQUENCER_AGGREGATE_SUBMISSION_TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    TRAFFIC_CONTROL_PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    ACS_COMMITMENTS_CATCHUP_CONFIG_FIELD_NUMBER: _ClassVar[int]
    confirmation_response_timeout: _duration_pb2.Duration
    mediator_reaction_timeout: _duration_pb2.Duration
    transfer_exclusivity_timeout: _duration_pb2.Duration
    topology_change_delay: _duration_pb2.Duration
    ledger_time_record_time_tolerance: _duration_pb2.Duration
    reconciliation_interval: _duration_pb2.Duration
    mediator_deduplication_timeout: _duration_pb2.Duration
    max_request_size: int
    onboarding_restriction: OnboardingRestriction
    required_packages: _containers.RepeatedScalarFieldContainer[str]
    only_required_packages_permitted: bool
    default_participant_limits: ParticipantDomainLimits
    default_max_hosting_participants_per_party: int
    sequencer_aggregate_submission_timeout: _duration_pb2.Duration
    traffic_control_parameters: _traffic_control_parameters_pb2.TrafficControlParameters
    acs_commitments_catchup_config: AcsCommitmentsCatchUpConfig
    def __init__(self, confirmation_response_timeout: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., mediator_reaction_timeout: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., transfer_exclusivity_timeout: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., topology_change_delay: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., ledger_time_record_time_tolerance: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., reconciliation_interval: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., mediator_deduplication_timeout: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., max_request_size: _Optional[int] = ..., onboarding_restriction: _Optional[_Union[OnboardingRestriction, str]] = ..., required_packages: _Optional[_Iterable[str]] = ..., only_required_packages_permitted: bool = ..., default_participant_limits: _Optional[_Union[ParticipantDomainLimits, _Mapping]] = ..., default_max_hosting_participants_per_party: _Optional[int] = ..., sequencer_aggregate_submission_timeout: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., traffic_control_parameters: _Optional[_Union[_traffic_control_parameters_pb2.TrafficControlParameters, _Mapping]] = ..., acs_commitments_catchup_config: _Optional[_Union[AcsCommitmentsCatchUpConfig, _Mapping]] = ...) -> None: ...
