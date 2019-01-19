from rest_framework import viewsets
from .serializers import CitySerializer
from .models import City
from rest_framework.decorators import detail_route
from rest_framework.response import Response
from stores.serializers import StoreSerializer
from stores.models import Store


class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer

    @detail_route(methods=['get'])
    def stores(self, request, pk=None):
        city = self.get_object()
        stores = Store.objects.filter(city=city)
        serializer = StoreSerializer(stores, many=True)
        return Response(serializer.data)
