from contextlib import asynccontextmanager
from pathlib import Path
from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates

from app.database import Base, engine, SessionLocal
from app import models

BASE_DIR = Path(__file__).resolve().parent

templates = Jinja2Templates(directory=str(BASE_DIR / "templates"))


@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine)
    yield


app = FastAPI(
    title="TaskFlow",
    version="0.0.3",
    lifespan=lifespan
)


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "product_name": "TaskFlow",
            "version": app.version
        },
    )


@app.get("/tasks", response_class=HTMLResponse)
def tasks_page(request: Request):
    with SessionLocal() as db:
        tasks = db.query(models.Task).order_by(models.Task.id).all()

    return templates.TemplateResponse(
        request=request,
        name="tasks.html",
        context={"tasks": tasks},
    )


@app.get("/tasks/new", response_class=HTMLResponse)
async def new_task_page(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="task_new.html",
        context={"error": None},
    )


@app.post("/tasks/new", response_class=HTMLResponse)
def create_task(
    request: Request,
    title: str = Form(...),
    description: str = Form("")
):
    title = title.strip()

    if not title:
        return templates.TemplateResponse(
            request=request,
            name="access_denied.html",
            context={"reason": "Нельзя создать задачу без названия."},
            status_code=400,
        )

    with SessionLocal() as db:
        task = models.Task(
            title=title,
            description=description.strip()
        )

        db.add(task)
        db.commit()

    return RedirectResponse(url="/tasks", status_code=303)


@app.get("/access-denied", response_class=HTMLResponse)
async def access_denied(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="access_denied.html",
        context={
            "reason": "Доступ к действию отклонён из-за некорректных данных."
        },
        status_code=400,
    )