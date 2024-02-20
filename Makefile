ifneq ("$(wildcard .env)","")
	include .env
	export
endif

API_DIR = backend
VUE_FRONT_DIR = frontend

MAKE_API = $(MAKE) -C $(API_DIR)
MAKE_VUE_FRONT = $(MAKE) -C $(VUE_FRONT_DIR)

run-api:
	$(MAKE_API) run

run-vue:
	$(MAKE_VUE_FRONT) run

install:
	$(MAKE_API) install
	$(MAKE_VUE_FRONT) install

pre-commit:
	$(MAKE_API) pre-commit

patch: pre-commit
	$(MAKE_API) patch
	$(MAKE_VUE_FRONT) patch

minor: pre-commit
	$(MAKE_API) minor
	$(MAKE_VUE_FRONT) minor

default-dot-envs:
	cp ./$(VUE_FRONT_DIR)/.env.example ./$(VUE_FRONT_DIR)/.env.local
	cp ./$(API_DIR)/.env.example ./$(API_DIR)/.env
