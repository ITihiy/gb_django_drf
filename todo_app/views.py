from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.viewsets import ModelViewSet

from todo_app.models import Project, TODOItem
from todo_app.serializers import ProjectModelSerializer, TODOItemModelSerializer


class ProjectsLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 10


class TODOLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 20


class ProjectModelViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectModelSerializer
    pagination_class = ProjectsLimitOffsetPagination
    filter_backends = [DjangoFilterBackend,]
    filter_fields = ['name', 'repo']


class TODOItemModelViewSet(ModelViewSet):
    queryset = TODOItem.objects.all()
    serializer_class = TODOItemModelSerializer
    pagination_class = TODOLimitOffsetPagination
    filter_backends = [DjangoFilterBackend,]
    filter_fields = ['todo_text', 'is_active']
