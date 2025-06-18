from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from database import Base  # Asegúrate de que tus modelos estén definidos aquí
from routes.alumnos import router as alumnos_router
from routes.login import router as login_router
from routes.profesor import router as profesor_router
from routes.asistencia_api import router as asistencia_router
from routes.generarExcel import router as generar_excel_router
from routes.horarioProfesor import router as horario_profesor_router
from routes.terminal_api import router as terminal_router
from routes.asistencia_profesor import router as asistencia_profesor_router
from fastapi.responses import FileResponse
from pathlib import Path





app = FastAPI()

# Obtener la ruta absoluta a la carpeta "frontend"
BASE_DIR = Path(__file__).resolve().parent
FRONTEND_DIR = BASE_DIR.parent / "frontend"

# Configuración CORS (ajusta según tus necesidades)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # En producción, reemplaza con tus dominios
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Incluir routers
app.include_router(alumnos_router, prefix="/api")
app.include_router(login_router)
app.include_router(profesor_router)
app.include_router(asistencia_router)
app.include_router(generar_excel_router)
app.include_router(horario_profesor_router)
app.include_router(terminal_router)
app.include_router(asistencia_profesor_router)


@app.get("/")
async def root():
    return {"message": "Sistema de Asistencia RFID con MySQL"}