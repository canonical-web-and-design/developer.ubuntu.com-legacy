# [developer.ubuntu.com](http://developer.ubuntu.com)

*Not yet live: This version is to replace what's currently on developer.ubuntu.com when it's ready.*

The simplest way to run the site is to have [docker](https://www.docker.com/) installed and enabled for the current user, and then to run:

``` bash
make run
```

This should serve the site on `http://localhost:8017` (or `http://${DOCKER_HOST}:8017` on Mac).

*Have patience, this command will take a long time the first time only as it needs to import all the initial data into the database.*

For more in-depth instructions, see [HACKING.md](HACKING.md).
