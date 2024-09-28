install:
	python3 -m venv venv
	venv/bin/pip3 install --upgrade pip &&\
	venv/bin/pip3 install -r requirements.txt

format:	
	venv/bin/black src/*.py

test:
	venv/bin/python3 -m pytest -vv --cov=src.dotp

lint:
	venv/bin/ruff check src/*.py

all: install lint test format