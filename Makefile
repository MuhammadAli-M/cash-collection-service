.PHONY: venv/init build clean

venv/init:
	virtualenv .venv;

build: venv/init
	source .venv/bin/activate; \
	pip install -r requirements.txt

clean:
	rm -r .venv
