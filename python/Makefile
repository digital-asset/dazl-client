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
	pipenv sync --dev

.PHONY: package
package: deps package-wheel package-docs

.PHONY: package-wheel
package-wheel:
	pipenv run pip3 wheel . --no-deps -w dist

.PHONY: package-docs
package-docs:
	pipenv run docs
	(cd dist && tar czf dazl-docs-$(VERSION).tar.gz documentation)


####################################################################################################
## TEST TARGETS                                                                                   ##
####################################################################################################

.PHONY: test
test: deps unit-test integration-test

.PHONY: unit-test
unit-test:
	export PYTHONPATH=. && pipenv run test

.PHONY: integration-test
integration-test:
	pipenv run python3 _template/integration-test.py
