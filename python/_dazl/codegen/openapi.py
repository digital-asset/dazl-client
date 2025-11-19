# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from pathlib import Path
from typing import Dict, List

from ..openapi import OpenAPISpec, Operation, Parameter, Schema, parse_openapi
from .python_header import HEADER

__all__ = ["openapi_files"]


def python_type_from_schema(schema: Schema, schemas: Dict[str, Schema]) -> str:
    if schema.ref:
        return schema.ref

    if schema.type == "string":
        return "str"
    elif schema.type == "integer":
        return "int"
    elif schema.type == "number":
        return "float"
    elif schema.type == "boolean":
        return "bool"
    elif schema.type == "array":
        if schema.items:
            item_type = python_type_from_schema(schema.items, schemas)
            return f"List[{item_type}]"
        return "List[Any]"
    elif schema.type == "object":
        if schema.additional_properties:
            if isinstance(schema.additional_properties, bool):
                return "Dict[str, Any]"
            else:
                value_type = python_type_from_schema(schema.additional_properties, schemas)
                return f"Dict[str, {value_type}]"
        return "Dict[str, Any]"
    return "Any"


def generate_schema_class(name: str, schema: Schema, schemas: Dict[str, Schema]) -> str:
    if schema.type != "object" or not schema.properties:
        return ""

    lines = [f"class {name}:"]

    for prop_name, prop_schema in schema.properties.items():
        prop_type = python_type_from_schema(prop_schema, schemas)
        is_required = prop_name in schema.required
        if not is_required:
            prop_type = f"Optional[{prop_type}]"

        lines.append(f"    {prop_name}: {prop_type}")

    if not schema.properties:
        lines.append("    pass")

    lines.append("")
    return "\n".join(lines)


def generate_operation_method(operation: Operation, schemas: Dict[str, Schema]) -> str:
    method_name = operation.operation_id
    params: List[str] = ["self"]

    path_params: List[Parameter] = []
    query_params: List[Parameter] = []
    for param in operation.parameters:
        if param.location == "path":
            path_params.append(param)
        elif param.location == "query":
            query_params.append(param)

        param_type = python_type_from_schema(param.schema, schemas)
        if not param.required:
            param_type = f"Optional[{param_type}]"
            params.append(f"{param.name}: {param_type} = None")
        else:
            params.append(f"{param.name}: {param_type}")

    if operation.request_body:
        body_type = python_type_from_schema(operation.request_body, schemas)
        params.append(f"body: {body_type}")

    params.append("timeout: Optional[float] = None")

    success_response = next((r for r in operation.responses if r.status_code.startswith("2")), None)
    return_type = "Any"
    if success_response and success_response.schema:
        return_type = python_type_from_schema(success_response.schema, schemas)

    lines = [f"    async def {method_name}({', '.join(params)}) -> {return_type}:"]

    if operation.description:
        desc_lines = operation.description.strip().split("\n")
        lines.append('        """')
        for desc_line in desc_lines:
            lines.append(f"        {desc_line}")
        lines.append('        """')

    path = operation.path
    for path_param in path_params:
        path = path.replace(f"{{{path_param.name}}}", f"{{{path_param.name}}}")

    lines.append(f'        url = f"{path}"')

    if query_params:
        lines.append("        params = {}")
        for qp in query_params:
            if qp.required:
                lines.append(f'        params["{qp.name}"] = {qp.name}')
            else:
                lines.append(f"        if {qp.name} is not None:")
                lines.append(f'            params["{qp.name}"] = {qp.name}')
    else:
        lines.append("        params = None")

    if operation.request_body:
        lines.append("        json_data = body")
    else:
        lines.append("        json_data = None")

    lines.append("")
    lines.append(
        f'        return await self._request("{operation.method.upper()}", url, params=params, json=json_data, timeout=timeout)'
    )
    lines.append("")

    return "\n".join(lines)


def generate_client_class(spec: OpenAPISpec) -> str:
    class_name = spec.title.replace(" ", "").replace("-", "")
    if not class_name.endswith("Client"):
        class_name += "Client"

    lines = [
        "class " + class_name + ":",
        '    """',
        f"    {spec.description or spec.title}",
        '    """',
        "",
        "    def __init__(self, base_url: str, auth: Optional[APIAuth] = None):",
        "        self.base_url = base_url.rstrip('/')",
        "        self.auth = auth",
        "        self._session: Optional[aiohttp.ClientSession] = None",
        "",
        "    async def __aenter__(self):",
        "        self._session = aiohttp.ClientSession()",
        "        return self",
        "",
        "    async def __aexit__(self, exc_type, exc_val, exc_tb):",
        "        if self._session:",
        "            await self._session.close()",
        "",
        "    async def _request(",
        "        self,",
        "        method: str,",
        "        path: str,",
        "        params: Optional[Dict[str, Any]] = None,",
        "        json: Optional[Any] = None,",
        "        timeout: Optional[float] = None,",
        "    ) -> Any:",
        "        if not self._session:",
        '            raise RuntimeError("Client must be used as async context manager")',
        "",
        "        url = f'{self.base_url}{path}'",
        "        headers = {}",
        "",
        "        if self.auth:",
        "            headers.update(await self.auth.get_headers())",
        "",
        "        async with self._session.request(",
        "            method, url, params=params, json=json, headers=headers, timeout=timeout",
        "        ) as response:",
        "            response.raise_for_status()",
        "            if response.content_type == 'application/json':",
        "                return await response.json()",
        "            return await response.text()",
        "",
    ]

    for operation in spec.operations:
        lines.append(generate_operation_method(operation, spec.schemas))

    return "\n".join(lines)


def openapi_files(from_: Path, to: Path) -> None:
    import shutil

    if to.exists():
        shutil.rmtree(to)
    to.mkdir(parents=True, exist_ok=True)

    yaml_files = list(from_.glob("**/*.yaml")) + list(from_.glob("**/*.yml"))

    all_schemas: Dict[str, Schema] = {}
    all_clients: List[str] = []

    for yaml_file in yaml_files:
        spec = parse_openapi(yaml_file)

        all_schemas.update(spec.schemas)

        client_module_name = spec.title.lower().replace(" ", "_").replace("-", "_")
        client_file = to / f"{client_module_name}.py"

        imports = [
            "from __future__ import annotations",
            "",
            "from typing import Any, Dict, List, Optional",
            "",
            "import aiohttp",
            "",
            "from ..api.auth import APIAuth",
            "",
        ]

        schema_classes = []
        for schema_name, schema in spec.schemas.items():
            schema_class = generate_schema_class(schema_name, schema, spec.schemas)
            if schema_class:
                schema_classes.append(schema_class)

        client_class = generate_client_class(spec)

        content = HEADER + "\n".join(imports)
        if schema_classes:
            content += "\n".join(schema_classes) + "\n\n"
        content += client_class

        client_file.write_text(content)
        all_clients.append(client_module_name)

    init_file = to / "__init__.py"
    init_imports = [
        "from __future__ import annotations",
        "",
    ]

    for client_module in all_clients:
        class_name = "".join(word.capitalize() for word in client_module.split("_"))
        if not class_name.endswith("Client"):
            class_name += "Client"
        init_imports.append(f"from .{client_module} import {class_name}")

    init_file.write_text(HEADER + "\n".join(init_imports) + "\n")
