from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    code = models.CharField(
        verbose_name='code',
        max_length=100,
        unique=True
    )
    is_superuser = models.BooleanField(default=True)

    def __str__(self):
        return f"Store {self.id}: {self.code}"

