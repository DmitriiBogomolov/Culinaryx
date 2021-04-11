FROM python:3.8.5

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .

RUN python manage.py collectstatic
RUN python manage.py makemigrations
RUN python manage.py migrate

CMD gunicorn foodgram.wsgi:application --bind 0.0.0.0:8000