# Copyright (c) 2017-2021 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

SHELL := /usr/bin/env bash
.SHELLFLAGS := -euo pipefail -c

LIBRARY_NAME=dazl
version := $(shell python3 -c "import configparser; config = configparser.ConfigParser(); config.read('pyproject.toml'); print(config['tool.poetry']['version'][1:-1])")
ghr_new_flags := $(shell python3 -c "from pkg_resources import parse_version; print('-prerelease' if parse_version('$(version)').is_prerelease else '')")

dazl_files := $(shell find dazl -name '*.py') README.md
dazl_docs_files := $(shell find docs -name '*.rst') $(dazl_files)
dazl_bdist := dist/dazl-$(version)-py3-none-any.whl
dazl_sdist := dist/dazl-$(version).tar.gz
dazl_docs_html := dist/dazl-docs-$(version)-html.tar.gz
dazl_docs_markdown := dist/dazl-docs-$(version)-markdown.tar.gz

build_dir := build/.dir
poetry_build_marker := build/.poetry.build
poetry_install_marker := build/.poetry.install
dazl_docs_html_dir := $(basename $(basename $(dazl_docs_html)))
dazl_docs_markdown_dir := $(basename $(basename $(dazl_docs_markdown)))

python := $(shell pwd)/.venv/bin/python3 

export PYTHONPATH:=.:${PYTHONPATH}



####################################################################################################
## GENERAL TARGETS                                                                                ##
####################################################################################################

.PHONY: all
all: clean test

.PHONY: clean
clean:
	find . -name *.pyc -print0 | xargs -0 rm
	find . -name __pycache__ -print0 | xargs -0 rm -fr
	rm -fr build dist $(LIBRARY_NAME).egg-info test-reports

.PHONY: deps
deps: $(poetry_install_marker)

.PHONY: format
format: $(poetry_install_marker)
	poetry run isort .
	poetry run black .

.PHONY: format-check
format-check: $(poetry_install_marker)
	poetry run isort . --check-only
	poetry run black . --check

.PHONY: build
build: package

.PHONY: package
package: $(dazl_bdist) $(dazl_sdist) $(dazl_docs_html) $(dazl_docs_markdown)

.PHONY: publish 
publish: package
	./scripts/publish.sh "$(dazl_bdist)" "$(dazl_sdist)" "$(dazl_docs_html)" "$(dazl_docs_markdown)"

.PHONY: version
version:
	@echo $(version)


####################################################################################################
## TEST TARGETS                                                                                   ##
####################################################################################################

.PHONY: typecheck
typecheck:
	poetry run python3 -m mypy -p dazl

.PHONY: test
test: deps unit-test integration-test

.PHONY: unit-test
unit-test:
	poetry run pytest --log-cli-level=INFO --junitxml=test-results/junit.xml

# Run tests specifically testing our documentation around using Python's unittest framework.
# This is NOT hooked into CircleCI because it requires a Docker container with both Java and Python.
.PHONY: unittest-test
unittest-test:
	poetry run python3 -m unittest tests/unittest_example/unittest_example.py

.PHONY: integration-test
integration-test:
	cd ../_fixtures/src/post-office && \
	$(python) integration-test.py $(if $(DAZL_TEST_DAML_LEDGER_URL),--url $(DAZL_TEST_DAML_LEDGER_URL))


####################################################################################################
## DOCUMENTATION TARGETS                                                                          ##
####################################################################################################

.PHONY: docs
docs: $(dazl_docs_html) $(dazl_docs_markdown)

.PHONY: docs-server
docs-server:
	poetry run python3 scripts/docs.py server


####################################################################################################
## file targets                                                                                   ##
####################################################################################################

$(build_dir):
	@mkdir -p build
	@touch $@

$(poetry_build_marker): $(build_dir) pyproject.toml $(dazl_files)
	poetry build
	touch $@

$(poetry_install_marker): $(build_dir) poetry.lock
	poetry run pip install -U pip
	poetry install -E oauth -E prometheus -E pygments -E server
	touch $@

$(dazl_bdist): $(poetry_build_marker)

$(dazl_sdist): $(poetry_build_marker)

$(dazl_docs_html): $(poetry_install_marker) $(dazl_docs_files)
	poetry run python3 scripts/docs.py build --format html -o $(dazl_docs_html_dir)
	(cd dist && tar czf $(@F) $(notdir $(dazl_docs_html_dir)))

$(dazl_docs_markdown): $(poetry_install_marker) $(dazl_docs_files)
	poetry run python3 scripts/docs.py build --format markdown -o $(dazl_docs_markdown_dir)
	(cd dist && tar czf $(@F) $(notdir $(dazl_docs_markdown_dir)))

.PHONY: poetry-build
poetry-build: $(poetry_build_marker)
