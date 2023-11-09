# Copyright (c) 2017-2023 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

cache_dir=.cache

proto_dir := $(cache_dir)/protos
python := poetry run python3
protoc := poetry run python3 -m _dazl_pb.protoc

version := $(shell python3 -c "import configparser; config = configparser.ConfigParser(); config.read('pyproject.toml'); print(config['tool.poetry']['version'][1:-1])")
docs_src := $(shell find docs -name '*.rst') $(py_src)
docs_html_dir := dist/dazl-docs-$(version)-html
docs_html_tgz := $(docs_html_dir).tar.gz
docs_markdown_dir := dist/dazl-docs-$(version)-markdown
docs_markdown_tgz := $(docs_markdown_dir).tar.gz
packages := $(py_bdist) $(py_sdist) $(docs_html_tgz) $(docs_markdown_tgz)

protos := _build/daml-connect/protos.py

####################################################################################################
# Protobuf

proto_rel_dir     := $(shell $(protos) list --kind dir)
proto_rel_pb_only := $(shell $(protos) list --kind pb)
proto_rel_grpc    := $(shell $(protos) list --kind grpc)
proto_rel_pb      := $(proto_rel_pb_only) $(proto_rel_grpc)

proto_src_pb      := $(foreach p,$(proto_rel_pb),.cache/protos/$(p))
proto_src_grpc    := $(foreach p,$(proto_rel_grpc),.cache/protos/$(p))

# proto: the (slightly modified) Protobuf files from Daml Connect
$(proto_src_pb): .cache/witnesses/proto
.cache/witnesses/proto: $(protos)
	@mkdir -p $(@D)
	$(protos) unpack
	@touch $@

####################################################################################################
# Go

go_src_gen_root := go/api
go_src_gen_pb := $(foreach d,$(proto_rel_pb),$(go_src_gen_root)/$(d:.proto=.pb.go))
go_src_gen_grpc := $(foreach d,$(proto_rel_grpc),$(go_src_gen_root)/$(d:.proto=_grpc.pb.go))
go_src_gen := $(go_src_gen_pb) $(go_src_gen_grpc)

go_tmp_gen_root := .cache/go-gen

# go: run all source generation
.PHONY: go-gen
go-gen: $(go_src_gen)

# go: Protobuf generated code (non-gRPC)
$(go_src_gen_pb): $(go_src_gen_root)/%: $(go_tmp_gen_root)/% COPYRIGHT
	@mkdir -p $(@D)
	cp $< $@

$(foreach d,$(proto_rel_pb),$(go_tmp_gen_root)/$(d:.proto=.pb.go)): .cache/witnesses/go-pb
.cache/witnesses/go-pb: .cache/bin/protoc-gen-go $(proto_src_pb)
	@mkdir -p $(go_tmp_gen_root)
	PATH=.cache/bin:"${PATH}" $(protoc) -I$(proto_dir) --go_out=$(go_tmp_gen_root) --go_opt=paths=source_relative $(proto_src_pb)

# go: Protobuf generated code (gRPC)
#  NOTE: Go's gRPC-generated code does NOT include a copyright, so we need to add that ourselves
$(go_src_gen_grpc): $(go_src_gen_root)/%: $(go_tmp_gen_root)/% COPYRIGHT
	@mkdir -p $(@D)
	{ sed 's/^/\/\/ /' COPYRIGHT ; cat $< ; } > $@

$(foreach d,$(proto_rel_grpc),$(go_tmp_gen_root)/$(d:.proto=_grpc.pb.go)): .cache/witnesses/go-grpc
.cache/witnesses/go-grpc: .cache/bin/protoc-gen-go .cache/bin/protoc-gen-go-grpc $(proto_src_grpc) .cache/witnesses/proto
	@mkdir -p $(go_tmp_gen_root)
	PATH=.cache/bin:"${PATH}" $(protoc) -I$(proto_dir) --go_out=$(go_tmp_gen_root) --go_opt=paths=source_relative --go-grpc_out=$(go_tmp_gen_root) --go-grpc_opt=paths=source_relative $(proto_src_grpc)

.cache/bin/protoc-gen-go:
	GOBIN=$(shell pwd)/.cache/bin go install google.golang.org/protobuf/cmd/protoc-gen-go@v1.27.1

.cache/bin/protoc-gen-go-grpc:
	GOBIN=$(shell pwd)/.cache/bin go install google.golang.org/grpc/cmd/protoc-gen-go-grpc@v1.2.0

####################################################################################################
# Python

py_root := python
py_src_gen_root := python/dazl/_gen
py_src_core := $(shell find python/dazl -path $(py_src_gen_root) -prune -false -o -name '*.py' -o -name '*.pyi')

py_src_gen_mod_init := $(py_src_gen_root)/__init__.py \
                       $(foreach d,$(proto_rel_dir),$(py_src_gen_root)/$(d)/__init__.py)
py_src_gen_pb := $(foreach d,$(proto_rel_pb),$(py_src_gen_root)/$(d:.proto=_pb2.py))
py_src_gen_pb_pyi := $(foreach d,$(proto_rel_pb),$(py_src_gen_root)/$(d:.proto=_pb2.pyi))
py_src_gen_grpc := $(foreach d,$(proto_rel_grpc),$(py_src_gen_root)/$(d:.proto=_pb2_grpc.py))
py_src_gen_grpc_pyi := $(foreach d,$(proto_rel_grpc),$(py_src_gen_root)/$(d:.proto=_pb2_grpc.pyi))
py_src_gen := $(py_src_gen_mod_init) $(py_src_gen_pb) $(py_src_gen_pb_pyi) $(py_src_gen_grpc) $(py_src_gen_grpc_pyi)

py_src = $(py_src_core) $(py_src_gen)
py_bdist := dist/dazl-$(version)-py3-none-any.whl
py_sdist := dist/dazl-$(version).tar.gz

py_tmp_gen_root := .cache/python-gen

.PHONY: python-deps
python-deps: .venv/poetry.lock

# python: reformat all of our files
.PHONY: python-format
python-format: .venv/poetry.lock
	poetry run isort python
	poetry run black python

# python: check if files are formatted properly
.PHONY: python-format-test
python-format-test: .venv/poetry.lock
	poetry run isort python --check-only
	poetry run black python --check

# python: run all source generation
.PHONY: python-gen
python-gen: $(py_src_gen)

# python: run mypy
.PHONY: python-typecheck
python-typecheck: .venv/poetry.lock
	poetry run python3 -m mypy python

# python: build BOTH $(py_bdist) and $(py_sdist)
$(py_sdist) $(py_bdist) &: $(py_src)
	poetry build

# python: Protobuf generated code (non-gRPC)
$(py_src_gen): $(py_src_gen_root)/%: .cache/witnesses/python
.cache/witnesses/python: .venv/poetry.lock .cache/witnesses/proto
	@mkdir -p $(@D)
	$(protoc) --dazl-python_out="$(py_src_gen_root)" -I$(proto_dir) $(proto_src_pb)

# python: witness that makes sure the current venv is up to date with our lock file
.venv/poetry.lock: poetry.lock
	poetry run pip install --no-color --disable-pip-version-check -U pip
	poetry install --no-ansi -E oauth -E prometheus -E pygments -E server -E tls-testing
	cp $< $@


####################################################################################################
# DAR test fixtures

_fixture_dars := $(shell scripts/make/dars -o)

.cache/make/dars.mk: scripts/make/dars $(shell scripts/make/dars -d)
	@mkdir -p $(@D)
	@$< -M > $@

.PHONY: dars
dars: $(_fixture_dars)

include .cache/make/dars.mk

####################################################################################################



.PHONY: help
help:	## Show list of available make targets
	@cat Makefile | grep -e "^[a-zA-Z_\-]*: *.*## *" | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

.PHONY: clean
clean:  ## Clean everything.
	rm -fr .cache dist target .venv $(shell find python -name '__pycache__' -type d)


.PHONY: deps
deps: python-deps


.PHONY: build
build: $(packages)  # Build everything.


.PHONY: test
test: python-format-test python-typecheck python-unit-test python-integration-test  ## Run all tests.


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


.PHONY: python-integration-test
python-integration-test: .venv/poetry.lock _fixtures/src/post-office/.daml/dist/post-office-1.0.0.dar
	cd _fixtures/src/post-office && \
	$(python) integration-test.py $(if $(DAZL_TEST_DAML_LEDGER_URL),--url $(DAZL_TEST_DAML_LEDGER_URL))


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


