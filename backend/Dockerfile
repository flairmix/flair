# FROM ghcr.io/astral-sh/uv:python3.12-bookworm-slim AS builder

# WORKDIR /app

# # Сначала только зависимости (для кеша)
# COPY pyproject.toml uv.lock* requirements.txt* ./

# # Устанавливаем системные пакеты и зависимости Python
# RUN apt-get update && apt-get install -y --no-install-recommends \
#     build-essential gcc g++ gfortran \
#     libopenblas-dev liblapack-dev \
#     python3-dev curl pkg-config libssl-dev \
#     && rm -rf /var/lib/apt/lists/* \
#     && uv pip install --system --no-cache --requirement requirements.txt

# # Теперь копируем только исходный код
# COPY . .

# CMD ["uvicorn", "src.app.main:app", "--host", "0.0.0.0", "--port", "8000"]


# Базовый образ
FROM ghcr.io/astral-sh/uv:python3.12-bookworm-slim AS base

# Этап 1: Системные зависимости
FROM base AS system-deps
WORKDIR /app

# Устанавливаем только системные зависимости в отдельный слой
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        build-essential \
        gcc \
        g++ \
        gfortran \
        libopenblas-dev \
        liblapack-dev \
        python3-dev \
        curl \
        pkg-config \
        libssl-dev && \
    rm -rf /var/lib/apt/lists/*


# Этап 2: Python зависимости
FROM system-deps AS python-deps
WORKDIR /app

# Копируем только файлы зависимостей
COPY pyproject.toml uv.lock* requirements.txt* ./

# Устанавливаем Python пакеты в отдельный слой
RUN uv pip install --system --no-cache --requirement requirements.txt

# Этап 3: Копирование кода
FROM python-deps AS code-stage
WORKDIR /app

# Копируем исходный код
COPY . .


# Финальный этап
FROM code-stage

# Устанавливаем исполняемые файлы в PATH
ENV PATH="/usr/local/bin:${PATH}"

CMD ["uvicorn", "src.app.main:app", "--host", "0.0.0.0", "--port", "8000"]