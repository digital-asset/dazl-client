# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

cache_dir=.cache

proto_dir := $(cache_dir)/protos
openapi_dir := $(cache_dir)/openapi
splice_version := 0.5.1
splice_tarball := $(cache_dir)/splice-$(splice_version).tar.gz
python := poetry run python3

# Use Nix-provided path if available, otherwise use local cache
SPLICE_OPENAPI_DIR ?= $(openapi_dir)

version := $(strip $(shell cat VERSION))
docs_src := $(shell find docs -name '*.rst') $(py_src)
docs_html_dir := dist/dazl-docs-$(version)-html
docs_html_tgz := $(docs_html_dir).tar.gz
docs_markdown_dir := dist/dazl-docs-$(version)-markdown
docs_markdown_tgz := $(docs_markdown_dir).tar.gz

####################################################################################################
# general targets

# Generate Python bindings from protobuf definitions
# PROTOPACK_DIR is set by nix/shell.nix from the protopack derivation
.PHONY: generate
generate: .venv/poetry.lock
	$(python) -m _dazl update "${PROTOPACK_DIR}/protos.pb"

# Download and extract Ledger API OpenAPI specification from Splice GitHub repository
# This creates a local cache at .cache/openapi/ledger-api/ with the spec
.PHONY: download-openapi
download-openapi: $(openapi_dir)/.downloaded  ## Download Ledger API OpenAPI spec from Splice GitHub repo

$(openapi_dir)/.downloaded: $(splice_tarball)
	@echo "Extracting Ledger API OpenAPI specification from Splice repository..."
	@mkdir -p $(openapi_dir)/ledger-api
	@tar -xzf $(splice_tarball) -C $(cache_dir)
	@# Extract Ledger API spec only
	@if [ -f $(cache_dir)/splice-$(splice_version)/canton/community/ledger/ledger-json-api/src/test/resources/json-api-docs/openapi.yaml ]; then \
		cp $(cache_dir)/splice-$(splice_version)/canton/community/ledger/ledger-json-api/src/test/resources/json-api-docs/openapi.yaml $(openapi_dir)/ledger-api/; \
		echo "✓ Extracted Ledger API spec"; \
	else \
		echo "⚠ Warning: Ledger API OpenAPI spec not found"; \
	fi
	@rm -rf $(cache_dir)/splice-$(splice_version)
	@touch $(openapi_dir)/.downloaded
	@echo "✓ Ledger API OpenAPI specification ready at $(openapi_dir)/ledger-api/"

$(splice_tarball):
	@echo "Downloading Splice repository v$(splice_version) from GitHub..."
	@mkdir -p $(cache_dir)
	@curl -L -o $(splice_tarball) https://github.com/hyperledger-labs/splice/archive/$(splice_version).tar.gz
	@echo "✓ Downloaded Splice repository"

# Generate Ledger API client from OpenAPI specification
# SPLICE_OPENAPI_DIR is set by nix/shell.nix from the splice-openapi derivation,
# or uses local cache at .cache/openapi/ if downloaded via make download-openapi
# Expected structure: ${SPLICE_OPENAPI_DIR}/ledger-api/openapi.yaml
.PHONY: generate-api
generate-api: .venv/poetry.lock download-openapi  ## Generate Python Ledger API client from OpenAPI spec
	@export SPLICE_OPENAPI_DIR=$(SPLICE_OPENAPI_DIR) && $(python) -m _dazl generate-api "$(SPLICE_OPENAPI_DIR)"

####################################################################################################
# Python

py_root := python
py_src_gen_root := python/dazl/_gen
py_src_core := $(shell find python/dazl -path $(py_src_gen_root) -prune -false -o -name '*.py' -o -name '*.pyi')

py_src = $(py_src_core) $(proto_gen_python_src)
py_bdist := dist/dazl-$(version)-py3-none-any.whl
py_sdist := dist/dazl-$(version).tar.gz

####################################################################################################
packages := $(py_bdist) $(py_sdist) $(docs_html_tgz) $(docs_markdown_tgz)

.PHONY: python-deps
python-deps: .venv/poetry.lock

# python: reformat all of our files
.PHONY: python-format
python-format: .venv/poetry.lock
	poetry run isort python $(protos)
	poetry run black python $(protos)

# python: check if files are formatted properly
.PHONY: python-format-test
python-format-test: .venv/poetry.lock
	poetry run isort python $(protos) --check-only
	poetry run black python $(protos) --check

# python: run mypy
.PHONY: python-typecheck
python-typecheck: .venv/poetry.lock
	poetry run python3 -m mypy python $(protos)

# python: build BOTH $(py_bdist) and $(py_sdist)
$(py_sdist) $(py_bdist) &: $(py_src)
	poetry build

# python: witness that makes sure the current venv is up to date with our lock file
.venv/poetry.lock: poetry.lock
	poetry run pip install --no-color --disable-pip-version-check -U pip
	poetry install --no-ansi -E pygments -E tls-testing
	cp $< $@


####################################################################################################
# DAR test fixtures

.PHONY: dars
dars:
	cd _fixtures/src && daml build --all

####################################################################################################



.PHONY: help
help:	## Show list of available make targets
	@cat Makefile | grep -e "^[a-zA-Z_\-]*: *.*## *" | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

.PHONY: clean
clean:  ## Clean everything.
	rm -fr .cache dist target .venv $(shell find python -name '__pycache__' -type d)

.PHONY: clean-openapi
clean-openapi:  ## Clean downloaded OpenAPI specs
	rm -fr $(openapi_dir) $(splice_tarball)


.PHONY: deps
deps: python-deps


.PHONY: build
build: $(packages)  # Build everything.


.PHONY: test
test: python-format-test python-typecheck python-unit-test  ## Run all tests.


.PHONY: local-ci
local-ci:  ## Run the build as if it were running on CI.
	circleci local execute


.PHONY: publish
publish: $(packages)  ## Publish everything.
	scripts/publish.sh $^


.PHONY: format
format: python-format


.PHONY: python-unit-test
python-unit-test: .venv/poetry.lock $(_fixture_dars)
	poetry run pytest --log-cli-level=INFO --junitxml=target/test-results/junit.xml


.PHONY: typecheck
typecheck: python-typecheck


.PHONY: docs
docs: $(docs_html_tgz) $(docs_markdown_tgz)


.PHONY: docs-server
docs-server:
	poetry run sphinx-autobuild -a -b html docs .cache/docs


$(docs_html_tgz): .venv/poetry.lock $(docs_src)
	poetry run sphinx-build -b html docs $(docs_html_dir)
	(cd dist && tar czf $(@F) $(notdir $(docs_html_dir)))


$(docs_markdown_tgz): .venv/poetry.lock $(docs_src)
	poetry run sphinx-build -b markdown docs $(docs_markdown_dir)
	(cd dist && tar czf $(@F) $(notdir $(docs_markdown_dir)))
