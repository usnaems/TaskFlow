
import json
from pathlib import Path

from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates

app = FastAPI(title="TaskFlow", version="0.0.2")

BASE_DIR = Path(__file__).resolve().parent
DATA_FILE = BASE_DIR / "data" / "tasks.json"

templates = Jinja2Templates(directory=str(BASE_DIR / "templates"))


def read_tasks():
    with open(DATA_FILE, "r", encoding="utf-8") as file:
        return json.load(file)


def save_tasks(tasks):
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(tasks, file, ensure_ascii=False, indent=4)


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={"product_name": "TaskFlow", "version": app.version},
    )


@app.get("/tasks", response_class=HTMLResponse)
async def tasks_page(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="tasks.html",
        context={"tasks": read_tasks()},
    )


@app.get("/tasks/new", response_class=HTMLResponse)
async def new_task_page(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="task_new.html",
        context={"error": None},
    )


@app.post("/tasks/new", response_class=HTMLResponse)
async def create_task(request: Request, title: str = Form(...), description: str = Form("")):
    title = title.strip()

    if not title:
        return templates.TemplateResponse(
            request=request,
            name="access_denied.html",
            context={"reason": "Нельзя создать задачу без названия."},
            status_code=400,
        )

    tasks = read_tasks()
    next_id = max((task["id"] for task in tasks), default=0) + 1

    tasks.append({
        "id": next_id,
        "title": title,
        "description": description.strip(),
    })
    save_tasks(tasks)

    return RedirectResponse(url="/tasks", status_code=303)


@app.get("/access-denied", response_class=HTMLResponse)
async def access_denied(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="access_denied.html",
        context={"reason": "Доступ к действию отклонён из-за некорректных данных."},
        status_code=400,
    )
