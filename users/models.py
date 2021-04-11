from django.contrib.auth.models import AbstractUser
from django.core.validators import EmailValidator
from django.db import models

from .validators import validate_name, validate_username


class User(AbstractUser):

    username = models.TextField(
        validators=[
            validate_username
        ],
        max_length=12,
        blank=False,
        null=False,
        unique=True,
        verbose_name="Логин"
    )

    email = models.EmailField(
        validators=[
            EmailValidator(message="Введите корректрый email адрес.")
        ],
        max_length=35,
        blank=False,
        null=False,
        unique=True,
        verbose_name="Email"
    )

    subscribes = models.ManyToManyField(
        "self",
        blank=True,
        related_name="subscribes",
        verbose_name="Подписки"
    )

    favorites = models.ManyToManyField(
        "recipes.Recipe",
        blank=True,
        related_name="favorites",
        verbose_name="Избранное"
    )

    shopping_list = models.ManyToManyField(
        "recipes.Recipe",
        blank=True,
        related_name="shopping_list",
        verbose_name="Список покупок"
    )
