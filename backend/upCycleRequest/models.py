from django.contrib.auth import get_user_model
from django.db import models

from item.models import Item

User = get_user_model()


class UpCycleRequest(models.Model):
    requestsAt = models.DateField()
    store = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(Item)

    def __str__(self):
        return f'{self.item} {self.quantity}'
