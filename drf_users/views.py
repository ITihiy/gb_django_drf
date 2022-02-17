from rest_framework.viewsets import ModelViewSet

from .models import DRFUser
from .serializers import DRFUserModelSerializer


class DRFUserModelViewSet(ModelViewSet):
    queryset = DRFUser.objects.all()
    serializer_class = DRFUserModelSerializer
