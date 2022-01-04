.PHONY: clean

install: venv
	: # Activate venv and install dependencies
	@. venv/bin/activate && pip install -r requirements.txt
	@(echo "make sure to activate venv in your shell")
venv:
	: # Create venv if it doesn't exist
	@test -d venv || python3 -m venv --prompt extended_knapsack venv
test:
	@pytest -vv
lint:
	@pycodestyle src
clean:
	@rm -rf dist
build: clean
	@python3 -m build
publish: build
	@python3 -m twine upload dist/*
