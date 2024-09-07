from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=100)
    expiresAt = models.DateTimeField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    packagingUnit = models.CharField(max_length=100)
    available = models.IntegerField()

    def __str__(self):
        return f"Item {self.id}: {self.expiresAt}"
