from django.db import models

from autoutilitare.models import Autoutilitare
from client.models import Client


class Comanda(models.Model):

    car = models.ForeignKey(Autoutilitare, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    observatii = models.TextField(max_length=200)

    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.id} {self.created_at}'
