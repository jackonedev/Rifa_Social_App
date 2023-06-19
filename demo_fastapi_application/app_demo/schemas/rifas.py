from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class Rifa(BaseModel):
    id: int
    cliente: str
    telefono: str
    fecha_inscripcion: datetime
    lugar_inscripcion: str