from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class ClienteBase(BaseModel):
    nombre: str
    apellido: Optional[str]
    telefono: str
    fecha_cumple: Optional[datetime] = None


class ClienteCreate(ClienteBase):
    pass

class ClienteUpdate(BaseModel):
    nombre: Optional[str]
    apellido: Optional[str]
    telefono: Optional[str]
    fecha_cumple: Optional[datetime] = None

class Cliente(ClienteBase):
    id: int
    fecha_registro: datetime

    class Config:
        orm_mode = True
