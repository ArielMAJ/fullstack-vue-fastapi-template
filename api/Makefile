ifneq ("$(wildcard .env)","")
	include .env
	export
endif


run:
	poetry run python -m src.main

install:
	pip install poetry
	poetry install --no-root
	poetry lock
	poetry run pre-commit install

pre-commit:
	poetry run pre-commit run --config ./.pre-commit-config.yaml

patch:
	poetry version patch

minor:
	poetry version minor
