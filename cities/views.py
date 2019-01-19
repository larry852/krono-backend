from rest_framework import viewsets
from .serializers import CitySerializer
from .models import City
from rest_framework.decorators import action
from rest_framework.response import Response
from stores.serializers import StoreSerializer
from stores.models import Store
from stores.filters import StoreFilter


class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer

    @action(detail=True, methods=['get'])
    def stores(self, request, pk=None):
        city = self.get_object()
        stores = StoreFilter(data=request.GET, queryset=Store.objects.filter(city=city)).qs
        serializer = StoreSerializer(stores, many=True)
        return Response(serializer.data)
