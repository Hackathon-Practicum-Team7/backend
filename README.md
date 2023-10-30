## Внутренний сервис найма в карьерном трекере

https://seventeam-hakaton.sytes.net/

### Описание проекта
Цель сервиса - предоставить возможность партнерам работать с базой заинтересованных кандидатов и отбирать не только текущих студентов, но и выпускников уровня middle и выше

### Технологии
- Python 3.9
- Django 4.1
- Django REST framework 3.14
- Postgresql
- Djoser 2.2
- [Pandas](https://pandas.pydata.org/docs/)
- [drf-spectacular](https://drf-spectacular.readthedocs.io/en/latest/)
- Gunicorn 21.2
- Nginx
- Docker

### API-документация:
https://seventeam-hakaton.sytes.net/api/schema/swagger/

### Запуск проекта

1. Склонировать репозиторий:
```
git clone git@github.com:Hackathon-Practicum-Team7/backend.git
```
2. Перейти папку с проектом:
```
cd backend
```
3. В директории /backend создать файл .env с таким содержанием:
```
DB_ENGINE=django.db.backends.postgresql
POSTGRES_DB=hakaton
POSTGRES_USER=user
POSTGRES_PASSWORD=yourpassword
DB_HOST=db
DB_PORT=5432
```
4. Запуск контейнеров:
```
docker compose up -d --build
docker compose exec -it backend python collectstatic --noinput
docker compose exec -it backend python manage.py migrate
```
5. Загрузить фикстуры в бд
```
docker compose exec -it backend python manage.py loaddata fixtures/fixtures.json
```
6. Локально API документация доступна по адресу
http://localhost:8000/api/schema/swagger/

7. Для работы с API проекта, необходимо получить токен:
```
POST http://localhost:8000/api/v1/auth/jwt/create/
content-type: application/json

{
    "email": "recruiter1@example.ru",
    "password": "password123"
}
```
Ответ:
```
{
  "refresh": "<refresh-token>",
  "access": "<access-token>"
}
```
Далее для эндпоинтов, которым требуется авторизация, необходимо передавать токен в заголовках
```
Authorization: JWT <access-token>
```

### Команда backend

- [Сергей Саморуков](https://github.com/bauman1922) (ТГ: https://t.me/bauman1922)
- [Вера Фадеева](https://github.com/verafadeeva) (ТГ: https://t.me/fadeevavera)
