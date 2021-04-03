from django.db import models
from dictionaries.models import Ingridient
from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator
from django.shortcuts import reverse


User = get_user_model()


"     ----    ----    ----    ----    ----    ----    ----    ----    ----    "


class Tag(models.Model):

    name = models.CharField(
        max_length=24,
        primary_key=True,
        verbose_name="Название тэга."
    )

    color = models.CharField(default='green', max_length=30)

    def __str__(self):
        return self.name


"     ----    ----    ----    ----    ----    ----    ----    ----    ----    "


class Recipe(models.Model):

    title = models.CharField(
        max_length=24,
        verbose_name="Название"
    )

    description = models.TextField(
        max_length=300,
        verbose_name="Описание"
    )

    image = models.ImageField(
        upload_to="recipes/",
        blank=True,
        null=True,
        verbose_name="Изображение"
    )

    author = models.ForeignKey(
        User,
        verbose_name="Автор",
        on_delete=models.SET_NULL,
        null=True
    )

    tags = models.ManyToManyField(
        Tag,
        verbose_name="Тэги"
    )

    ingridients = models.ManyToManyField(
        Ingridient,
        through="RecipeIngridient"
    )

    time = models.IntegerField(
        verbose_name="Время приготовления в минутах",
        validators=[MaxValueValidator(600), MinValueValidator(1)]
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('recipe_detail', kwargs={'pk': self.id})


"     ----    ----    ----    ----    ----    ----    ----    ----    ----    "


class RecipeIngridient(models.Model):

    recipe = models.ForeignKey(
        Recipe,
        verbose_name="Рецепт",
        on_delete=models.CASCADE
    )

    ingridient = models.ForeignKey(
        Ingridient,
        verbose_name="Ингридиент",
        on_delete=models.CASCADE
    )

    value = models.IntegerField(
        verbose_name="Количество"
    )
