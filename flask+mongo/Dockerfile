# Этап 1: Сборка зависимостей
FROM python:3.10-alpine as builder

# Устанавливаем зависимости для сборки
RUN apk add --no-cache --update build-base libffi-dev gcc

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем только файл с зависимостями
COPY requirements.txt .

# Устанавливаем зависимости в изолированное место
RUN pip install --no-cache-dir --prefix=/install -r requirements.txt


# Этап 2: Финальный легковесный образ
FROM python:3.10-alpine

# Указываем непривилегированного пользователя
ENV USER=appuser

# Добавляем минимальные системные зависимости
RUN apk add --no-cache libffi \
    && adduser --disabled-password --gecos "" $USER

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем собранные зависимости из первого этапа
COPY --from=builder /install /usr/local

# Копируем исходный код
COPY . .

# Меняем владельца файлов
RUN chown -R $USER:$USER /app

# Запускаем контейнер от непривилегированного пользователя
USER $USER

# Указываем порт для Flask
EXPOSE 5000

# Команда запуска
CMD ["sh", "-c", "python init_db.py && flask run --host=0.0.0.0"]
