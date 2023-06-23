from fastapi import status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from typing import List, Optional
from datetime import datetime as dt
import random

from ..database import models
from ..schemas.sorteos import SorteoCreate, SorteoOut, SorteoUpdate
from ..schemas.users import UserOut
from ..database.database import get_db
from ..auth.oauth2 import get_current_user


router = APIRouter(
    prefix="/v1/sorteos",
    tags=['Sorteos']
)


# create a post path operation for creating a new sorteo
## FALTA MIGRACION DE DB PARA QUE FUNCIONE O RESETEAR LAS TABLAS
@router.post("/", status_code=status.HTTP_201_CREATED, response_model=SorteoOut)
def create_sorteo(db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    rifas = db.query(models.Rifa).filter(models.Rifa.en_sorteo == False).all()
    premios = db.query(models.Premio).filter(models.Premio.en_sorteo == False).all()


    rifa_ids = []
    for rifa in rifas:
        rifa.en_sorteo = True
        rifa_ids.append(rifa.id)

    premio_ids = []
    for premio in premios:
        premio.en_sorteo = True
        premio_ids.append(premio.id)

    db.commit()


    sorteo = models.Sorteo(
        user_id=current_user.id,
        owner=current_user,
        rifas_id=rifa_ids,
        premios_id=premio_ids
        )
    
    db.add(sorteo)
    db.commit()
    db.refresh(sorteo)
    
    sorteo_sc = models.Sorteo_SC(
        rifas_id=sorteo.rifas_id,
        premios_id=sorteo.premios_id
    )

    db.add(sorteo_sc)
    db.commit()
    db.refresh(sorteo_sc)

    return sorteo

#create a put path operation for update a method
@router.put("/{id}", status_code=status.HTTP_202_ACCEPTED, response_model=SorteoOut)
def get_sorteo(id: int, payload:SorteoUpdate, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    sorteo_sc = db.query(models.Sorteo_SC).filter(models.Sorteo_SC.id == id).first()
    sorteo = db.query(models.Sorteo).filter(models.Sorteo.id == id).first()
    
    if not sorteo_sc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Sorteo con id {id} no encontrado")
    
    if sorteo.user_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=f"No tienes permisos para editar este sorteo")
    
    if sorteo.sorteado:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Este sorteo ya fue realizado")
    
    # update the sorteo
    for field, value in payload.dict(exclude_unset=True).items():
        setattr(sorteo_sc, field, value)
    sorteo_sc.fecha_sorteo = dt.now().strftime("%d/%m/%Y %H:%M:%S")
    
    db.commit()
    db.refresh(sorteo_sc)
    
    # Realizamos el sorteo
    sorteo.sorteado = True
    premios = sorteo_sc.premios_id
    print('hola mundo')
    print(premios)
    rifas_mezcladas = sorteo_sc.rifas_id
    random.shuffle(rifas_mezcladas)
    print(rifas_mezcladas)
    ganadores = list(zip(premios, rifas_mezcladas))

    sorteo_sc.ganadores = ganadores

    db.commit()
    return sorteo_sc

# create a get path operation for get all sorteos
@router.get("/{sorteo_id}", status_code=status.HTTP_200_OK)
def get_all_sorteos(sorteo_id:int, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    sorteos = db.query(models.Sorteo_SC).filter(models.Sorteo_SC.id == sorteo_id).first()
    return sorteos