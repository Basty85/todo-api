from app.models import Todo
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi import Request

app = FastAPI()

# Erlaube Anfragen von deinem lokalen HTML
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Für Entwicklung: alle Domains erlaubt. Später spezifisch machen!
    allow_credentials=True,
    allow_methods=["*"],  # Erlaube POST, GET, DELETE usw.
    allow_headers=["*"],
)

templates = Jinja2Templates(directory="app/templates")

todos = []

@app.get("/", response_class=HTMLResponse)
async def serve_index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/todos")
def get_todos():
    return todos

@app.post("/todos")
def add_todo(todo: Todo):
    todos.append(todo)
    return todo

@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int):
    for i, todo in enumerate(todos):
        if todo.id == todo_id:
            del todos[i]
            return {"message": "Deleted"}
    raise HTTPException(status_code=404, detail="Todo not found")