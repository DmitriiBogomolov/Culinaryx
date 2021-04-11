from django.contrib import admin

from .models import Recipe, RecipeIngridient, Tag


class RecipeIngridientInline(admin.TabularInline):
    model = RecipeIngridient
    extra = 1


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    inlines = (RecipeIngridientInline,)
    empty_value_display = "-Пусто-"
    list_display = ("title", "author", "get_tags", "get_ingridients")

    def get_tags(self, obj):
        return " | ".join([tag.name for tag in obj.tags.all()])
    get_tags.short_description = "Тэги"

    def get_ingridients(self, obj):
        return "\n".join([tag.name for tag in obj.ingridients.all()])
    get_tags.get_ingridients = "Ингридиенты"


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    empty_value_display = "-Пусто-"
