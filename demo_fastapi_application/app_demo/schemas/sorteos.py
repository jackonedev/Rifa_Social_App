from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime
from . import users


class SorteoBase(BaseModel):
    owner: users.UserOut
    rifas_id: List[int]
    premios_id: List[int]

class SorteoCreate(SorteoBase):
    pass

class SorteoOut(SorteoBase):
    id: int
    fecha_registro: datetime

    class Config:
        orm_mode = True

class SorteoUpdate(BaseModel):
    lugar_sorteo: str
    auspciante: str
    contacto: str

class SorteoRealizado(BaseModel):
    id: int
    fecha_registro: datetime
    lugar_sorteo: str
    auspciante: str
    contacto: str
    ganadores: List[tuple]

    class Config:
        orm_mode = True