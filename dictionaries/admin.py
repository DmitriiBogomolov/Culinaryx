from django.contrib import admin
from .models import Unit, Ingridient


class UnitAdmin(admin.ModelAdmin):
    pass


class IngridientAdmin(admin.ModelAdmin):
    pass


admin.site.register(Unit, UnitAdmin)
admin.site.register(Ingridient, IngridientAdmin)
