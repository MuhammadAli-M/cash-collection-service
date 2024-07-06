.PHONY: venv/init build run clean

venv/init:
	virtualenv .venv;

build: venv/init
	source .venv/bin/activate; \
	pip install -r requirements.txt

run:
	python src/server/manage.py runserver;

clean:
	rm -r .venv

