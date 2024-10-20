# Використовуємо базовий образ Python 3.9
FROM python:3.9-slim

# Встановлюємо робочу директорію всередині контейнера
WORKDIR /app

# Копіюємо файл залежностей в контейнер
COPY requirements.txt ./

# Встановлюємо залежності
RUN pip install --no-cache-dir -r requirements.txt

# Копіюємо весь код з папки app
COPY . .

# Указуємо команду для запуску Uvicorn сервера
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
