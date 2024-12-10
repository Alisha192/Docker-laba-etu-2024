# Используем легковесный образ Python на базе Alpine
FROM python:3.10-alpine

# Указываем переменную окружения для непривилегированного запуска
ENV USER=appuser

# Добавляем системные зависимости
RUN apk add --no-cache --update build-base libffi-dev gcc \
    && pip install --upgrade pip \
    && adduser --disabled-password --gecos "" $USER

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем только файлы для установки зависимостей
COPY requirements.txt .

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Устанавливаем права и копируем исходный код
COPY . .

# Меняем владельца файлов
RUN chown -R $USER:$USER /app

# Запускаем контейнер от непривилегированного пользователя
USER $USER

# Указываем порт для Flask
EXPOSE 5000

# Команда запуска
CMD ["sh", "-c", "python init_db.py && flask run --host=0.0.0.0"]