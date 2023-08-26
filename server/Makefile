.PHONY: run
.DEFAULT_GOAL := run

install:
	poetry install

run: install
	cd server && poetry run uvicorn main:app --reload
