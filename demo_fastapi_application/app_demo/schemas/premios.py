from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from validator import validate_url
from pydantic import validator


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


    @validator('imagen_url')
    def validate_imagen_url(cls, value):
        if not validate_url(value):
            raise ValueError('Invalid imagen_url')
        return value


class Premio(PremioBase):
    id: int
    auspiciante: Optional[str] = None
    imagen: Optional[str] = None
    imagen_url: Optional[str] = None
    fecha_registro: datetime

    class Config:
        orm_mode = True


