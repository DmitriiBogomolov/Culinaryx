from recipes.models import RecipeIngridient


def build_shopping_list(request):
    """
    Из связанной таблицы ингридиентов компонует
    общий shopping list
    """

    sdict = {}

    for recipe in request.user.shopping_list.all():

        for through in RecipeIngridient.objects.filter(recipe=recipe):
            if through.ingridient.name in sdict:
                sdict[through.ingridient.name][0] += through.value
            else:
                sdict[through.ingridient.name] = [through.value, through.ingridient.unit.name]


    slist = []
    for key in sdict.keys():
        slist.append([key, sdict[key][0], sdict[key][1]])


    slist.sort(key=lambda x: x[1], reverse=True)

    return slist


def get_string_by_shopping_list(slist):
    """
    Формирует string из общего списка shopping list
    """

    response_content = ''
    for item in slist:
        response_content += f'{item[0]}: {item[1]} {item[2]}\n'

    return response_content
