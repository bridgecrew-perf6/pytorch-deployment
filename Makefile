.PHONY: venv install

PYTHON=venv/bin/python
PIP=venv/bin/pip
VERSION?=latest
TAG=gcr.io/$(PROJECT_ID)/pytorch-deployment:$(VERSION)

venv:
	@rm -rf venv
	@virtualenv venv
	@$(PIP) install --upgrade pip

install:
	@$(PIP) install -r requirements.txt

run:
	@$(PYTHON) -m uvicorn --factory src.main:create_app

dockerpush:
	@docker build -t $(TAG) .
	@docker push $(TAG)