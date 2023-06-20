from pydantic import BaseModel, HttpUrl
from typing import Optional
from datetime import datetime


class PremioBase(BaseModel):
    nombre: str
    descripcion: str
    precio: int
    descuento: int
    cantidad: int

class PremioCreate(PremioBase):
    auspiciante: Optional[str] = None
    imagen: Optional[str] = None
    imagen_url: Optional[str] = None


class Premio(PremioBase):
    id: int
    auspiciante: Optional[str] = None
    imagen: Optional[str] = None
    imagen_url: Optional[HttpUrl] = None
    fecha_registro: datetime

    class Config:
        orm_mode = True


