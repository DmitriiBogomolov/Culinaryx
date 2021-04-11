from django.contrib import admin

from .models import Ingridient, Unit


class UnitAdmin(admin.ModelAdmin):
    empty_value_display = "-Пусто-"


class IngridientAdmin(admin.ModelAdmin):
    empty_value_display = "-Пусто-"


admin.site.register(Unit, UnitAdmin)
admin.site.register(Ingridient, IngridientAdmin)
