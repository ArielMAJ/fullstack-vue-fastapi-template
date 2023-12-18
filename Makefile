ifneq ("$(wildcard .env)","")
	include .env
	export
endif

API_DIR = api
VUE_FRONT_DIR = vue-front

MAKE_API = $(MAKE) -C $(API_DIR)
MAKE_VUE_FRONT = $(MAKE) -C $(VUE_FRONT_DIR)

up-api:
	$(MAKE_API) up-api

up-vue:
	$(MAKE_VUE_FRONT) up-vue

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
