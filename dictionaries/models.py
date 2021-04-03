from django.db import models


# Единица измерения количества ингридиентов
class Unit(models.Model):
    name = models.CharField(
        max_length=32,
        verbose_name="Единица измерения",
        primary_key=True
    )

    def __str__(self):
        return self.name


class Ingridient(models.Model):
    name = models.CharField(
        max_length=60,
        verbose_name="Ингридиент",
        unique=True
    )
    unit = models.ForeignKey(
        Unit,
        on_delete=models.SET_NULL,
        null=True
    )

    def __str__(self):
        return self.name
