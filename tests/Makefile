pattbats := %.bats
batssrc := $(shell find bats/ -type f)
bats := $(filter $(pattbats),$(batssrc))


.PHONY: test
test: $(bats)
	make -C ../python package
	bats -t $<

.PHONY: clean
clean:
	rm -fr venvs
