from django.urls import reverse_lazy
from django.views.generic.list import ListView

from recipes.models import Recipe, RecipeIngridient, Tag

from .QueryFilters import filter_by_tags, parse_filters_from_url
from .SafePaginator import SafePaginator
from django.core.exceptions import ImproperlyConfigured


class FilteredListView(ListView):
    paginator_class = SafePaginator
    filters = []
    tags_all = Tag.objects.all()
    url = reverse_lazy('recipes')

    def get_queryset(self, queryset=None):

        if queryset is None:

            if self.model is not None:
                queryset = super().get_queryset()
            else:
                raise ImproperlyConfigured(
                    "%(cls)s is missing a QuerySet. Define "
                    "%(cls)s.model, %(cls)s.queryset, or override "
                    "%(cls)s.get_queryset(). "
                    "Use super().get_queryset(custom_qs) "
                    "for more variability. " % {
                        'cls': self.__class__.__name__
                    }
                )

        url_qstring = self.request.META['QUERY_STRING']
        self.filters = parse_filters_from_url(url_qstring)
        filtered_queryset = filter_by_tags(queryset, self.filters, self.tags_all)

        return filtered_queryset

    def get_context_data(self, **kwargs):
        context = super(FilteredListView, self).get_context_data(**kwargs)

        context['url'] = self.url
        context['filters'] = self.filters
        context['tags'] = self.tags_all

        return context