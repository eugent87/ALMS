# Dockerfile для микросервиса contact

# Используем базовый образ Python
FROM python:3.9

# Установка зависимостей
WORKDIR /app
COPY ./contact/requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

# Копирование исходного кода микросервиса
COPY ./contact /app

# Команда для запуска микросервиса (вы можете настроить это в зависимости от ваших потребностей)
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
