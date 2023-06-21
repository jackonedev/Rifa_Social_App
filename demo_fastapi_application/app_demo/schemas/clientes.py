from pydantic import BaseModel, EmailStr, constr
from typing import Optional
from datetime import datetime
import re

class ClienteBase(BaseModel):
    nombre: str
    apellido: Optional[str]
    telefono: constr(regex=re.compile(r'^\+?\d{0,3}\d{0,5}-?\d{0,10}$'))
    email: Optional[EmailStr]
    fecha_cumple: Optional[str] = None


class ClienteCreate(ClienteBase):
    pass

class ClienteUpdate(BaseModel):
    nombre: Optional[str]
    apellido: Optional[str]
    telefono: Optional[constr(regex=re.compile(r'^\+?\d{0,3}\d{0,5}-?\d{0,10}$'))]
    fecha_cumple: Optional[str] = None
    email: Optional[EmailStr] = None

class Cliente(ClienteBase):
    id: int
    fecha_registro: datetime

    class Config:
        orm_mode = True
