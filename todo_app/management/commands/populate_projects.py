from random import choice, sample, randint

from django.core.management import BaseCommand

from drf_users.models import DRFUser
from todo_app.models import Project

SIZE = 20


class Command(BaseCommand):
    def handle(self, *args, **options):
        project_names = Command._create_project_names()
        all_users = list(DRFUser.objects.all())
        if len(all_users) == 0:
            print('Execute populate_users before this command', file=self.stderr)
            exit(-1)
        for i in range(SIZE):
            project_users = sample(all_users, k=randint(1, len(all_users)))
            current_project = Project.objects.create(
                name=project_names[i],
                repo=f'https://github.com/{project_users[0].username}/{project_names[i].replace(" ", "_").lower()}/',
            )
            current_project.users.set(project_users)

    @classmethod
    def _create_project_names(cls):
        with open('adjectives.txt', encoding='utf-8') as adjectives, open('nouns.txt', encoding='utf-8') as nouns:
            adjectives_data = adjectives.readlines()
            nouns_data = nouns.readlines()
            return [
                f'{choice(adjectives_data).strip().capitalize()} {choice(nouns_data).strip().capitalize()}'
                for _ in range(SIZE)]
