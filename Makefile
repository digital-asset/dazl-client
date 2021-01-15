# Copyright (c) 2017-2021 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

cache_dir=.cache
daml_proto_version=1.3.0

download_protos_zip := $(cache_dir)/download/protobufs-$(daml_proto_version).zip
download_status_proto := $(cache_dir)/download/google/rpc/status.proto
proto_dir := $(cache_dir)/protos
proto_manifest := $(proto_dir)/manifest.json
python := $(shell cd python && poetry env info -p)/bin/python3

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
	  -i $(download_protos_zip):protos-$(daml_proto_version) \
	  -i $(download_status_proto):$(cache_dir)/download \
	  -o $(@D) -m $@


.PHONY: unpack-protos
unpack-protos: $(cache_dir)/protos/manifest.json


.PHONY: help
help:	## Show list of available make targets
	@cat Makefile | grep -e "^[a-zA-Z_\-]*: *.*## *" | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

.PHONY: deps
deps:  ## Fetch all dependencies.
	make -C python deps

.PHONY: clean
clean:  ## Clean everything.
	rm -fr .cache
	make -C python clean
	make -C tests clean

.PHONY: build
build:  ## Build everything.
	make -C python build

.PHONY: test
test: dars  ## Run all tests.
	make -C python test
	make -C tests test

.PHONY: local-ci
local-ci:  ## Run the build as if it were running on CI.
	circleci local execute

.PHONY: publish
publish:  ## Publish everything.
	make -C python publish


.PHONY: python-test
python-test: dars
	$(MAKE) -C python test


.PHONY: python-integration-test
python-integration-test:
	$(MAKE) -C python integration-test


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


.cache/make/dars.mk: _build/dar/make-fragment
	mkdir -p $(@D)
	$^ > $@
	

.cache/bin/protoc-gen-go:
	mkdir -p $(@D)
	go install google.golang.org/protobuf/cmd/protoc-gen-go

	
.cache/make/go.mk: _build/go/make-fragment $(proto_manifest)
	mkdir -p $(@D)
	$^ > $@


.cache/make/python.mk: _build/python/make-fragment $(proto_manifest)
	mkdir -p $(@D)
	$^ > $@


include .cache/make/dars.mk
include .cache/make/go.mk
include .cache/make/python.mk
