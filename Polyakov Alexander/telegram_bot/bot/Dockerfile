# Базовый образ
FROM python:3.9

WORKDIR /usr/src/bot

# Файлы зависимостей и установка
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Копирование кода внутрь контейнера
COPY . .

# Запуск
CMD ["python", "./main.py"]
