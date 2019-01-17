from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ('password', 'last_login', 'date_joined', 'is_superuser', 'is_staff', 'user_permissions', 'groups')
        extra_kwargs = {
            'password': {'write_only': True}
        }
