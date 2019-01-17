from rest_framework import serializers
from .models import Store
from users.serializers import UserSerializer


class StoreSerializer(serializers.ModelSerializer):
    users = UserSerializer(read_only=True, many=True)

    class Meta:
        model = Store
        fields = ('__all__')
        extra_kwargs = {
            'is_active': {'read_only': True},
        }
