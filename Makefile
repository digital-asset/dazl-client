# Copyright (c) 2017-2023 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

cache_dir=.cache

proto_dir := $(cache_dir)/protos
python := poetry run python3
protoc := poetry run python3 -m _dazl_pb.protoc

version := $(strip $(shell cat VERSION))
docs_src := $(shell find docs -name '*.rst') $(py_src)
docs_html_dir := dist/dazl-docs-$(version)-html
docs_html_tgz := $(docs_html_dir).tar.gz
docs_markdown_dir := dist/dazl-docs-$(version)-markdown
docs_markdown_tgz := $(docs_markdown_dir).tar.gz
packages := $(py_bdist) $(py_sdist) $(docs_html_tgz) $(docs_markdown_tgz)

protos := _build/daml-connect/protos.py
proto_filelist = _build/filelists/protobufs.txt
proto_gen_go_src := $(shell cat _build/filelists/go.txt)
proto_gen_python_src := $(shell cat _build/filelists/python.txt)
proto_src := $(shell cat $(proto_filelist))

####################################################################################################
# Protobuf

# proto: the (slightly modified) Protobuf files from Daml Connect
$(proto_src): $(protos)
	@mkdir -p $(@D)
	$(protos) unpack

.cache/protos.pb: $(protos)
	$(protoc) -I.cache/protos -o "$@" --include_imports --include_source_info --retain_options @_build/filelists/protobufs.txt

####################################################################################################
# Go

go_src_gen_root := go/api

# go: run all source generation
.PHONY: go-gen
go-gen: $(go_src_gen)
$(go_src_gen) &: .cache/bin/protoc-gen-go .cache/bin/protoc-gen-go-grpc $(proto_src) COPYRIGHT
	@rm -fr "$(go_src_gen_root)"
	@mkdir -p "$(go_src_gen_root)"
	$(protoc) -I$(proto_dir) --dazl-go_out=$(go_src_gen_root) "@$(proto_filelist)"

.cache/bin/protoc-gen-go:
	GOBIN=$(shell pwd)/.cache/bin go install google.golang.org/protobuf/cmd/protoc-gen-go@v1.27.1

.cache/bin/protoc-gen-go-grpc:
	GOBIN=$(shell pwd)/.cache/bin go install google.golang.org/grpc/cmd/protoc-gen-go-grpc@v1.2.0

####################################################################################################
# Python

py_root := python
py_src_gen_root := python/dazl/_gen
py_src_core := $(shell find python/dazl -path $(py_src_gen_root) -prune -false -o -name '*.py' -o -name '*.pyi')

py_src = $(py_src_core) $(proto_gen_python_src)
py_bdist := dist/dazl-$(version)-py3-none-any.whl
py_sdist := dist/dazl-$(version).tar.gz

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

# python: run all source generation
.PHONY: python-gen
python-gen: $(proto_gen_python_src)

# python: run mypy
.PHONY: python-typecheck
python-typecheck: .venv/poetry.lock
	poetry run python3 -m mypy python $(protos)

# python: build BOTH $(py_bdist) and $(py_sdist)
$(py_sdist) $(py_bdist) &: $(py_src)
	poetry build

# python: Protobuf generated code
$(proto_gen_python_src) &: .venv/poetry.lock $(proto_src)
	@rm -fr "$(@D)"
	@mkdir -p "$(@D)"
	$(protoc) --dazl-python_out="$(py_src_gen_root)" -I$(proto_dir) "@$(proto_filelist)"

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
