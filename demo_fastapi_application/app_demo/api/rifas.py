from fastapi import status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from typing import List, Optional

from ..database import models
from ..schemas.rifas import Rifa, RifaCreate, RifaUpdate, RifaOut
from ..database.database import get_db
from ..auth.oauth2 import get_current_user


router = APIRouter(
    prefix="/v1/rifas",
    tags=['Rifas']
)

# Create
@router.post("/", status_code=status.HTTP_201_CREATED, response_model=Rifa)
def create_rifa(rifa: RifaCreate, db: Session = Depends(get_db), current_user: int = Depends(get_current_user)):

    telefono_existente = db.query(models.Cliente).filter(models.Cliente.telefono == rifa.telefono).first()
    if not telefono_existente:
        cliente_nuevo = models.Cliente(
            **{'nombre': rifa.jugador,
              'telefono': rifa.telefono,
              'fecha_cumple': rifa.fecha_cumple})
        
        db.add(cliente_nuevo)
        db.commit()
        db.refresh(cliente_nuevo)
    
    rifa_dict = rifa.dict(exclude={"fecha_cumple"})
    db_rifa = models.Rifa(**rifa_dict)
    db.add(db_rifa)
    db.commit()
    db.refresh(db_rifa)
    return db_rifa

# Read all Rifas -> schema RifaOut para que todo el mundo tenga acceso a las rifas vendidas, pero no a los telefonos
@router.get("/", response_model=List[RifaOut])
def read_rifas(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    rifas = db.query(models.Rifa).offset(skip).limit(limit).all()
    return rifas

# Read one
@router.get("/{rifa_id}", response_model=Rifa)
def read_rifa(rifa_id: int, db: Session = Depends(get_db), current_user: int = Depends(get_current_user)):
    db_rifa = db.query(models.Rifa).filter(models.Rifa.id == rifa_id).first()
    if not db_rifa:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Rifa not found")
    return db_rifa

# Update - not done
@router.put("/{rifa_id}", response_model=Rifa)
def update_rifa(rifa_id: int, rifa_actualizada: RifaUpdate, db: Session = Depends(get_db), current_user: int = Depends(get_current_user)):
    rifa = db.query(models.Rifa).filter(models.Rifa.id == rifa_id).first()

    if not rifa:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Rifa {rifa_id} no encontrada")

    #TODO: si actualizamos rifa, no actualizamos tabla clientes
    if rifa.dict()['en_sorteo']:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Rifa {rifa_id} ya está en el sorteo y no puede ser modificada")

    for field, value in rifa_actualizada.dict(exclude_unset=True).items():
        setattr(rifa, field, value)

    db.commit()
    db.refresh(rifa)

    return rifa

# Delete
@router.delete("/{rifa_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_rifa(rifa_id: int, db: Session = Depends(get_db), current_user: int = Depends(get_current_user)):
    db_rifa = db.query(models.Rifa).filter(models.Rifa.id == rifa_id)
    
    rifa = db_rifa.first()
    if not rifa:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Rifa not found")
    if rifa.en_sorteo:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Rifa en sorteo, no se puede eliminar")
    
    db_rifa.delete(synchronize_session=False)
    db.commit()
    return None