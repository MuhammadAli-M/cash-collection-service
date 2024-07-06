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

clean:
	rm -r .venv
