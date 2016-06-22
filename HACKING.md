# Hacking on developer.ubuntu.com

More in-depth instructions than [README.md](README.md) on running this site in
more custom ways and in other environments.

## The Makefile

The Makefile provides a standard mechanism for spinning up docker containers
to run the site.

### Basic make commands

`make run`: Run the application at <localhost:8776>
`PORT=8111 make run`: Run the application at <localhost:8111>
`PORT=8111 make db-client`: Connect a psql client to the database container
`make commands`: List further commands
`make sh`: Connect to the [`ubuntudesign/devrun-db`][devrun-db] container itself

### Understanding devrun-db

The Makefile passes all commands through to the
[`ubuntudesign/devrun-db` docker image][devrun-db].

This image is based off the [docker/compose image][compose-image].
It contains a basic [Dockerfile][devrun-dockerfile] for building the application image
with all the dependencies specified in [requirements/dev.txt](requirements/dev.txt)
and a [docker-compose config][devrun-compose] which defines the application
database containers necessary for running a standard database-backed website
project.

All `make` targets will be run against this image. Therefore you can connect
to the `devrun-db` container with `make sh`, and you can run more complex
commands against the image using quotes,
e.g.: `make "docker-compose run web bash"`.

## Hand-rolling dependencies

You may not want to use the standard `Makefile` setup. Maybe you can't or don't
want to run Docker locally, or you are trying to setup a production environment
to run this website project, or you simply want to have more understanding &
control over the guts of how this application is run.

In this case you'll need to understand the project dependencies in more depth.

### System dependencies

For installing the python dependencies, you'll need [python 2][python 2] and
[pip][]. The `psycopg2` python module will also require the PostgreSQL C client
library.

To install these in Ubuntu, run:

``` bash
sudo apt install python-dev python-pip libpq-dev
```

### Python dependencies

Assuming you have the above system dependencies installed, you should be able
to install all the python dependencies with:

``` bash
pip install -r requirements/dev.txt  # To include modules helpful for local debugging
# or
pip install -r requirements/standard.txt  # If you just need the basics for running the app
```

#### Python environment management

If you're trying to run `pip install` directly on your local system, you'll
probably hit a permissions error. You *could* append `sudo` to the above
commands to install these modules directly into your sytem Python.

However, it is usually preferable to use a [virtualenv][] instead, e.g.:

``` bash
sudo pip install virtualenv  # Install virtualenv in your system
virtualenv ./env    # Setup a local virtualenv in a folder called "env"
. ./env/bin/activate  # Use the new virtualenv
```

And then run the `pip install` commands to install these dependencies into
this `./env` virtual environment folder.

When you're done with using this Python environment you can deactivate it with
`deactivate`, and when you want to use it again, re-run `. ./env/bin/activate`.

### Database

The application is intended to work with a PostgreSQL database, although
you could cnofigure it to work with any database.

The database for the application is defined by setting
[a database URL][database-url]. For PostgreSQL, this URL will take the form
`postgres://USER:PASSWORD@HOST:PORT/NAME`. The default database URL is
`postgres://postgres:dev@db:5432/postgres`.

You can override this URL by setting the `DATABASE_URL` environment variable,
e.g.:

``` bash
export DATABASE_URL='postgres://me:my-password@localhost:5432/my-database'
```

#### Other databases

To use a different type of database, you can simply change the schema of
the `DATABASE_URL`, e.g.:

``` bash
export DATABASE_URL='sqlite:///`pwd`/sqlite.db'
```

[database-url]: https://github.com/kennethreitz/dj-database-url#url-schema
