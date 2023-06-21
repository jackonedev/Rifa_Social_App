### schema.premios.py
from typing import Optional
from pydantic import BaseModel, HttpUrl
from datetime import datetime


class PremioBase(BaseModel):
    nombre: str
    cantidad: Optional[int]
    precio: int
    descuento: Optional[int]
    auspiciante: Optional[str]
    descripcion: Optional[str]
    imagen_url: Optional[HttpUrl]

class PremioCreate(PremioBase):
    pass

class PremioUpdate(BaseModel):
    nombre: Optional[str]
    cantidad: Optional[int]
    precio: Optional[int]
    descuento: Optional[int]
    auspiciante: Optional[str]
    descripcion: Optional[str]
    imagen_url: Optional[HttpUrl]

class Premio(PremioBase):
    id: int
    fecha_registro: datetime

    class Config:
        orm_mode = True
