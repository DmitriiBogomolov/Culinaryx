from django.contrib import admin
from .models import Recipe, Tag, RecipeIngridient


class RecipeIngridientInline(admin.TabularInline):
    model = RecipeIngridient
    extra = 1


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    inlines = (RecipeIngridientInline,)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass


@admin.register(RecipeIngridient)
class RecipeIngridientAdmin(admin.ModelAdmin):
    pass
