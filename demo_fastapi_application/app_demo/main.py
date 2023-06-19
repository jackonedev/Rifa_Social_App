from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from typing import Optional
from datetime import datetime
#https://youtu.be/ToXOb-lpipM?t=4959


class Premio(BaseModel):
    id: int
    nombre: str
    descripcion: str
    precio_dcto: str
    fecha_ingreso: datetime
    auspiciante: Optional[str] = None
    imagen: Optional[str] = None


class Cliente(BaseModel):
    id: int
    nombre_apellido: str
    telefono: str
    cumple: str
    fecha_registro: datetime

class Rifa(BaseModel):
    id: int
    cliente: str
    telefono: str
    fecha_inscripcion: datetime
    lugar_inscripcion: str

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Hello World"}








## CRUD PREMIOS ##
premios = [{"id": 1, "nombre": "Ganaste una Picada", "descripcion": "Promo de picada p/2 con birra ", "precio_dcto": "$3000", "fecha_ingreso": "2021-01-01", "auspiciante": "La Despensa", "imagen": "Imagen 1"},
           {"id": 2, "nombre": "Descuento en Picada", "descripcion": "Descuento del 25% para comprar una promo de picada para 2 con birra", "precio_dcto": "$3000/25%", "fecha_ingreso": "2021-01-02", "auspiciante": "La despensa"}
              ]
@app.get("/v1/premios")
def get_premios():
    return {"data": premios}
@app.get("/v1/premios/{premio_id}")
def get_premio(premio_id: int):
    return {"message": f"Este es el premio {premio_id}"}
@app.post("/v1/premios", status_code=status.HTTP_201_CREATED)
def create_premio(premio_nuevo: Premio):
    premio_nuevo_dict = premio_nuevo.dict()
    premios.append(premio_nuevo_dict)
    print(premio_nuevo.dict())
    return {"nuevo_premio": f"Se creo el premio {premio_nuevo.nombre}, precio {premio_nuevo.precio_dcto}, fecha {premio_nuevo.fecha_ingreso}"}
@app.put("/v1/premios/{premio_id}")
def update_premio(premio_id: int):
    return {"message": f"Premio {premio_id} actualizado"}
@app.delete("/v1/premios/{premio_id}")
def delete_premio(premio_id: int):
    return {"message": f"Premio {premio_id} eliminado"}
#############     #############     #############     ############








