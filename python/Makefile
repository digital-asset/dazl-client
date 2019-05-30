# Copyright (c) 2019 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

LIBRARY_NAME=dazl
SANDBOX_PORT=7600
VERSION=$(shell python3 setup.py --version)


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
deps:
	poetry install -E prometheus -E pygments

.PHONY: package
package:
	poetry build

.PHONY: package-docs
package-docs:
	pipenv run docs
	(cd dist && tar czf dazl-docs-$(VERSION).tar.gz documentation)


####################################################################################################
## TEST TARGETS                                                                                   ##
####################################################################################################

.PHONY: mypy
mypy:
	poetry run python3 -m mypy -p dazl

.PHONY: test
test: deps unit-test integration-test

.PHONY: unit-test
unit-test:
	poetry run pytest --log-cli-level=INFO --junitxml=test-results/junit.xml

.PHONY: integration-test
integration-test:
	poetry run python3 _template/integration-test.py


####################################################################################################
## TEST TARGETS                                                                                   ##
####################################################################################################

.PHONY: docs
docs:
	poetry run python3 scripts/docs.py build

.PHONY: docs-server
docs-server:
	poetry run python3 scripts/docs.py server
