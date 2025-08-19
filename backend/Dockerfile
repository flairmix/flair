FROM ghcr.io/astral-sh/uv:python3.12-bookworm-slim AS builder

WORKDIR /app

# Сначала только зависимости (для кеша)
COPY pyproject.toml uv.lock* requirements.txt* ./

# Устанавливаем системные пакеты и зависимости Python
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential gcc g++ gfortran \
    libopenblas-dev liblapack-dev \
    python3-dev curl pkg-config libssl-dev \
    && rm -rf /var/lib/apt/lists/* \
    && uv pip install --system --no-cache --requirement requirements.txt

# Теперь копируем только исходный код
COPY . .

CMD ["uvicorn", "src.app.main:app", "--host", "0.0.0.0", "--port", "8000"]