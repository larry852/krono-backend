
from django_filters import FilterSet, CharFilter
from .models import Store


class StoreFilter(FilterSet):
    user = CharFilter(field_name='users')

    class Meta:
        model = Store
        fields = ['user']
