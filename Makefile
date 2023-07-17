NAME=toypandas
PY=python3


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

### Documentation ###
documentation:
	$(PY) -m pip install autoapi
	make html -C docs/


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

