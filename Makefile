.PHONY: clean

VERSION ?= $(shell pipenv run python -c "from setuptools_scm import get_version;print(get_version())")

test:
	pipenv run py.test tests

clean:
	rm -rf api

docker_image: $(wildcard generator/**/*) $(wildcard generator/*)
	docker build -t custom-codegen generator

clean_api:
	rm -rf api

api: openapi.yaml Makefile $(wildcard templates/**/*) $(wildcard templates/*) docker_image
	docker run --rm --user `id -u`:`id -g` -v ${PWD}:/local custom-codegen \
	           generate -i /local/openapi.yaml \
	           --git-user-id rienafairefr \
	           --git-repo-id pytruelayer \
	           -t /local/templates \
	           -g eu.rienafairefr.customcodegen.PythonCustomCodegen -o /local/api \
	           -p projectName=pytruelayer \
	           -p packageName=truelayer \
	           -p packageVersion="$(VERSION)" \
	           -p appName="pytruelayer" \
	           -p infoEmail="rienafairefr@gmail.com"
	docker run --rm --user `id -u`:`id -g` -v ${PWD}:/local custom-codegen \
	           generate -i /local/auth_openapi.yaml \
	           -t /local/templates \
	           -g eu.rienafairefr.customcodegen.PythonCustomCodegen -o /local/api \
	           -p packageName=truelayer.auth \
	           -p generateSourceCodeOnly="true"
