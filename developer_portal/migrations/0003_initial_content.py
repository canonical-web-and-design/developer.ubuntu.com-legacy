# System modules
import os
import urllib

# Third party modules
from django.core.management import call_command
from django.db import migrations
from django.apps import apps
from django.db.models.signals import post_migrate


def download_fixture(fixture_url, target_path):
    """
    Download a fixture JSON file into a specified location
    """

    file_exists = os.path.isfile(target_path)

    if not file_exists and fixture_url:
        print("Downloading '{}' to '{}'...".format(fixture_url, target_path))
        urllib.URLopener().retrieve(fixture_url, target_path)
        print("Downloaded")
        file_exists = os.path.isfile(target_path)

    return file_exists


def finish_previous_migrations(migrate_apps):
    """
    Explicitly run the post_migrate actions
    for all apps
    """

    for app_config in apps.get_app_configs():
        post_migrate.send(
            sender=app_config,
            app_config=app_config
        )


def load_initial_content(migrate_apps, schema_editor):
    """
    Load the website content fixture
    """

    finish_previous_migrations(migrate_apps)
    if download_fixture(
        fixture_url=os.environ.get('INITIAL_FIXTURE_URL'),
        target_path="developer_portal/fixtures/initial_content.json"
    ):
        print("Loading initial_content...")
        call_command("loaddata", "initial_content")
        print("Loaded")


class Migration(migrations.Migration):
    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
        ('sites', '0001_initial'),
        ('cms', '0014_auto_20160404_1908'),
        ('zinnia', '0001_initial'),
        ('tagging', '0001_initial'),
        ('cmsplugin_zinnia', '0001_initial'),
        ('developer_portal', '0002_update_rawhtml_data_type'),
        ('django_comments', '0003_add_submit_date_index'),
        ('django_openid_auth', '0001_initial'),
        ('djangocms_inherit', '0002_auto_20150622_1244'),
        ('djangocms_link', '0005_auto_20151003_1710'),
        ('djangocms_picture', '0002_auto_20151018_1927'),
        ('djangocms_snippet', '0004_auto_alter_slug_unique'),
        ('djangocms_text_ckeditor', '0003_set_related_name_for_cmsplugin_ptr'),
        ('djangocms_video', '0002_set_related_name_for_cmsplugin_ptr'),
        ('md_importer', '0004_move_from_page_object_to_url_string'),
        ('menus', '0001_initial'),
        ('reversion', '0002_auto_20141216_1509'),
        ('sessions', '0001_initial'),
        ('store_data', '0003_make_iconurl_optional'),
        ('zinnia', '0003_publication_date'),
    ]
    operations = [
        migrations.RunPython(load_initial_content),
    ]
