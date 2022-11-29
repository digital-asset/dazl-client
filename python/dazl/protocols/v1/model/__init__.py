# Copyright (c) 2017-2022 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import warnings

warnings.warn(
    "dazl.protocols.v1.model is deprecated; use the types in dazl._gen instead",
    DeprecationWarning,
    stacklevel=2,
)

from ...._gen.com.daml.daml_lf_1_15.daml_lf_1_pb2 import (
    DefDataType,
    DefTemplate,
    PrimType,
    TemplateChoice,
)
from ...._gen.com.daml.daml_lf_1_15.daml_lf_pb2 import ArchivePayload
from ...._gen.com.daml.ledger.api.v1.active_contracts_service_pb2 import (
    GetActiveContractsRequest,
    GetActiveContractsResponse,
)
from ...._gen.com.daml.ledger.api.v1.active_contracts_service_pb2_grpc import (
    ActiveContractsServiceStub,
)
from ...._gen.com.daml.ledger.api.v1.admin.package_management_service_pb2 import (
    UploadDarFileRequest,
    UploadDarFileResponse,
)
from ...._gen.com.daml.ledger.api.v1.admin.package_management_service_pb2_grpc import (
    PackageManagementServiceStub,
)
from ...._gen.com.daml.ledger.api.v1.command_service_pb2_grpc import CommandServiceStub
from ...._gen.com.daml.ledger.api.v1.command_submission_service_pb2 import SubmitRequest
from ...._gen.com.daml.ledger.api.v1.commands_pb2 import (
    Command,
    Commands,
    CreateAndExerciseCommand,
    CreateCommand,
    ExerciseByKeyCommand,
    ExerciseCommand,
)
from ...._gen.com.daml.ledger.api.v1.event_pb2 import Event
from ...._gen.com.daml.ledger.api.v1.ledger_identity_service_pb2 import GetLedgerIdentityRequest
from ...._gen.com.daml.ledger.api.v1.ledger_identity_service_pb2_grpc import (
    LedgerIdentityServiceStub,
)
from ...._gen.com.daml.ledger.api.v1.ledger_offset_pb2 import LedgerOffset
from ...._gen.com.daml.ledger.api.v1.package_service_pb2 import (
    GetPackageRequest,
    ListPackagesRequest,
)
from ...._gen.com.daml.ledger.api.v1.package_service_pb2_grpc import PackageServiceStub
from ...._gen.com.daml.ledger.api.v1.testing.time_service_pb2 import GetTimeRequest, SetTimeRequest
from ...._gen.com.daml.ledger.api.v1.testing.time_service_pb2_grpc import TimeServiceStub
from ...._gen.com.daml.ledger.api.v1.transaction_filter_pb2 import (
    Filters,
    InclusiveFilters,
    TransactionFilter,
)
from ...._gen.com.daml.ledger.api.v1.transaction_pb2 import Transaction
from ...._gen.com.daml.ledger.api.v1.transaction_service_pb2 import (
    GetLedgerEndRequest,
    GetTransactionByEventIdRequest,
    GetTransactionsRequest,
    GetTransactionsResponse,
)
from ...._gen.com.daml.ledger.api.v1.transaction_service_pb2_grpc import TransactionServiceStub
from ...._gen.com.daml.ledger.api.v1.value_pb2 import (
    Identifier,
    List,
    Record,
    RecordField,
    Value,
    Variant,
)
