# Import DQoc HTML from lp:ubuntu-ui-toolkit
import os, sys, re

from optparse import make_option
import xml.etree.ElementTree as ET

from django.core.management.base import BaseCommand
from django.core.files import File
from django.core.files.storage import get_storage_class
from django.conf import settings

from api_docs.models import *
from api_docs.importers.qdoc import QDocImporter


__all__ = (
    'Command',
)

class Command(BaseCommand):
    
    option_list = BaseCommand.option_list + (
        make_option(
            "-i",
            "--index",
            dest="index",
            help="QDoc .index file to import documentation from",
        ),
        make_option(
            "-s",
            "--section",
            dest="section",
            help="Section the documentation if from",
        ),
        make_option(
            "-r",
            "--release",
            dest="version",
            help="Version of the topic the documentation if from",
        ),
        make_option(
            "-t",
            "--topic",
            dest="topic",
            help="Topic the documentation if from",
        ),
        make_option(
            "-n",
            "--namespace",
            dest="namespace",
            help="Fallback namespace to use if none is provided in the docs",
        ),
        make_option(
            "-N",
            "--force-namespace",
            dest="force_namespace",
            help="Force a specific namespace, ignoring anything in the docs",
        ),
        make_option(
            "-p",
            "--pages",
            dest="all_pages",
            action="store_true",
            help="Import all Pages, not just those referenced by Elements",
        ),
        make_option(
            "-P",
            "--force-pages",
            dest="force_pages",
            action="store_true",
            help="Import pages of any type",
        ),
        make_option(
            "-l",
            "--lang",
            dest="lang",
            help="Target programming language (cpp or qml)",
        ),
    )

    def handle(self, *args, **options):
        lang = options.get('lang', 'qml')
        verbosity = int(options.get('verbosity', 0))
        topic = Topic.objects.get(slug=options.get('topic'))
        language = Language.objects.get(slug=options.get('lang'), topic=topic)
        if options.get('version') == 'development':
            version = language.development_version
        elif options.get('version') == 'current':
            version = language.current_version
        else:
            version = Version.objects.get(slug=options.get('version'), language=language)
        section, created = Section.objects.get_or_create(name=options.get('section'), topic_version=version)
        
        importer = QDocImporter(topic, language, version, section, options)
        importer.run()
