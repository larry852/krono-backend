from django.db import models
from django.contrib.auth.models import AbstractUser
from .choices import GENDER_CHOICES
from core.utils.file import get_path_class


class CustomUser(AbstractUser):
    birthdate = models.DateField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='')
    avatar = models.ImageField(upload_to=get_path_class, default='default-profile.png')
