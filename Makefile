# Copyright (c) 2017-2021 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

cache_dir=.cache
daml_proto_version=1.9.0

download_protos_zip := $(cache_dir)/download/protobufs-$(daml_proto_version).zip
download_status_proto := $(cache_dir)/download/google/rpc/status.proto
proto_dir := $(cache_dir)/protos
proto_manifest := $(proto_dir)/manifest.json
python := poetry run python3

version := $(shell python3 -c "import configparser; config = configparser.ConfigParser(); config.read('pyproject.toml'); print(config['tool.poetry']['version'][1:-1])")
py_src := $(shell find python/dazl -name '*.py[i]') README.md pyproject.toml
docs_src := $(shell find docs -name '*.rst') $(py_src)
py_bdist := dist/dazl-$(version)-py3-none-any.whl
py_sdist := dist/dazl-$(version).tar.gz
docs_html_dir := dist/dazl-docs-$(version)-html
docs_html_tgz := $(docs_html_dir).tar.gz
docs_markdown_dir := dist/dazl-docs-$(version)-markdown
docs_markdown_tgz := $(docs_markdown_dir).tar.gz
packages := $(py_bdist) $(py_sdist) $(docs_html_tgz) $(docs_markdown_tgz)


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


# Go requires that GOBIN be an absolute path
export GOBIN := $(shell pwd)/.cache/bin
export PATH := $(shell go env GOPATH)/bin:${GOBIN}:${PATH}


$(download_protos_zip):
	@mkdir -p $(@D)
	curl -sSL https://github.com/digital-asset/daml/releases/download/v$(daml_proto_version)/protobufs-$(daml_proto_version).zip -o $@


$(download_status_proto):
	@mkdir -p $(@D)
	curl -sSL https://raw.githubusercontent.com/googleapis/googleapis/master/google/rpc/status.proto -o $@


$(proto_manifest): $(download_protos_zip) $(download_status_proto)
	_build/unpack.py \
	  -i $(download_protos_zip) \
	  -i $(download_status_proto) \
	  -o $(@D) -m $@


.PHONY: unpack-protos
unpack-protos: $(cache_dir)/protos/manifest.json


.PHONY: help
help:	## Show list of available make targets
	@cat Makefile | grep -e "^[a-zA-Z_\-]*: *.*## *" | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

.PHONY: clean
clean:  ## Clean everything.
	rm -fr .cache dist target


.PHONY: deps
deps: python-deps


.PHONY: python-deps
python-deps: .venv/poetry.lock


.venv/poetry.lock: poetry.lock
	poetry run pip install pip==21.1.1
	poetry install -E oauth -E prometheus -E pygments -E server
	cp $< $@


# `poetry build` produces both the wheel and a source dist; see
# https://www.gnu.org/software/automake/manual/html_node/Multiple-Outputs.html
# for why these rules are written this way
.PHONY: build
build: $(packages)  # Build everything.


$(py_sdist): $(py_src)
	poetry build


$(py_bdist): $(py_sdist)
	@test -f $@ || rm -f $^
	@test -f $@ || $(MAKE) $(AM_MAKEFLAGS) $^


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


.PHONY: python-format
python-format: .venv/poetry.lock
	poetry run isort python
	poetry run black python


.PHONY: python-format-test
python-format-test: .venv/poetry.lock
	poetry run isort python --check-only
	poetry run black python --check


.PHONY: python-unit-test
python-unit-test: .venv/poetry.lock $(_fixture_dars)
	poetry run pytest --log-cli-level=INFO --junitxml=target/test-results/junit.xml


.PHONY: python-integration-test
python-integration-test: .venv/poetry.lock _fixtures/src/post-office/.daml/dist/post-office-1.0.0.dar
	cd _fixtures/src/post-office && \
	$(python) integration-test.py $(if $(DAZL_TEST_DAML_LEDGER_URL),--url $(DAZL_TEST_DAML_LEDGER_URL))


.PHONY: fetch-protos
fetch-protos: .cache/protos/protobufs-$(daml_proto_version).zip


.PHONY: gen-python
gen-python: .cache/make/python.mk  ## Rebuild Python code-generated files.


.PHONY: gen-go
gen-go: .cache/make/go.mk


.PHONY: gen-go-clean
gen-go-clean:
	echo $(PATH)
	rm -fr .cache/make/go.mk .cache/go-protos go/v7/pkg


.cache/bin/protoc-gen-go:
	mkdir -p $(@D)
	go install google.golang.org/protobuf/cmd/protoc-gen-go

	
.cache/make/go.mk: _build/go/make-fragment $(proto_manifest)
	mkdir -p $(@D)
	$^ > $@


.cache/make/python.mk: _build/python/make-fragment $(proto_manifest)
	mkdir -p $(@D)
	$^ > $@


.PHONY: typecheck
typecheck: python-typecheck


.PHONY: python-typecheck
python-typecheck: .venv/poetry.lock
	poetry run python3 -m mypy -p dazl


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



include .cache/make/go.mk
include .cache/make/python.mk
