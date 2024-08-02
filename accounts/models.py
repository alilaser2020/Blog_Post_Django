from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    email = models.EmailField(max_length=100, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    age = models.PositiveIntegerField(null=True, blank=True)
    photo = models.ImageField(upload_to='photo/pofile/%Y/%m/%d', default='null')
    about = models.CharField(max_length=255, default='null')
