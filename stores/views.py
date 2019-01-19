from rest_framework import viewsets
from .serializers import StoreSerializer, DetailStoreSerializer
from .models import Store
from rest_framework.decorators import action
from rest_framework.response import Response
from users.serializers import UserSerializer


class StoreViewSet(viewsets.ModelViewSet):
    queryset = Store.objects.filter(is_active=True)
    serializer_class = StoreSerializer
    detail_serializer_class = DetailStoreSerializer

    def get_serializer_class(self):
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
