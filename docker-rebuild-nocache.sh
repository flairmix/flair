#!/bin/bash
set -e

docker compose down --volumes

# unused images clean
docker system prune -f

# Очистка build cache Docker
docker builder prune -f

# Пересборка образов без использования кэша и запуск контейнеров
docker compose build --no-cache
docker compose up --force-recreate --no-deps -d