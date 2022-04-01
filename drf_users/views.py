from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin

from .models import DRFUser
from .serializers import DRFUserModelSerializer, DRFUserModelSerializerV2


class DRFUserModelViewSet(CreateModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin, GenericViewSet):
    def get_serializer_class(self):
        if self.request.version == '2.0':
            return DRFUserModelSerializerV2
        return DRFUserModelSerializer

    queryset = DRFUser.objects.all()
