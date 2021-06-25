from django.db import models

from fastOrder.utils.models import FastOrderModel


class Platillo(FastOrderModel):
    name = models.CharField('platillo', max_length=140)
    price = models.FloatField('price')
    comida_choices = (
        ('Desayuno', 'Desayuno'),
        ('Almuerzo', 'Almuerzo'),
        ('Cena', 'Cena'),
    )
    comida = models.CharField(max_length=35, blank=False, null=True, choices=comida_choices)
    description = models.TextField(max_length=500, blank=True)

    def __str__(self):
        return self.name


class Bebida(FastOrderModel):
    name = models.CharField('bebida name', max_length=140)
    price = models.FloatField('price')
    bebida_choices = (
        ('Bebidas con alcohol', 'Bebidas con alcohol'),
        ('Bebidas sin alcohol', 'Bebidas sin alcohol'),
        ('Bebidas calientes', 'Bebidas calientes'),
        ('Cerveza', 'Cerveza'),
    )
    bebida = models.CharField(max_length=60, blank=False, null=True, choices=bebida_choices)
    description = models.TextField(max_length=500, blank=True)

    def __str__(self):
        return self.name


class Postre(FastOrderModel):
    name = models.CharField('postre', max_length=140)
    price = models.FloatField('price')
    description = models.TextField(max_length=500, blank=True)

    def __str__(self):
        return self.name
