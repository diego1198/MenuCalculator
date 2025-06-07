# Sistema de Menú y Pedidos

Un sistema web simple para gestionar un menú y realizar pedidos, con la capacidad de guardar el historial de ventas.

## Características

- Interfaz moderna y responsive
- Selección fácil de platos del menú
- Cálculo automático del total
- Historial de ventas con filtrado por fecha
- Base de datos local SQLite
- Panel de administración para gestionar productos

## Requisitos

- Python 3.8 o superior
- pip (gestor de paquetes de Python)

## Instalación Local

1. Clonar el repositorio:
```bash
git clone <url-del-repositorio>
cd <nombre-del-directorio>
```

2. Crear un entorno virtual (opcional pero recomendado):
```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

3. Instalar las dependencias:
```bash
pip install -r requirements.txt
```

4. Inicializar la base de datos:
```bash
python init_db.py
```

5. Iniciar el servidor:
```bash
python app.py
```

6. Abrir el navegador y acceder a:
```
http://localhost:4036
```

## Despliegue en Render.com

1. Crear una cuenta en [Render.com](https://render.com)

2. Crear un nuevo Web Service:
   - Conectar con tu repositorio de GitHub
   - Configurar el servicio:
     - Name: `menu-app` (o el nombre que prefieras)
     - Environment: `Python 3`
     - Build Command: `pip install -r requirements.txt`
     - Start Command: `gunicorn app:app`
     - Plan: Free

3. Configurar variables de entorno:
   - PYTHON_VERSION=3.9.0

4. Desplegar y esperar a que el servicio esté activo

5. Inicializar la base de datos (opcional):
   - Usar el panel de administración para agregar productos
   - O ejecutar el script de inicialización si es necesario

## Estructura del Proyecto

- `app.py`: Aplicación principal Flask
- `init_db.py`: Script para inicializar la base de datos localmente
- `init_deploy.py`: Script para inicializar la base de datos en producción
- `gunicorn.conf.py`: Configuración de Gunicorn para producción
- `Procfile`: Archivo de configuración para Render
- `templates/`: Directorio con las plantillas HTML
- `menu.db`: Base de datos SQLite (se crea automáticamente)

## Contribuir

Las contribuciones son bienvenidas. Por favor, abre un issue para discutir los cambios propuestos.

## Licencia

Este proyecto está bajo la Licencia MIT. 