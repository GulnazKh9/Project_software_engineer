FROM python:3.10-slim

WORKDIR /app

# Копирование исходного кода
COPY creature.py .

# Точка входа
CMD ["python", "creature.py"]