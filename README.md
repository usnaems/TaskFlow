# TaskFlow

TaskFlow — веб-приложение для управления задачами и совместной работы команды.

## Версия

**0.0.3**

## Технологии

- Python 3.15
- FastAPI
- Uvicorn
- Jinja2
- SQLAlchemy
- PostgreSQL 18
- Docker
- Docker Compose

## Архитектура

Приложение состоит из двух Docker-сервисов:

- **app** — веб-приложение на FastAPI.
- **db** — база данных PostgreSQL 18.

Данные задач хранятся в PostgreSQL. Для постоянного хранения используется именованный Docker volume `dbdata`. При запуске приложения таблицы базы данных создаются автоматически.

## Запуск

Репозиторий: https://github.com/usnaems/TaskFlow

Ветка: `lab3`

Pull Request: https://github.com/usnaems/TaskFlow/pull/2

Docker-образ: `danildol/taskflow:0.0.3`

Страница образа: https://hub.docker.com/r/danildol/taskflow

Клонирование репозитория:

```bash
git clone -b lab3 https://github.com/usnaems/TaskFlow
cd TaskFlow
```

Запуск приложения и базы данных:

```bash
docker compose up -d
```

После запуска приложение доступно по адресу:

http://localhost:8080

Проверить состояние контейнеров можно командой:

```bash
docker compose ps
```

Остановка контейнеров:

```bash
docker compose down
```

Данные PostgreSQL сохраняются в Docker volume `dbdata` и не удаляются при обычной остановке контейнеров. Для удаления данных вместе с томом используется команда `docker compose down -v`.

## Основные функции

- Просмотр списка задач.
- Создание новых задач.
- Обработка некорректных запросов.
- Постоянное хранение данных в PostgreSQL.
