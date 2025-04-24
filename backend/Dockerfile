FROM ghcr.io/astral-sh/uv:python3.12-bookworm-slim

WORKDIR /app

#ENV UV_COMPILE_BYTECODE=1
#ENV UV_LINK_MODE=copy
#ENV PATH="/app/.venv/bin:$PATH"

RUN apt-get update && apt-get install -y \
    build-essential gcc g++ gfortran \
    libopenblas-dev liblapack-dev \
    python3-dev curl pkg-config libssl-dev \
    && rm -rf /var/lib/apt/lists/*

COPY . .

#COPY src/ src/
#COPY pyproject.toml uv.lock ./

#RUN --mount=type=cache,target=/root/.cache/uv \
#    uv sync --frozen --no-dev

RUN pip install --no-cache-dir -r requirements.txt

CMD ["uvicorn", "src.app.main:app", "--host", "0.0.0.0", "--port", "8000"]