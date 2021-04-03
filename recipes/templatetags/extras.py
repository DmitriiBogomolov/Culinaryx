from django.template.defaulttags import register


# Template getitem helper
@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)


# Используется для склонения слов
@register.filter
def converte_word(value, word):

    def recipe_conv(value):
        last_d = int(str(value)[:1])

        if value in ['11', '12', '13', '14']:
            return 'рецептов'
        elif last_d == 1:
            return 'рецепт'
        elif last_d in [2, 3, 4]:
            return 'рецепта'
        else:
            return 'рецептов'

    converter = {
        'рецепт': recipe_conv
    }

    return converter[word](value)


# Формирует строку запроса из активных фильтров
@register.filter
def form_url_filter_params(filters, value):

    flts = filters.copy()

    if value:
        if value in filters:
            flts.remove(value)
        else:
            flts.append(value)

    out = ''

    inc = 1
    for flt in flts:
        out += f'flt_{str(inc)}={flt}&'
        inc += 1

    return out