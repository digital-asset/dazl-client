PYTHON := pipenv run python3

.PHONY: clean
clean:
	rm -fr target

.PHONY: package
package: target/hello-world.zip

target/hello-world/requirements.txt:
	echo https://digitalassetsdk.bintray.com/DigitalAssetSDK/com/digitalasset/dazl/dazl/5.2.12/dazl-5.2.12-py3-none-any.whl > $@

target/hello-world.zip: target/hello-world/hello-world.dar target/hello-world/requirements.txt src/python/hello_world.py
	cp src/python/hello_world.py target/hello-world/
	(cd target && zip -r hello-world.zip hello-world)

.PHONY: package
run: package
	DAML_LEDGER_URL=sandbox:// \
	DAML_LEDGER_PARTY=Alice \
	PIPENV_PIPFILE=../../python/Pipfile \
	$(PYTHON) src/python/hello_world.py

target/hello-world/hello-world.dar: src/daml/Sample.daml
	mkdir -p `dirname $@`
	da run damlc -- package -o $@ $< hello-world
