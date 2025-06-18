#manero asíncrona
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.orm import declarative_base
from sqlalchemy.pool import NullPool  # Opcional para ciertos casos
import os
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

# Configuración de la conexión (usa una sola llamada a os.getenv)
DATABASE_URL = ("mysql+asyncmy://root:BuYGMrZkhEixlhvpehSraSzScbYJNNLY@maglev.proxy.rlwy.net:17631/railway")

# Configuración del motor (echo solo en desarrollo)
engine = create_async_engine(
    DATABASE_URL,
    echo=True if os.getenv("ENV") == "dev" else False,  # Desactiva en producción
    poolclass=NullPool  # Opcional: útil para evitar problemas con conexiones persistentes
)

# Sesión asíncrona
AsyncSessionLocal = async_sessionmaker(
    engine,
    expire_on_commit=False,
    class_=AsyncSession
)

# Base para modelos
Base = declarative_base()

# Dependency para FastAPI (mejorada con manejo de errores)
async def get_db():
    async with AsyncSessionLocal() as session:
        try:
            yield session
        finally:
            await session.close()  # Cierra la sesión explícitamente