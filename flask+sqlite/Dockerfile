# Используем легковесный базовый образ
FROM python:3.11-alpine

# Устанавливаем зависимости
RUN apk add --no-cache gcc musl-dev

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем файлы проекта
COPY . .

# Создаем пользователя flaskuser и меняем владельца директории /app на flaskuser
RUN adduser -D flaskuser && chown -R flaskuser:flaskuser /app

# Устанавливаем зависимости из requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Даем права flaskuser на рабочую директорию
USER flaskuser

# Очищаем кеш
RUN pip cache purge

# Инициализация миграций
RUN flask db init
RUN flask db migrate
RUN flask db upgrade

# Экспонируем порт
EXPOSE 5000

# Запускаем приложение
CMD ["flask", "run", "--host=0.0.0.0"]