PYTHON ?= poetry run python3

.PHONY: all
all:
	mkdir -p target
	$(PYTHON) -m daml_lf_decoder_gen py-model > target/daml_lf_1.py
	$(PYTHON) -m daml_lf_decoder_gen py-typing > target/daml_lf_1.pyi
	$(PYTHON) -m daml_lf_decoder_gen go > target/daml_lf_1.go
