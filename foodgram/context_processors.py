from django.conf import settings


# Отображает заголовок приложения
def app_title(request):
    return {'APP_TITLE': settings.APP_TITLE}
