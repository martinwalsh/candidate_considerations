include .makefiles/ludicrous.mk
include .makefiles/docker-compose.mk

DOCKER_COMPOSE_DAEMON := no

shell: | build
	docker-compose run --rm notebook bash
