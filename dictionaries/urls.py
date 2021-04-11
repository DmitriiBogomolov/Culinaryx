from django.urls import path

from .views import get_ingrediends_dict_view

urlpatterns = [
    path("ingredients/", get_ingrediends_dict_view, name="ingrediends"),
]
