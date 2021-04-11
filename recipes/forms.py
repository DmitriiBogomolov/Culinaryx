from django import forms
from django.contrib.auth import get_user_model
from django.core import validators
from django.core.exceptions import ValidationError

from dictionaries.models import Ingridient

from .models import Recipe, RecipeIngridient, Tag

user = get_user_model()


class RecipeForm(forms.ModelForm):

    # Используется для отображения ошибок
    ingridients = forms.CharField(initial='None', required=False)

    ingridients_list = []

    class Meta:
        model = Recipe
        exclude = ['author', 'ingridients']

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(RecipeForm, self).__init__(*args, **kwargs)

    def clean_ingridients(self):
        """
        Обрабатывает неопределенное количество полей формы вида
        'nameIngredient_1=name', 'valueIngredient_1=value'
        сохраняет список ингридиентов ingridients_list
        """
        data = self.data

        self.ingridients_list = []

        for key in data.keys():
            if key.startswith('nameIngredient_'):
                index = key.rsplit('_')[1]

                ingridient = data['nameIngredient_' + str(index)]
                value = data['valueIngredient_' + str(index)]

                try:
                    ingridient = Ingridient.objects.get(name=ingridient)

                    try:
                        validate_value(self, value)
                        self.ingridients_list.append([ingridient, value])
                    except ValidationError:
                        pass

                except Ingridient.DoesNotExist:
                    self.add_error('ingridients', "Недопустимый ингридиент.")

        if not self.ingridients_list:
            self.add_error('ingridients', "Укажите ингридиенты.")

    # Проверяет поступившие тэги
    def clean_tags(self):
        data = self.cleaned_data['tags']

        if not data:
            self.add_error('tags', "Укажите тэги.")
            raise ValidationError("Укажите тэги.")

        for tag in data:
            if tag not in Tag.objects.all():
                self.add_error('tags', "Недопустимый тэг.")
                raise ValidationError("Недопустимый тэг.")

        return data

    def save(self, commit=True):
        """
        Устанавливает автора, создает промежуточные таблицы,
        сохрняет форму
        """
        instance = super(RecipeForm, self).save(commit=False)
        instance.author = self.user

        instance.save()

        # Тэги
        instance.tags.set(
            Tag.objects.filter(
                name__in=self.cleaned_data.get("tags")
            )
        )

        # Промежуточная таблица Recipe - Ingridient - Value
        RecipeIngridient.objects.filter(recipe=instance).delete()
        for unit in self.ingridients_list:
            RecipeIngridient.objects.create(recipe=instance, ingridient=unit[0], value=unit[1])
        instance.save()

        return instance


# Используется для валидации value ингридиента
def validate_value(self, value):
    try:
        value = int(value)

    except ValueError:

        raise ValidationError(
                _('Недопустимое количество для ингридиента.')
            )

    validators.MinValueValidator(0)(value)
    validators.MaxValueValidator(6000)(value)
