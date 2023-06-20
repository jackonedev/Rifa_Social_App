from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from typing import List, Optional

from sqlalchemy import func
# from sqlalchemy.sql.functions import func
from ..database import models
from ..schemas.premios import Premio, PremioCreate
from ..database.database import get_db


router = APIRouter(
    prefix="/v1/premios",
    tags=['Premios']
)


@router.get("/", response_model=List[Premio])
def get_premios(db: Session = Depends(get_db), skip: int = 0, limit: int = 100, search: Optional[str] = ""):
    premios = db.query(models.Premio).offset(skip).limit(limit).all()
    return premios


@router.get("/{premio_id}", response_model=Premio)
def get_premio(premio_id: int, db: Session = Depends(get_db)):
    premio = db.query(models.Premio).filter(models.Premio.id == premio_id).first()
    if not premio:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Premio {premio_id} no encontrado")
    return premio


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=Premio)
def create_premio(premio_nuevo: PremioCreate, db: Session = Depends(get_db)):

    # premio_nuevo_dict = premio_nuevo.dict()
    # premios = db.query(models.Premio).all()
    # for premio in premios:
    #     if premio.nombre == premio_nuevo.nombre:
    #         raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Premio {premio_nuevo.nombre} ya existe")
    # print(premio_nuevo.dict())
    # return {"nuevo_premio": f"Se creo el premio {premio_nuevo.nombre}, precio {premio_nuevo.precio_dcto}, fecha {premio_nuevo.fecha_ingreso}"}
    pass

@router.put("/{premio_id}")
def update_premio(premio_id: int):
    return {"message": f"Premio {premio_id} actualizado"}


@router.delete("/{premio_id}")
def delete_premio(premio_id: int):
    return {"message": f"Premio {premio_id} eliminado"}









