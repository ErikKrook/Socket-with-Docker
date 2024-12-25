# Använd en officiell Python-bild som bas
FROM python:3.10-slim

# Sätt arbetskatalogen i containern
WORKDIR /app

# Kopiera aktuell katalogs innehåll till /app i containern
COPY . .

# Starta programmet
CMD ["python", "socket_server.py"]
