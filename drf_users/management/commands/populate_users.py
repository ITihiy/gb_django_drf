import os

from django.conf import settings
from django.core.management import BaseCommand
from dotenv import load_dotenv

from drf_users.models import DRFUser


class Command(BaseCommand):
    def handle(self, *args, **options):
        load_dotenv(settings.BASE_DIR / '.env')

        DRFUser.objects.create_superuser(
            username=os.environ.get('SUPERUSER_USERNAME'),
            first_name=os.environ.get('SUPERUSER_FIRSTNAME'),
            last_name=os.environ.get('SUPERUSER_LASTNAME'),
            password=os.environ.get('SUPERUSER_PASSWORD'),
            email=os.environ.get('SUPERUSER_EMAIL')
        )

        for i in range(10):
            DRFUser.objects.create_user(
                username=f'django_{i}',
                email=f'django_{i}@email.local',
                password='geekbrains',
                first_name=f'django_{i}',
                last_name=f'django_{i}'
            )
