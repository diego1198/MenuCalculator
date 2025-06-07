#!/usr/bin/env bash
# exit on error
set -o errexit

# Instalar dependencias
pip install -r requirements.txt

# Inicializar la base de datos
python init_deploy.py

# Iniciar la aplicación
gunicorn app:app 