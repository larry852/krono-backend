from django.contrib import admin
from .models import Store


@admin.register(Store)
class AdminOrganization(admin.ModelAdmin):
    list_display = ('id', 'city', 'name', 'logo', 'is_active')
