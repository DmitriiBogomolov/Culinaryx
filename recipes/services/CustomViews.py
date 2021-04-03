from django.urls import reverse_lazy
from recipes.models import Recipe, RecipeIngridient, Tag
from .QueryFilters import (filter_by_tags,
                           parse_filters_from_url)
from django.views.generic.list import ListView
from .SafePaginator import SafePaginator

class FilteredListView(ListView):
    paginator_class = SafePaginator
    filters = []
    tags_all = Tag.objects.all()
    url = reverse_lazy('recipes')

    def get_queryset(self, queryset=None): 
        if not queryset:
            queryset = super().get_queryset()
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