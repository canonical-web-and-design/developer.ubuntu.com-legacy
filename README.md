# The codebase for developer.ubuntu.com

## Dependencies

To run the project locally, you'll need some apt packages:

``` bash
sudo apt install python-dev python-django python-django-south python-psycopg2 pwgen virtualenv libpq-dev
```

Then install the python dependencies:

``` bash
pip install -r requirements.txt
```

## Run the site

``` bash
./manage.py runserver
```

## Importing data

For instructions for how to import some initial data (to get the site looking like developer.ubuntu.com),
visit [developer-data](https://github.com/ubuntudesign/developer-data) (you'll need to request access).

