from rest_framework.serializers import HyperlinkedModelSerializer
from .models import DRFUser


class DRFUserModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = DRFUser
        fields = ['username', 'first_name', 'last_name', 'email']


class DRFUserModelSerializerV2(HyperlinkedModelSerializer):
    class Meta:
        model = DRFUser
        fields = ['username', 'first_name', 'last_name', 'email', 'is_superuser', 'is_staff']

