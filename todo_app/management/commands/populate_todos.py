from random import choice

from django.core.management import BaseCommand

from drf_users.models import DRFUser
from todo_app.models import TODOItem, Project

SIZE = 200


class Command(BaseCommand):
    def handle(self, *args, **options):
        todo_texts = Command._create_todo_texts()
        all_users = list(DRFUser.objects.all())
        all_projects = list(Project.objects.all())
        if len(all_users) == 0 or len(all_projects) == 0:
            print('Execute populate_users and populate_projects before this command', file=self.stderr)
            exit(-1)
        for i in range(SIZE):
            author = choice(all_users)
            project = choice(all_projects)
            TODOItem.objects.create(
                todo_text=todo_texts[i],
                author=author,
                project=project
            )

    @classmethod
    def _create_todo_texts(cls):
        with open('adjectives.txt', encoding='utf-8') as adjectives, open('nouns.txt', encoding='utf-8') as nouns, open(
                'verbs.txt', encoding='utf-8') as verbs:
            adjectives_data = adjectives.readlines()
            nouns_data = nouns.readlines()
            verbs_data = verbs.readlines()
            return [
                f'{cls._choose_word(verbs_data)} {cls._choose_word(adjectives_data)} {cls._choose_word(nouns_data)}'
                for _ in range(SIZE)]

    @classmethod
    def _choose_word(cls, _list):
        return choice(_list).strip().capitalize()
