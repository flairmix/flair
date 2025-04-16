FROM python:3.13-slim
# Установка uv
RUN pip install --no-cache-dir uv

WORKDIR /app
COPY . .

# Копируем только pyproject.toml для установки зависимостей
# COPY pyproject.toml ./
RUN cat pyproject.toml

# Установка из [project.dependencies]
RUN uv pip install --system --group default

# Копируем оставшиеся файлы проекта

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--app-dir", "src"]
