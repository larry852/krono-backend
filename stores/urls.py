from rest_framework import routers
from .views import StoreViewSet


router = routers.DefaultRouter()
router.register('stores', StoreViewSet)
