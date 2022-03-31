from mixer.backend.django import mixer
from rest_framework.test import APITestCase

from drf_users.models import DRFUser
from todo_app.models import Project


class TestProject(APITestCase):
    def test_creating_project(self):
        DRFUser.objects.create_superuser('admin', 'admin@mail.local', 'Qwerty123456')
        project = mixer.blend(Project)
        self.client.login(username='admin@mail.local', password='Qwerty123456')
        result = self.client.get('/api/drf_projects/1/')
        self.assertEqual(result.data['name'], project.name)
