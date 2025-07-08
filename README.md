# 📝 Todo API mit FastAPI + HTML Frontend

Ein einfaches Fullstack-Projekt mit **FastAPI** als Backend-Framework und einer statischen **HTML/JavaScript-Seite** als Frontend. Die Anwendung erlaubt das Erstellen, Anzeigen und Löschen von Todos über eine REST API – ideal zum Lernen und Erweitern.

---

## 📦 Inhalt

- Python Backend mit FastAPI
- HTML + JavaScript Frontend
- REST API (GET, POST, DELETE)
- Docker Container
- Swagger API-Dokumentation (`/docs`)

---

## 🚀 Schnellstart

### 🔧 Voraussetzungen

- [Docker](https://www.docker.com/)
- oder lokal: `Python 3.10+` + `pip`

---

### 🐳 Mit Docker starten

```bash
# Build Image
docker build -t todo-api .

# Container starten
docker run -p 8000:8000 todo-api
