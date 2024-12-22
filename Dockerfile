# Använd en officiell Python-bild som bas
FROM python:3.10-slim

# Sätt arbetskatalogen i containern
WORKDIR /app

# Kopiera aktuell katalogs innehåll till /app i containern
COPY . /app

# Installera Python-beroenden (om en requirements.txt finns)
#RUN pip install --no-cache-dir -r requirements.txt

# Starta programmet
CMD ["python", "app.py"]
