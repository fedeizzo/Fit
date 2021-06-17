
PROJECT_BASE=$(CURDIR)
export PROJECT_BASE

include defines.mk

all: deps

install:
	$(PYTHON) -m build

uninstall:
	$(PIP) uninstall -y fitfile

dist: install

publish_check: dist
	$(PYTHON) -m twine check dist/*

publish: publish_check
	$(PYTHON) -m twine upload dist/* --verbose

deps:
	$(PIP) install --upgrade --requirement requirements.txt

devdeps:
	$(PIP) install --upgrade --requirement dev-requirements.txt

remove_deps:
	# $(PIP) uninstall -y --requirement requirements.txt
	$(PIP) uninstall -y --requirement dev-requirements.txt

test:
	$(MAKE) -C test

verify_commit: test

flake8:
	$(PYTHON) -m flake8 fit/*.py fit/conversions/*.py fit/exceptions/*.py fit/field_enums/*.py --max-line-length=180 --ignore=E203,E221,E241,W503

test_clean:
	$(MAKE) -C test clean

clean: test_clean
	$(MAKE) -C test clean
	rm -f *.pyc
	rm -rf __pycache__
	rm -rf build
	rm -rf dist
	rm -rf *.egg-info

.PHONY: deps remove_deps test verify_commit clean
