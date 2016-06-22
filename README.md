# [developer.ubuntu.com](http://developer.ubuntu.com)

*Not yet live: This fork of [lp:developer-ubuntu-com](https://launchpad.net/developer-ubuntu-com) is intended to become the new official codebase behind http://developer.ubuntu.com when it's ready.*

## Initial content

By default, the database won't be provisioned with any website content, so what you will see will look very similar to a vanilla [Django CMS](https://www.django-cms.org/) installation.

You can provide an initial site content [database fixture](https://docs.djangoproject.com/en/1.9/howto/initial-data/#providing-initial-data-with-fixtures) at `developer_portal/fixtures/initial_content.json`, in which case the first time [`migrate`](https://docs.djangoproject.com/en/1.9/ref/django-admin/#migrate) is run it will import this initial content into the database.

You can instead provide a URL to retrieve this fixture from by setting the `INITIAL_FIXTURE_URL` environment variable, e.g.:

``` bash
export INITIAL_CONTENT_FIXTURE=https://example.com/fixtures/initial-content.json
```

in which case the initial run of `migrate` will download this file to `developer_portal/fixtures/initial_content.json` (if it doesn't already exist) before importing the fixture.

### Official database snapshot

If you have access to the private [developer-data repository](https://github.com/ubuntudesign/developer-data/), you can download the initial content from there.

1. Ensure you're logged in to GitHub with an account which has access to [ubuntudesign/developer-data](https://github.com/ubuntudesign/developer-data/)
2. Visit https://github.com/ubuntudesign/developer-data/raw/master/initial-content.json, which will forward you to a new URL for the fixture containing an access token, something like:
    ```
    https://raw.githubusercontent.com/ubuntudesign/developer-data/master/initial-content.json?token=xxx
    ```
3. Use this new URL to set the `INITIAL_CONTENT_FIXTURE`, e.g.:
    ```
    export INITIAL_CONTENT_FIXTURE=https://raw.githubusercontent.com/ubuntudesign/developer-data/master/initial-content.json?token=xxx
    ```
   before runnning the site for the first time

## Local development

The simplest way to run the site is to have [docker](https://www.docker.com/) installed and enabled for the current user, and then to run:

``` bash
make run
```

This should serve the site on `http://localhost:8017`.

For more in-depth instructions, see [HACKING.md](HACKING.md).
