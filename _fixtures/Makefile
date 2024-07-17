.PHONY: all
all: target/versions.txt
	$(foreach version,$(shell cat $^),$(MAKE) archives/$(version)/Test.dar ; )


target/versions.txt:
	mkdir -p target
	./scripts/list.py > $@


archives/%/Test.dar: target/%/build.sh
	$<


target/%/build.sh:
	./scripts/generate.py $(*F)
