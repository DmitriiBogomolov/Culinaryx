# Продуктовый помощник

Cайт, на котором пользователи могут публиковать рецепты, добавлять чужие рецепты в избранное и подписываться на публикации других авторов. Сервис «Список покупок» позволяет пользователям создавать список продуктов, которые нужно купить для приготовления выбранных блюд.

http://www.yatubetest.ml/

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

## Инструментарий

1. Django
2. Docker
3. GitHub Actions

## Лицензия
[MIT](https://choosealicense.com/licenses/mit/)

## Статус workflow

![foodgram](https://github.com/dmitriibogomolov/foodgram-project/workflows/foodgram%20workflow/badge.svg?branch=master)
