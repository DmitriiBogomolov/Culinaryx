from .models import Ingridient
from django.http import JsonResponse
from django.http import HttpResponse


"""
Получает из GET параметра начало названия ингридиента
и предоставляет все совпадения
"""
def get_ingrediends_dict_view(request):
    query = request.GET.get("query", "")

    if not query:
        return HttpResponse('none')

    ingridients = Ingridient.objects.filter(
                        name__startswith=query
                                             ).order_by('name').values()

    ingridients_list = list(ingridients)

    return JsonResponse(ingridients_list, safe=False)
