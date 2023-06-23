from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime
from . import users


class SorteoBase(BaseModel):
    id: int
    owner: users.UserOut

class SorteoCreate(SorteoBase):
    rifas: List[int]
    premios: List[int]

class SorteoOut(SorteoBase):
    rifas: List[int]
    premios: List[int]
    fecha_registro: datetime

    class Config:
        orm_mode = True
