##
# Run make targets using the ubuntudesign/devrun image.
# You can see a list of the commands in the image here:
# https://github.com/ubuntudesign/devrun/tree/master/bin
##

# The docker run command for running devrun image
define DEVRUN
docker run ${COMPOSE_OPTIONS} \
  --volume /var/run/docker.sock:/var/run/docker.sock \
  --tty --interactive \
  --volume "`pwd`":"`pwd`" \
  --workdir "`pwd`" \
  --env-file .env $(patsubst %,--env PORT=%,$(PORT)) $(patsubst %,--env INITIAL_FIXTURE_URL=%,$(INITIAL_FIXTURE_URL)) \
  devrun
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
	@${MAKE} --quiet check-for-docker
	@${DEVRUN} $@
