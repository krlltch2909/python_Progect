from django.core.management.base import BaseCommand
from django.contrib.sites.models import Site
import os


class Command(BaseCommand):
    help = "Command for upgrade Sites"

    def add_arguments(self, parser):
        parser.add_argument('--get', action='store_true', help='Add this parameter if you want to all Sites')

    def handle(self, *args, **options):

        if options['get']:
            sites = list(Site.objects.all())
            print(sites)
        else:
            try:
                Site.objects.create(name=os.environ.get("SITE_ID", default="127.0.0.1"),
                                    domain=os.environ.get("DOMAIN_ID", default="127.0.0.1"))
            except:
                print("This Site already in use")
