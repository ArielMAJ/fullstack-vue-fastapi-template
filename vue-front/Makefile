up-vue:
	yarn serve

install:
	yarn install

patch:
	yarn version --patch
	make untag

minor:
	yarn version --minor
	make untag

untag:
	git tag -d $(shell git describe --tags --abbrev=0)
