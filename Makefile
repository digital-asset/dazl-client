cache_dir=.cache
daml_proto_version=0.13.56-snapshot.20200408.3877.0.1ddcd3c0

download_protos_zip := $(cache_dir)/download/protobufs-$(daml_proto_version).zip
download_status_proto := $(cache_dir)/download/google/rpc/status.proto
proto_dir := $(cache_dir)/protos
proto_manifest := $(proto_dir)/manifest.json
python := $(shell cd python && poetry env info -p)/bin/python3


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
test:  ## Run all tests.
	make -C python test
	make -C tests test

.PHONY: local-ci
local-ci:  ## Run the build as if it were running on CI.
	circleci local execute

.PHONY: publish
publish:  ## Publish everything.
	make -C python publish


.PHONY: gen-python
gen-python: .cache/make/python.mk  ## Rebuild Python code-generated files.


.PHONY: fetch-protos
fetch-protos: .cache/protos/protobufs-$(daml_proto_version).zip


.cache/make/python.mk: _build/make-template.py $(proto_manifest)
	mkdir -p $(@D)
	$^ > $@


include .cache/make/python.mk
