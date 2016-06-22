##
# Run make targets using the ubuntudesign/devrun image.
# You can see a list of the commands in the image here:
# https://github.com/ubuntudesign/devrun/tree/master/bin
##

# Tell ubuntudesign/devrun where to find docker
# Based on https://github.com/docker/compose/releases/download/1.7.1/run.sh
ifeq ($(DOCKER_HOST),)
	DOCKER_HOST := /var/run/docker.sock
	DOCKER_ADDR := --volume "$(DOCKER_HOST)":"$(DOCKER_HOST)" --env DOCKER_HOST
else
	DOCKER_ADDR := --env DOCKER_HOST --env DOCKER_TLS_VERIFY --env DOCKER_CERT_PATH
endif

# The docker run command for running devrun image
define DEVRUN
docker run \
  ${DOCKER_ADDR} ${COMPOSE_OPTIONS} \
  --tty --interactive \
  --volume "`pwd`":"`pwd`" \
  --workdir "`pwd`" \
  --env-file .env $(patsubst %,--env PORT=%,$(PORT))  \
  ubuntudesign/devrun:v1.0.3
endef

# Error message if docker is missing
define DOCKER_MISSING
Error: Docker not installed
==

Please install Docker before continuing:
https://docs.docker.com/engine/installation/

endef

# Error message if user is not in docker group
define NOT_IN_GROUP
Error: User not in docker group
===

Please add this user to the docker group, e.g. with:
$$ newgrp docker

endef

export GROUP_MESSAGE INSTALL_MESSAGE

.DEFAULT_GOAL := commands

.env:
	@echo "Notice: .env file not found. Initialising with PORT=8000 and DB=false."
	@echo ""
	@echo "PORT=8000" >> .env
	@echo "DB=false" >> .env

check-for-docker:
	@if ! command -v docker >/dev/null 2>&1 || ! grep -q '^docker:' /etc/group; then \
	    echo >&2 "$$DOCKER_MISSING"; \
	    exit 1; \
	fi
	@if ! groups | grep -q '\bdocker\b'; then \
	    echo "$$NOT_IN_GROUP"; \
	    exit 1; \
	fi

%:
	@${MAKE} --quiet .env
	@${MAKE} --quiet check-for-docker
	@${DEVRUN} $@
