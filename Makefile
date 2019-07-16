.PHONY: help
help:	## Show list of available make targets
	@cat Makefile | grep -e "^[a-zA-Z_\-]*: *.*## *" | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

.PHONY: deps
deps:  ## Fetch all dependencies.
	make -C python deps

.PHONY:
clean:  ## Clean everything.
	make -C python clean
	make -C tests clean

.PHONY:
build:  ## Build everything.
	make -C python build

.PHONY:
test:  ## Run all tests.
	make -C python test
	make -C tests test

.PHONY:
local-ci:  ## Run the build as if it were running on CI.
	circleci local execute

.PHONY:
publish:  ## Publish everything.
	make -C python publish
