from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class Cliente(BaseModel):
    id: int
    nombre_apellido: str
    telefono: str
    cumple: str
    fecha_registro: datetime