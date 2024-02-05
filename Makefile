ifneq ("$(wildcard .env)","")
	include .env
	export
endif

API_DIR = api
VUE_FRONT_DIR = vue-front

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
	cp ./vue-front/.env.example ./vue-front/.env
	cp ./api/.env.example ./api/.env
