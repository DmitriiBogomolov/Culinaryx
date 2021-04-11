# Generated by Django 3.1.7 on 2021-04-05 12:47

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0004_auto_20210401_1910'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='time',
            field=models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(600), django.core.validators.MinValueValidator(1)], verbose_name='Время приготовления в минутах'),
        ),
    ]