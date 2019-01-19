from django.db import models
from core.utils.file import get_path_class
from django.contrib.auth import get_user_model

User = get_user_model()


class Store(models.Model):
    users = models.ManyToManyField(User, blank=True)
    city = models.ForeignKey('cities.City', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to=get_path_class, default='default-store.png')
    is_active = models.BooleanField(default=True)
