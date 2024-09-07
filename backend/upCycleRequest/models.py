from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class UpCycleRequest(models.Model):
    requestsAt = models.DateField(null=True)
    store = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f' Request {self.id} '
