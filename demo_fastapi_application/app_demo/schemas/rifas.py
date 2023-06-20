from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class RifaBase(BaseModel):
    jugador: str
    telefono: str

class RifaCreate(RifaBase):
    fecha_cumple: Optional[datetime] = None
    lugar_registro: Optional[str]

class RifaUpdate(BaseModel):
    jugador: Optional[str]
    telefono: Optional[str]
    fecha_cumple: Optional[datetime] = None
    lugar_registro: Optional[str]

class Rifa(RifaBase):
    id: int
    fecha_cumple: Optional[datetime] = None
    lugar_registro: Optional[str]
    fecha_registro: datetime

    class Config:
        orm_mode = True