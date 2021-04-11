from django.urls import path

from .views import (FavoritesView, ProfileView, RecipeCreateView,
                    RecipeDetailView, RecipeEditView, RecipesView,
                    ShoppingListView, SubscribesView, add_favorite,
                    add_purchases, add_subscription, get_shopping_list_txt,
                    remove_favorite, remove_purchases, remove_subscription)

urlpatterns = [
    path("shopping_list/", ShoppingListView.as_view(), name="shopping_list"),
    path("favorites/", FavoritesView.as_view(), name="favorites"),
    path("recipe_create/", RecipeCreateView.as_view(), name="recipe_create"),
    path("recipe_edit/<int:pk>/", RecipeEditView.as_view(), name="recipe_edit"),
    path("recipe/<int:pk>/", RecipeDetailView.as_view(), name="recipe_detail"),
    path("subscribes/", SubscribesView.as_view(), name="subscribes"),
    path("profile/<str:username>/", ProfileView.as_view(), name="profile"),


    path("download_shopping_list/", get_shopping_list_txt, name="download_shopping_list"),
    path("purchases/", add_purchases, name="add_purchases"),
    path("purchases/<int:pk>/", remove_purchases, name="remove_purchases"),
    path("favorite/", add_favorite, name="add_favorite"),
    path("favorite/<int:pk>/", remove_favorite, name="remove_favorite"),
    path("subscribe/", add_subscription, name="add_subscribtion"),
    path("subscribe/<int:pk>/", remove_subscription, name="remove_subscribtion"),

    path("", RecipesView.as_view(), name="recipes"),
]
