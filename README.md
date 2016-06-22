# The codebase for developer.ubuntu.com

The simplest way to run the site is to have [docker](https://www.docker.com/) and enabled for the current user, and then to run:

``` bash
make run
```

This should serve the site on <localhost:8017>.

*Have patience, this command will take a long time the first time only as it needs to import all the initial data into the database.*

For more in-depth instructions, see [HACKING.md](HACKING.md).

