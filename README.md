# TaskFlow

Веб-приложение для управления задачами и командной работы.

## Описание

TaskFlow — учебный проект, разрабатываемый в рамках лабораторных работ по дисциплине «Методы и средства проектирования информационных систем».

Текущая версия: **0.0.1**

Статус разработки: разработка продолжается.

## Технологии

- Python 3.15
- FastAPI 0.115.12
- Uvicorn 0.34.2
- Jinja2 3.1.6
- Docker

## Запуск через Docker

Скачайте образ:

```bash
docker pull danildol/taskflow:0.0.1
```

Запустите контейнер:

```bash
docker run --rm -p 8080:8080 danildol/taskflow:0.0.1
```

Откройте приложение в браузере:

http://localhost:8080

Чтобы остановить приложение, нажмите `Ctrl+C` в терминале.

## Сборка образа самостоятельно

Клонируйте репозиторий:

```bash
git clone https://github.com/usnaems/TaskFlow.git
cd TaskFlow
```

Соберите образ:

```bash
docker build -t taskflow:0.0.1 .
```

Запустите контейнер:

```bash
docker run --rm -p 8080:8080 taskflow:0.0.1
```

## Поддерживаемые архитектуры

Опубликованный Docker-образ поддерживает:

- `linux/amd64` — компьютеры с процессорами Intel и AMD.
- `linux/arm64` — компьютеры с ARM-процессорами, включая Apple Silicon.

## Ссылки

- GitHub: https://github.com/usnaems/TaskFlow
- Docker Hub: https://hub.docker.com/r/danildol/taskflow
