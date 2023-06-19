from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class Premio(BaseModel):
    id: int
    nombre: str
    descripcion: str
    precio_dcto: str
    fecha_ingreso: datetime
    auspiciante: Optional[str] = None
    imagen: Optional[str] = None


