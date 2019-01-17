from rest_framework import viewsets
from .serializers import StoreSerializer
from .models import Store


class StoreViewSet(viewsets.ModelViewSet):
    queryset = Store.objects.filter(is_active=True)
    serializer_class = StoreSerializer
