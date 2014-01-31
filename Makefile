SHELL := /bin/sh

LOCALPATH := $(CURDIR)
TESTPATH := $(LOCALPATH)/tests

.PHONY: test

test:
	nosetests -v --with-coverage --cover-package=pyca --cover-inclusive --cover-erase tests
