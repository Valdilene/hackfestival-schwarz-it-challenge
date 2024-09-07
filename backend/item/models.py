from django.db import models

from upCycleRequest.models import UpCycleRequest


class Item(models.Model):
    name = models.CharField(max_length=100)
    expiresAt = models.CharField(max_length=100, null=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    weight = models.CharField(max_length=100)
    packagingUnit = models.CharField(max_length=100)
    available = models.IntegerField()
    upCycleRequest = models.ForeignKey(UpCycleRequest, related_name="items", on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"Item {self.id}: {self.expiresAt}"
