# Этап 1: Сборка зависимостей
FROM python:3.11-alpine as builder

# Устанавливаем зависимости для сборки
RUN apk add --no-cache gcc musl-dev libffi-dev

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем файл зависимостей
COPY requirements.txt .

# Устанавливаем зависимости в изолированное место
RUN pip install --no-cache-dir --prefix=/install -r requirements.txt

# Этап 2: Финальный легковесный образ
FROM python:3.11-alpine

# Устанавливаем минимальные системные зависимости
RUN apk add --no-cache libffi

# Создаем непривилегированного пользователя
RUN adduser -D flaskuser

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем установленные зависимости из этапа сборки
COPY --from=builder /install /usr/local

# Копируем весь проект в контейнер
COPY . .

# Меняем владельца рабочей директории
RUN chown -R flaskuser:flaskuser /app

# Устанавливаем пользователя по умолчанию
USER flaskuser

# Экспонируем порт
EXPOSE 5000

# Выполняем автоматические миграции при запуске
CMD ["sh", "-c", "flask db upgrade && flask run --host=0.0.0.0"]
