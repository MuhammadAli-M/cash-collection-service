.PHONY: venv/init build run clean

venv/init:
	virtualenv .venv;

build: venv/init
	source .venv/bin/activate; \
	pip install -r requirements.txt; \
	python -m pip install -e src/

run:
	python src/server/manage.py runserver;

test:
	source .venv/bin/activate; \
	python src/server/manage.py test


migrations:
	python src/server/manage.py makemigrations

migrate:
	python src/server/manage.py migrate

migrate-reset:
	# usage: make migrate-reset name=<app name>
	python src/server/manage.py migrate $(name) zero

lint:
	tunck fmt

clean:
	rm -r .venv

