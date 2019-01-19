from rest_framework import viewsets
from .serializers import StoreSerializer
from .models import Store
from rest_framework.decorators import detail_route
from rest_framework.response import Response
from users.serializers import UserSerializer


class StoreViewSet(viewsets.ModelViewSet):
    queryset = Store.objects.filter(is_active=True)
    serializer_class = StoreSerializer

    @detail_route(methods=['get'])
    def users(self, request, pk=None):
        store = self.get_object()
        users = store.users.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
