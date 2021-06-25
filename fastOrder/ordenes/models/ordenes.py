from django.db import models

from fastOrder.utils.models import FastOrderModel
from fastOrder.menus.models import Bebida, Platillo, Postre

class Orden(FastOrderModel):
    bebida = models.ManyToManyField(Bebida)
    platillo = models.ManyToManyField(Platillo)
    postre = models.ManyToManyField(Postre)
    comments = models.TextField(max_length=500, blank=True)

    def __str__(self):
        return str(self.pk)
