from rest_framework import routers
from .views import CityViewSet


router = routers.DefaultRouter()
router.register('cities', CityViewSet)
