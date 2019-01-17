from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from users.urls import router as users_router

router = routers.DefaultRouter()
router.registry.extend(users_router.registry)

urlpatterns = [
    path('', admin.site.urls),
    path('api/v1/', include(router.urls)),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
