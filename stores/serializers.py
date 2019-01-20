from rest_framework import serializers
from .models import Store
from users.serializers import UserSerializer
from cities.serializers import CitySerializer
from django.contrib.auth import get_user_model

User = get_user_model()


class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = ('__all__')
        extra_kwargs = {
            'is_active': {'read_only': True},
        }


class DetailStoreSerializer(StoreSerializer):
    users = UserSerializer(read_only=True, many=True)
    city = CitySerializer()


class UsersFormSerializer(serializers.Serializer):
    users = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), many=True, help_text='Users related Store')

    class Meta:
        model = Store
        fields = ('users',)
