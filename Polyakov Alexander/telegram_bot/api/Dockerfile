FROM python:3.9

WORKDIR /usr/src/app

# Устанавливаем зависимости
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Копируем исходный код в контейнер
COPY . .

# Запускаем приложение
CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:app"]
