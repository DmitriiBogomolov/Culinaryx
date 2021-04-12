from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.flatpages import views
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("auth/", include("users.urls")),
    path("dicts/", include("dictionaries.urls")),
    path("", include("recipes.urls")),
]


urlpatterns += static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
)


urlpatterns += [
    #path("pages/", include('django.contrib.flatpages.urls')),
    path(
        "about/",
        views.flatpage,
        {'url': '/about/'},
        name='about'
    )
]


handler404 = "recipes.views.custom_404_view"
