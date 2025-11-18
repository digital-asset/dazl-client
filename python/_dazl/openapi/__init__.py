# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Dict, List, Optional

import yaml

__all__ = ["OpenAPISpec", "Operation", "Parameter", "Schema", "parse_openapi"]


@dataclass
class Parameter:
    name: str
    location: str
    required: bool
    schema: Schema
    description: Optional[str] = None


@dataclass
class Schema:
    type: str
    format: Optional[str] = None
    ref: Optional[str] = None
    items: Optional[Schema] = None
    properties: Dict[str, Schema] = field(default_factory=dict)
    required: List[str] = field(default_factory=list)
    additional_properties: Optional[Schema | bool] = None
    enum: List[Any] = field(default_factory=list)
    default: Optional[Any] = None


@dataclass
class Response:
    status_code: str
    description: str
    schema: Optional[Schema] = None


@dataclass
class Operation:
    operation_id: str
    method: str
    path: str
    description: Optional[str]
    parameters: List[Parameter]
    responses: List[Response]
    request_body: Optional[Schema] = None


@dataclass
class OpenAPISpec:
    title: str
    version: str
    description: Optional[str]
    operations: List[Operation]
    schemas: Dict[str, Schema]


def parse_schema(schema_data: Dict[str, Any], schemas: Dict[str, Schema]) -> Schema:
    if "$ref" in schema_data:
        ref = schema_data["$ref"]
        ref_name = ref.split("/")[-1]
        return Schema(type="object", ref=ref_name)

    schema_type = schema_data.get("type", "object")
    schema_format = schema_data.get("format")
    items = None
    properties = {}
    required = schema_data.get("required", [])
    additional_properties = schema_data.get("additionalProperties")
    enum = schema_data.get("enum", [])
    default = schema_data.get("default")

    if schema_type == "array" and "items" in schema_data:
        items = parse_schema(schema_data["items"], schemas)

    if "properties" in schema_data:
        for prop_name, prop_data in schema_data["properties"].items():
            properties[prop_name] = parse_schema(prop_data, schemas)

    if additional_properties is not None:
        if isinstance(additional_properties, dict):
            additional_properties = parse_schema(additional_properties, schemas)

    return Schema(
        type=schema_type,
        format=schema_format,
        items=items,
        properties=properties,
        required=required,
        additional_properties=additional_properties,
        enum=enum,
        default=default,
    )


def parse_openapi(spec_path: Path) -> OpenAPISpec:
    with open(spec_path, "r") as f:
        spec_data = yaml.safe_load(f)

    info = spec_data.get("info", {})
    title = info.get("title", "")
    version = info.get("version", "")
    description = info.get("description")

    schemas: Dict[str, Schema] = {}
    components = spec_data.get("components", {})
    if "schemas" in components:
        for schema_name, schema_data in components["schemas"].items():
            schemas[schema_name] = parse_schema(schema_data, schemas)

    operations: List[Operation] = []
    paths = spec_data.get("paths", {})

    for path, path_item in paths.items():
        for method in ["get", "post", "put", "patch", "delete"]:
            if method not in path_item:
                continue

            operation_data = path_item[method]
            operation_id = operation_data.get("operationId", f"{method}_{path}")
            op_description = operation_data.get("description")

            parameters: List[Parameter] = []
            if "parameters" in operation_data:
                for param_data in operation_data["parameters"]:
                    param_schema = parse_schema(param_data.get("schema", {}), schemas)
                    parameters.append(
                        Parameter(
                            name=param_data["name"],
                            location=param_data["in"],
                            required=param_data.get("required", False),
                            schema=param_schema,
                            description=param_data.get("description"),
                        )
                    )

            request_body = None
            if "requestBody" in operation_data:
                content = operation_data["requestBody"].get("content", {})
                if "application/json" in content:
                    request_body = parse_schema(content["application/json"]["schema"], schemas)

            responses: List[Response] = []
            if "responses" in operation_data:
                for status_code, response_data in operation_data["responses"].items():
                    response_schema = None
                    if "content" in response_data:
                        content = response_data["content"]
                        if "application/json" in content:
                            response_schema = parse_schema(
                                content["application/json"]["schema"], schemas
                            )

                    responses.append(
                        Response(
                            status_code=status_code,
                            description=response_data.get("description", ""),
                            schema=response_schema,
                        )
                    )

            operations.append(
                Operation(
                    operation_id=operation_id,
                    method=method,
                    path=path,
                    description=op_description,
                    parameters=parameters,
                    request_body=request_body,
                    responses=responses,
                )
            )

    return OpenAPISpec(
        title=title,
        version=version,
        description=description,
        operations=operations,
        schemas=schemas,
    )
