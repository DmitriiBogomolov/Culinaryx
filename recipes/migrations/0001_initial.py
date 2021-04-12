# Generated by Django 3.1.7 on 2021-04-12 12:15

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('dictionaries', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=24, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Описание')),
                ('image', models.ImageField(blank=True, null=True, upload_to='recipes/', verbose_name='Изображение')),
                ('time', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(600), django.core.validators.MinValueValidator(1)], verbose_name='Время приготовления в минутах')),
            ],
            options={
                'verbose_name': 'Рецепт',
                'verbose_name_plural': 'Рецепты',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('name', models.CharField(max_length=24, primary_key=True, serialize=False, verbose_name='Название тэга')),
                ('color', models.CharField(default='green', max_length=30, verbose_name='Цвет (дополняет класс элемента dom)')),
            ],
            options={
                'verbose_name': 'Тэг',
                'verbose_name_plural': 'Тэги',
            },
        ),
        migrations.CreateModel(
            name='RecipeIngridient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.IntegerField(verbose_name='Количество')),
                ('ingridient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dictionaries.ingridient', verbose_name='Ингридиент')),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipes.recipe', verbose_name='Рецепт')),
            ],
        ),
    ]
