# Proyecto FastAPI - Backend ERP

Este proyecto es el backend del sistema ERP desarrollado con **FastAPI**. Está diseñado para manejar la gestión de usuarios y otras entidades del sistema empresarial.

## 📁 Estructura del Proyecto

ERP/
└── backend/
├── app/
│ ├── api/
│ │ └── v1/
│ │ ├── crud/
│ │ └── endpoints/
│ ├── database.py
│ ├── models/
│ ├── schemas/
│ ├── util.py
│ └── main.py
├── requirements.txt
└── README.md


## ⚙️ Tecnologías utilizadas

- **Python 3.10+**
- **FastAPI**
- **SQLAlchemy**
- **MySQL / SQL Server** (según configuración)
- **Pydantic**
- **bcrypt**
- **dotenv**
- **uvicorn**

## 🚀 Cómo ejecutar el proyecto

1. Clona el repositorio:

```bash
git clone https://github.com/saranda40/fastapi.git
cd fastapi

python -m venv venv
source venv/bin/activate  # En macOS/Linux
venv\Scripts\activate     # En Windows

pip install -r requirements.txt

DATABASE_URL=mysql+pymysql://usuario:password@localhost/erp

uvicorn app.main:app --reload


uncionalidades actuales
Registro y validación de usuarios

Encriptación de contraseñas

Listado, edición y eliminación de usuarios

Validación contra tablas relacionadas (sexo, región, comuna, etc.)

📌 Organización del código
crud/: Lógica de acceso y operaciones con la base de datos

endpoints/: Rutas disponibles de la API

models/: Modelos SQLAlchemy que representan las tablas

schemas/: Esquemas de entrada/salida (Pydantic)

util.py: Funciones utilitarias (ej. encriptación)

🛡️ Autenticación
Pendiente de implementar: autenticación con JWT o integración con el sistema de usuarios del ERP.

📅 Futuras versiones
/api/v2 con mejoras en seguridad y rendimiento

Registro de auditoría

Autenticación y permisos

Soporte multicliente

👨‍💻 Autor
Desarrollado por Sebastián Aranda
GitHub: @saranda40




