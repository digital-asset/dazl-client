#!/usr/bin/env bash

set -euo pipefail

daml start  --start-navigator=no &
sandbox_pid=$!
trap "kill ${sandbox_pid}" SIGINT SIGTERM EXIT

DAML_LEDGER_URL=http://localhost:6865/ DAZL_SERVER_PORT=53390 .venv/bin/python3 app.py
kill ${sandbox_pid}
