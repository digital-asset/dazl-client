PYTHON := pipenv run python3
bot_version := $(shell python3 src/python/setup.py --version)
dar := target/artifacts/hello-world.dar
bot := target/artifacts/hello-world-$(bot_version).tar.gz

.PHONY: package
package: $(bot) $(dar)


$(dar):
	daml build -o $@


$(bot):
	cd src/python && python3 setup.py sdist
	rm -fr src/python/hello_world.egg-info
	mkdir -p $(@D)
	mv src/python/dist/hello-world-$(bot_version).tar.gz $@


.PHONY: clean
clean:
	rm -fr src/python/hello_world.egg-info src/python/dist target


.PHONY: run-bot
run-bot: $(bot)
	DAML_LEDGER_URL=http://localhost:6865 \
	DAML_LEDGER_PARTY=Operator \
	PIPENV_PIPFILE=src/python/Pipfile \
	PYTHONPATH=src/python \
	$(PYTHON) -um bot
