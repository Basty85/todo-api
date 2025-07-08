from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from app.models import todos
from app.schemas import Todo  # dein Pydantic Modell
from app.db import database, engine, metadata
from sqlalchemy import select

app = FastAPI()

# CORS Middleware (für lokale Entwicklung "allow_origins=['*']")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"],
)

templates = Jinja2Templates(directory="app/templates")

# Tabelle erstellen, falls noch nicht existiert
metadata.create_all(engine)

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

@app.get("/", response_class=HTMLResponse)
async def serve_index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/todos")
async def get_todos():
    query = select(todos)
    result = await database.fetch_all(query)
    # Ergebnis in Pydantic-Modelle umwandeln oder direkt zurückgeben (dicts)
    return [dict(r) for r in result]

@app.post("/todos")
async def add_todo(todo: Todo):
    query = todos.insert().values(id=todo.id, title=todo.title, done=todo.done)
    await database.execute(query)
    return todo

@app.delete("/todos/{todo_id}")
async def delete_todo(todo_id: int):
    query = todos.delete().where(todos.c.id == todo_id)
    result = await database.execute(query)
    if result:
        return {"message": "Deleted"}
    raise HTTPException(status_code=404, detail="Todo not found")