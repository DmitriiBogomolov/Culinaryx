import json

from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseNotAllowed, JsonResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView

from dictionaries.models import Ingridient

from .forms import RecipeForm
from .models import Recipe, RecipeIngridient
from .services.CustomViews import FilteredListView
from .services.SafePaginator import SafePaginator
from .services.ShoppingList import (build_shopping_list,
                                    get_string_by_shopping_list)

User = get_user_model()


"     ----    ----    ----    ----    ----    ----    ----    ----    ----    "

"""
                ListViews
"""

"     ----    ----    ----    ----    ----    ----    ----    ----    ----    "


# Страница рецептов
class RecipesView(FilteredListView):
    model = Recipe
    template_name = "recipes/recipes.html"
    context_object_name = "recipes"
    paginate_by = 6
    url = reverse_lazy("recipes")


# Страница избранного
@method_decorator(login_required, name="dispatch")
class FavoritesView(FilteredListView):
    template_name = "recipes/favorites.html"
    context_object_name = "favorites"
    paginate_by = 6
    url = reverse_lazy("favorites")

    def get_queryset(self):
        queryset = super().get_queryset(self.request.user.favorites.all())
        return queryset


# Страница профиля пользователя
class ProfileView(FilteredListView):
    template_name = "recipes/profile.html"
    context_object_name = "recipes"
    paginate_by = 6

    def get_queryset(self):
        self.profile = get_object_or_404(User, username=self.kwargs["username"])
        queryset = super().get_queryset(Recipe.objects.filter(author=self.profile))
        return queryset

    def get_context_data(self, **kwargs):
        self.url = reverse_lazy("profile", kwargs={"username": self.kwargs["username"]})
        context = super(ProfileView, self).get_context_data(**kwargs)

        if self.request.user.is_authenticated:
            subscribed = self.request.user.subscribes.filter(id=self.profile.id).exists()
        else:
            subscribed = []

        context["profile"] = self.profile
        context["subscribed"] = subscribed

        return context


# Страница подписок
@method_decorator(login_required, name="dispatch")
class SubscribesView(ListView):
    template_name = "recipes/subscribes.html"
    context_object_name = "subscribes"
    displayed_recipes_count = 3
    paginator_class = SafePaginator
    paginate_by = 6

    def get_queryset(self):
        user = self.request.user
        return user.subscribes.all()

    def get_context_data(self, **kwargs):
        context = super(SubscribesView, self).get_context_data(**kwargs)

        subscribe_recipes = {}
        subscribe_recipes_count = {}

        for author in self.get_queryset().values():
            query = Recipe.objects.filter(author__id=author["id"])
            set_to_context = query[:self.displayed_recipes_count]
            subscribe_recipes[author["id"]] = set_to_context
            subscribe_recipes_count[author["id"]] = query.count() - set_to_context.count()

        context["subscribe_recipes"] = subscribe_recipes
        context["subscribe_recipes_count"] = subscribe_recipes_count

        return context


# Страницы списка покупок
@method_decorator(login_required, name="dispatch")
class ShoppingListView(ListView):
    template_name = "recipes/shopping_list.html"
    context_object_name = "recipes"

    def get_queryset(self):
        user = self.request.user
        return user.shopping_list.all()


# Возвращает файл с ингридиентами из списка покупок
@login_required
def get_shopping_list_txt(request):
    file_name = "recipes/shopping_list.txt"
    slist = build_shopping_list(request)

    response_content = get_string_by_shopping_list(slist)

    response = HttpResponse(response_content, content_type="text/plain, charset=utf8")
    response["Content-Disposition"] = f"attachment; filename={file_name}"

    return response


"     ----    ----    ----    ----    ----    ----    ----    ----    ----    "

"""
                EditViews
"""

"     ----    ----    ----    ----    ----    ----    ----    ----    ----    "

@method_decorator(login_required, name="dispatch")
class RecipeCreateView(CreateView):
    # Уникальные элементы шаблона
    title = "Создание рецепта"
    button_capture = "Создать рецепт"
    action = reverse_lazy("recipe_create")

    template_name = "recipes/recipe_edit.html"
    form_class = RecipeForm

    def get_context_data(self, **kwargs):
        context = super(RecipeCreateView, self).get_context_data(**kwargs)

        context["title"] = self.title
        context["action"] = self.action
        context["button_capture"] = self.button_capture

        return context

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(RecipeCreateView, self).get_form_kwargs()
        kwargs["user"] = self.request.user
        return kwargs


@method_decorator(login_required, name="dispatch")
class RecipeEditView(UpdateView):
    # Уникальные элементы шаблона
    title = "Редактировать рецепт"
    button_capture = "Сохранить изменения"
    action = "См. get_object"

    template_name = "recipes/recipe_edit.html"
    form_class = RecipeForm
    ingridients_list = []

    def get_object(self):
        obj_id = self.kwargs["pk"]
        obj = Recipe.objects.get(id=obj_id)

        self.action = reverse_lazy("recipe_edit", kwargs={"pk": obj_id})

        # Заполняем ingridients_list из связанной таблицы
        qs = RecipeIngridient.objects.filter(recipe=obj).values()
        self.ingridients_list = []

        for recipeing in qs:
            ingridient = Ingridient.objects.get(id=recipeing["ingridient_id"])
            self.ingridients_list.append([ingridient, recipeing["value"]])

        return obj

    def get_context_data(self, **kwargs):
        context = super(RecipeEditView, self).get_context_data(**kwargs)

        # При первой загрузке формы нормализуем данные под шаблон
        if self.request.method == "GET":
            obj = self.get_object()

            form_class = self.form_class
            form = form_class(
                {
                    "title": obj.title,
                    "description": obj.description,
                    "image": obj.image,
                    "tags": obj.tags.all(),
                    "time": obj.time
                }
            )

            context["form"] = form

            for index, ing in enumerate(self.ingridients_list):
                form.data["nameIngredient_" + str(index)] = ing[0].name
                form.data["valueIngredient_" + str(index)] = ing[1]

            form.is_valid()

        context["title"] = self.title
        context["action"] = self.action
        context["button_capture"] = self.button_capture

        return context

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(RecipeEditView, self).get_form_kwargs(*args, **kwargs)
        kwargs["user"] = self.request.user

        return kwargs

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.author != self.request.user:
            return HttpResponseNotAllowed(["GET", "POST"])
        return super(RecipeEditView, self).dispatch(request, *args, **kwargs)


"     ----    ----    ----    ----    ----    ----    ----    ----    ----    "

"""
                Detail Views
"""

"     ----    ----    ----    ----    ----    ----    ----    ----    ----    "


# Страница рецепта
class RecipeDetailView(DetailView):
    template_name = "recipes/recipe.html"
    model = Recipe

    def get_context_data(self, **kwargs):
        context = super(RecipeDetailView, self).get_context_data(**kwargs)

        recipe = get_object_or_404(Recipe, id=self.kwargs["pk"])

        if self.request.user.is_authenticated:
            subscribed = self.request.user.subscribes.filter(id=recipe.author.id).exists()
        else:
            subscribed = []

        context["subscribed"] = subscribed
        return context


"     ----    ----    ----    ----    ----    ----    ----    ----    ----    "

"""
API методы для работы с подписками, покупками и избранным
"""

"     ----    ----    ----    ----    ----    ----    ----    ----    ----    "


@login_required
def add_subscription(request):
    if request.method == "POST":
        data = json.loads(request.body)
        user_target = get_object_or_404(User, id=data["id"])
        request.user.subscribes.add(user_target)

        return JsonResponse({"success": True})


@login_required
def remove_subscription(request, pk):
    if request.method == "DELETE":
        user_target = get_object_or_404(User, id=pk)
        request.user.subscribes.remove(user_target)

        return JsonResponse({"success": True})


@login_required
def add_favorite(request):
    if request.method == "POST":
        data = json.loads(request.body)
        recipe_target = get_object_or_404(Recipe, id=data["id"])
        request.user.favorites.add(recipe_target)

        return JsonResponse({"success": True})


@login_required
def remove_favorite(request, pk):
    if request.method == "DELETE":
        recipe_target = get_object_or_404(Recipe, id=pk)
        request.user.favorites.remove(recipe_target)

        return JsonResponse({"success": True})


@login_required
def add_purchases(request):
    print("--------------------------")
    if request.method == "POST":
        data = json.loads(request.body)
        recipe_target = get_object_or_404(Recipe, id=data["id"])
        request.user.shopping_list.add(recipe_target)

        return JsonResponse({"success": True})


@login_required
def remove_purchases(request, pk):
    if request.method == "DELETE":
        recipe_target = get_object_or_404(Recipe, id=pk)
        request.user.shopping_list.remove(recipe_target)

        return JsonResponse({"success": True})


def custom_404_view(request, exception):
    data = {"name": "yoursite.com"}
    return render(request, "recipes/404.html", data)
