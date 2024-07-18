# Copyright (c) 2017-2024 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

cache_dir=.cache

proto_dir := $(cache_dir)/protos
python := poetry run python3

version := $(strip $(shell cat VERSION))
docs_src := $(shell find docs -name '*.rst') $(py_src)
docs_html_dir := dist/dazl-docs-$(version)-html
docs_html_tgz := $(docs_html_dir).tar.gz
docs_markdown_dir := dist/dazl-docs-$(version)-markdown
docs_markdown_tgz := $(docs_markdown_dir).tar.gz
packages := $(py_bdist) $(py_sdist) $(docs_html_tgz) $(docs_markdown_tgz)

####################################################################################################
# general targets

.PHONY: generate
generate: .venv/poetry.lock .cache/bin/protoc-gen-go .cache/bin/protoc-gen-go-grpc
	$(python) -m _dazl update 2.9.1

####################################################################################################
# Go

.cache/bin/protoc-gen-go:
	GOBIN=$(shell pwd)/.cache/bin go install google.golang.org/protobuf/cmd/protoc-gen-go@v1.28

.cache/bin/protoc-gen-go-grpc:
	GOBIN=$(shell pwd)/.cache/bin go install google.golang.org/grpc/cmd/protoc-gen-go-grpc@v1.2

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

# python: run mypy
.PHONY: python-typecheck
python-typecheck: .venv/poetry.lock
	poetry run python3 -m mypy python $(protos) --exclude='.*_py3_10\.py$$'

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
