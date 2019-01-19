
from django_filters import FilterSet
from .models import Store


class StoreFilter(FilterSet):
    class Meta:
        model = Store
        fields = ['city']
