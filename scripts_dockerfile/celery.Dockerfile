FROM python:3.11-slim

WORKDIR /app

# Instala dependências
COPY requirements.txt .


RUN pip install --no-cache-dir -r requirements.txt

# Copia o resto do código
COPY . .

# O comando padrão será sobrescrito pelo docker-compose