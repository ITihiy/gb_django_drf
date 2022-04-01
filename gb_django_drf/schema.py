import graphene
from graphene_django import DjangoObjectType

from drf_users.models import DRFUser
from todo_app.models import Project, TODOItem


class TODOItemType(DjangoObjectType):
    class Meta:
        model = TODOItem
        fields = '__all__'


class DRFUserType(DjangoObjectType):
    class Meta:
        model = DRFUser
        fields = '__all__'


class ProjectType(DjangoObjectType):
    class Meta:
        model = Project
        fields = '__all__'


class Query(graphene.ObjectType):
    all_projects = graphene.List(ProjectType)

    def resolve_all_projects(root, info):
        return Project.objects.all()


schema = graphene.Schema(query=Query)
