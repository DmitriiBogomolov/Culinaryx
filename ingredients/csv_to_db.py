

from dictionaries.models import Unit, Ingridient


"""
Скрипт django shell для заполнения БД ингридиентами
"""
for line in open("ingredients.csv", encoding="utf-8"):
    lst = line.replace("\n","").split(",")

    unit = Unit.objects.get_or_create(name=lst[1])[0]

    try:
        Ingridient.objects.create(name=lst[0], unit=unit)
    except:
        pass

    print(lst)
