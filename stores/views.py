from rest_framework import viewsets
from .serializers import StoreSerializer, DetailStoreSerializer, UsersFormSerializer
from .models import Store
from rest_framework.decorators import action
from rest_framework.response import Response
from users.serializers import UserSerializer


class StoreViewSet(viewsets.ModelViewSet):
    queryset = Store.objects.filter(is_active=True)
    serializer_class = StoreSerializer
    detail_serializer_class = DetailStoreSerializer
    users_form_serializer = UsersFormSerializer

    def get_serializer_class(self):
        if self.action == 'associate' or self.action == 'disassociate':
            if hasattr(self, 'users_form_serializer'):
                return self.users_form_serializer
        if self.action == 'retrieve':
            if hasattr(self, 'detail_serializer_class'):
                return self.detail_serializer_class
        return self.serializer_class

    @action(detail=True, methods=['get'])
    def users(self, request, pk=None):
        store = self.get_object()
        users = store.users.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['patch'])
    def associate(self, request, pk=None):
        store = self.get_object()
        users = self.get_validated_users(request.data)
        store.users.add(*users)
        return self.users(request, pk=None)

    @action(detail=True, methods=['patch'])
    def disassociate(self, request, pk=None):
        store = self.get_object()
        users = self.get_validated_users(request.data)
        store.users.remove(*users)
        return self.users(request, pk=None)

    def get_validated_users(self, data):
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        return serializer.validated_data.get('users')
