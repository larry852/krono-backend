from rest_framework import serializers
from .models import Store
from users.serializers import UserSerializer
from cities.serializers import CitySerializer


class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = ('__all__')
        extra_kwargs = {
            'is_active': {'read_only': True},
        }


class DetailStoreSerializer(serializers.ModelSerializer):
    users = UserSerializer(read_only=True, many=True)
    city = CitySerializer()

    class Meta:
        model = Store
        fields = ('__all__')
        extra_kwargs = {
            'is_active': {'read_only': True},
        }
