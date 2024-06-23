from django.db import models
from django.contrib.auth.models import AbstractUser
from contents.manager import UserManager

class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=100,unique=True)
    bio = models.TextField(null=True, blank=True)

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    objects = UserManager()