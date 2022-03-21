from rest_framework.viewsets import ModelViewSet

from todo_app.models import Project, TODOItem
from todo_app.serializers import ProjectModelSerializer, TODOItemModelSerializer


class ProjectModelViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectModelSerializer


class TODOItemModelViewSet(ModelViewSet):
    queryset = TODOItem.objects.all()
    serializer_class = TODOItemModelSerializer
