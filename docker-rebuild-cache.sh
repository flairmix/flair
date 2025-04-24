#!/bin/bash
set -e

# Пересборка образов с использованием кэша и запуск контейнеров
docker compose build
docker compose up --force-recreate --no-deps -d