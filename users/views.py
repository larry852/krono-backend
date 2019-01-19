from rest_framework import viewsets
from .serializers import UserSerializer
from django.contrib.auth import get_user_model
from rest_framework.decorators import action
from stores.serializers import StoreSerializer
from rest_framework.response import Response

User = get_user_model()


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.filter(is_staff=False)
    serializer_class = UserSerializer

    @action(detail=True, methods=['get'])
    def stores(self, request, pk=None):
        user = self.get_object()
        stores = user.store_set.all()
        serializer = StoreSerializer(stores, many=True)
        return Response(serializer.data)
