from rest_framework.serializers import ModelSerializer

from drf_users.serializers import DRFUserModelSerializer
from todo_app.models import Project, TODOItem


class ProjectModelSerializer(ModelSerializer):
    users = DRFUserModelSerializer(many=True)

    class Meta:
        model = Project
        fields = ['name', 'repo', 'users']


class TODOItemModelSerializer(ModelSerializer):
    project = ProjectModelSerializer()
    author = DRFUserModelSerializer()

    class Meta:
        model = TODOItem
        fields = ['todo_text', 'project', 'author', 'created_at', 'updated_at']
