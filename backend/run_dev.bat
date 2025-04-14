@echo off

REM === Активация venv ===
call .venv\Scripts\activate

REM === Установка переменных окружения ===
set PYTHONPATH=src
set ENV=dev

REM === Запуск uvicorn ===
uvicorn app.main:app --reload --port 8000 --host 0.0.0.0
