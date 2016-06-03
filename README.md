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

And provision the database, [importing initial data](https://github.com/ubuntudesign/developer-data) if you have it:

``` bash
# If you have an initial database fixture, either:
# - Provide an INITIAL_FIXTURE_URL, or
# - Place the fixture in developer_portal/fixtures/initial_content.json

./manage.py migrate --noinput
```

## Run the site

``` bash
./manage.py runserver
```
