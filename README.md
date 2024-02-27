# Product helper

Приложение "продуктовый помошник", где пользователи могут:
- создавать и заполнять профили;
- подписываться друг на друга;
- публиковать, комментировать, оценивать, кулинарные рецепты;
- формировать и скачивать персональные списки продуктов для приготовления понравившихся блюд;
- получать доступ к функциональности приложения в зависимости от установленных прав доступа.

Алгоритм регистрации пользователей:
1. Пользователь отправляет запрос на регистрацию.
2. Приложение отправляет письмо с кодом подтверждения.
3. Пользователь отправляет запрос с кодом подтверждения.
4. При желании пользователь отправляет запрос на изменение данных профиля.

## Как использовать

1. Запустить docker-compose

        docker-compose up --build

2. Остановка:

        docker-compose down -v

## Технологии

1. Django
2. PostgreSQL
3. Docker
4. Gunicorn
5. NGINX
6. GitHub Actions

## Скриншоты

![1](https://github.com/DmitriiBogomolov/product_helper/blob/master/media/refs/1.png)
![2](https://github.com/DmitriiBogomolov/product_helper/blob/master/media/refs/2.png)
![3](https://github.com/DmitriiBogomolov/product_helper/blob/master/media/refs/3.png)
![4](https://github.com/DmitriiBogomolov/product_helper/blob/master/media/refs/4.png)

## Лицензия
[MIT](https://choosealicense.com/licenses/mit/)
