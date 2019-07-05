pip := .venv/bin/pip
python := .venv/bin/python3
pip-compile := .venv/bin/pip-compile
pip-sync := .venv/bin/pip-sync
version := $(shell python3 setup.py --version)


.PHONY: wheel
wheel: dist/dazl_pb-$(version)-py3-none-any.whl

.PHONY: python
python: $(python) requirements-sync

.PHONY: requirements-sync
requirements-sync: $(python) $(pip-sync)
	$(pip-sync) requirements.txt requirements-dev.txt

$(python):
	python3 -m venv .venv

$(pip): $(python)

$(pip-compile): $(pip)
	$(pip) install -r requirements-dev.txt

$(pip-sync): $(pip)
	$(pip) install -r requirements-dev.txt

requirements.txt: $(pip-compile) setup.py
	CUSTOM_COMPILE_COMMAND="make $@" $(pip-compile) --generate-hashes

requirements-dev.txt: $(pip-compile) requirements-dev.in
	CUSTOM_COMPILE_COMMAND="make $@" $(pip-compile) requirements-dev.in --generate-hashes

dist/dazl_pb-$(version)-py3-none-any.whl: $(pip)
	$(pip) wheel . --no-deps -w dist
