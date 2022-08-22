# Продуктовый помощник.

Приложение позволяет пользователям публиковать кулинарные рецепты, подписываться друг на друга и общаться. Кроме того - формировать персональные списки продуктов (покупок), необходимых для приготовления выбранных блюд.

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

## Статус workflow

![foodgram](https://github.com/dmitriibogomolov/foodgram-project/workflows/foodgram%20workflow/badge.svg?branch=master)
