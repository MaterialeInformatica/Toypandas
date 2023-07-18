# Makefile by Davide Ponzini

NAME=toypandas
PY=python3



prepare: test documentation
	:

install: uninstall build
	sudo $(PY) -m pip install ./dist/*.whl

build:
	$(PY) -m pip install pipreqs
	pipreqs --force
	sudo $(PY) -m pip install --upgrade -r requirements.txt
	sudo rm -rf dist/
	$(PY) -m pip install build
	$(PY) -m build

uninstall:
	sudo $(PY) -m pip uninstall -y $(NAME)

documentation:
	$(PY) -m pip install --upgrade autoapi
	make html -C docs/

test: install
	$(PY) -m pip install --upgrade pytest
	pytest


### PyPi ###
upload: build documentation
	$(PY) -m pip install --upgrade twine
	$(PY) -m twine upload --verbose dist/*

download: uninstall
	sudo $(PY) -m pip install $(NAME)


### TestPyPi ###
download-test: uninstall
	$(PY) -m pip install --index-url https://test.pypi.org/simple/ --no-deps $(NAME)

upload-test: build
	$(PY) -m pip install --upgrade twine
	$(PY) -m twine upload --repository testpypi dist/*

