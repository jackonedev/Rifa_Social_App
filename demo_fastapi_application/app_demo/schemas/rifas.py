from pydantic import BaseModel, constr
from typing import Optional
from datetime import datetime
import re


class RifaBase(BaseModel):
    jugador: str
    telefono: constr(regex=re.compile(r'^\+?\d{0,3}\d{0,5}-?\d{0,10}$'))

class RifaCreate(RifaBase):
    fecha_cumple: Optional[datetime] = None
    lugar_registro: Optional[str]

class RifaUpdate(BaseModel):
    jugador: Optional[str]
    telefono: Optional[constr(regex=re.compile(r'^\+?\d{0,3}\d{0,5}-?\d{0,10}$'))]
    fecha_cumple: Optional[datetime] = None
    lugar_registro: Optional[str]

class Rifa(RifaBase):
    id: int
    fecha_cumple: Optional[datetime] = None
    lugar_registro: Optional[str]
    fecha_registro: datetime

    class Config:
        orm_mode = True

class RifaOut(BaseModel):
    id: int
    jugador: str
    
    class Config:
        orm_mode = True