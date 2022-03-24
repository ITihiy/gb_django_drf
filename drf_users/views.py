from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin

from .models import DRFUser
from .serializers import DRFUserModelSerializer


class DRFUserModelViewSet(CreateModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin, GenericViewSet):
    queryset = DRFUser.objects.all()
    serializer_class = DRFUserModelSerializer
