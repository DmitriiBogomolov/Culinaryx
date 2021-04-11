import urllib

from django.db.models import Q


def filter_by_tags(queryset, tags_to_filter, tags_all):
    """
    Фильтр queryset, получает список тэгов для фильтрации
    и список доступных тэгов
    предоставляет элементы queryset, имеющие хотя бы один
    тэг, не совпадающий с tags_to_filter
    """

    tag_list = [x.name for x in tags_all]

    current_tag_list = tag_list.copy()

    for name in tag_list:
        if name in tags_to_filter:
            current_tag_list.remove(name)

    if not current_tag_list:
        return queryset

    q = Q()
    for tag in current_tag_list:
        q |= Q(tags__name=tag)

    return queryset.filter(q).distinct()


def parse_filters_from_url(url_qstring):
    """
    Парсит из строки запроса список тэгов для фильтрации
    """
    url_params_string = urllib.parse.unquote(url_qstring)
    filters = []
    filters = url_params_string.split('&')
    filters = list(filter(lambda x: x.startswith('flt'), filters))
    filters = list(map(lambda x: x.rsplit('=')[1], filters))

    return filters
