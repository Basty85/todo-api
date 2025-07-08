# Basis-Image mit Python
FROM python:3.10-slim

# Setze das Arbeitsverzeichnis
WORKDIR /app

# Kopiere requirements und installiere
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN apt-get update && apt-get install -y sqlite3

# Kopiere den Code
COPY ./app ./app

# Exponiere Port (für Doku)
EXPOSE 8000

# Starte den Server
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]