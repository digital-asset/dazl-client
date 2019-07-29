daml_files := $(shell find . -name '*.daml' -type f)


.PHONY: run
run: .venv/bin/python3 .daml/dist/pingpong.dar
	./run.sh


.daml/dist/pingpong.dar: $(daml_files)
	daml build


.venv/bin/python3:
	python3 -m venv .venv
	.venv/bin/pip install -e ../../python
