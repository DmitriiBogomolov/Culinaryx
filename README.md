# Продуктовый помошник на Django.

Приложение, где пользователи могут:
- создавать и заполнять профили;
- подписываться друг на друга;
- публиковать, комментировать, оценивать, кулинарные рецепты;
- формировать и скачивать персональные списки продуктов для приготовления понравившихся блюд;
- получать доступ к функциональности приложения в зависимости от установленных прав доступа.

## Установка

Склонировать репозиторий, разместить .env в директории с проектом.

```python
DB_ENGINE=********
DB_NAME=********
POSTGRES_USER=********
POSTGRES_PASSWORD=********
DB_HOST=********
DB_PORT=********
SECRET_KEY=********
SERVER_IP=********
SERVER_DOMAIN_NAME=********
EMAIL_HOST_USER=********
EMAIL_HOST_PASSWORD=******** 
EMAIL_PORT=********
EMAIL_HOST=********
EMAIL_BACKEND=********
```

Запустить docker-compose

```bash
docker-compose build
docker-compose up
```

## Технологии

1. Django
2. PostgreSQL
3. Docker
4. Nginx, Gunicorn
4. GitHub Actions

## Лицензия
[MIT](https://choosealicense.com/licenses/mit/)

