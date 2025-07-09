FROM python:3.11-slim

# Installer bash
RUN apt-get update && apt-get install -y bash && rm -rf /var/lib/apt/lists/*

# Définir le répertoire de travail
WORKDIR /app

# Copier le projet
COPY . /app

# Installer les dépendances globalement dans l’image
RUN pip install --upgrade pip && pip install -r requirements.txt

# Exposer le port
EXPOSE 8000

# Lancer le serveur Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
