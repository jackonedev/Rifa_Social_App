from fastapi import status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from typing import List, Optional

from ..database import models
from ..schemas.premios import Premio, PremioCreate, PremioUpdate
from ..database.database import get_db
from ..auth.oauth2 import get_current_user

router = APIRouter(
    prefix="/v1/premios",
    tags=['Premios']
)



@router.get("/", response_model=List[Premio])
def get_premios(db: Session = Depends(get_db), skip: int = 0, limit: int = 100, search: Optional[str] = "", current_user: models.User = Depends(get_current_user)):
    print(search)
    premios = db.query(models.Premio).offset(skip).limit(limit).all()
    return premios


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=Premio)
def create_premio(premio_nuevo: PremioCreate, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):

    for i in range(premio_nuevo.cantidad):
        premio = models.Premio(user_id=current_user.id, **premio_nuevo.dict(exclude={'cantidad'}))
        db.add(premio)
        db.commit()
        db.refresh(premio)

    return premio


@router.get("/{premio_id}", response_model=Premio)
def get_premio(premio_id: int, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    premio = db.query(models.Premio).filter(models.Premio.id == premio_id).first()
    if not premio:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Premio {premio_id} no encontrado")
    return premio


@router.delete("/{premio_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_premio(premio_id: int, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    
    premio = db.query(models.Premio).filter(models.Premio.id == premio_id).first()

    if not premio:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Premio {premio_id} no encontrado")
    
    if premio.user_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=f"Usuario no autorizado")
    db.delete(premio)
    db.commit()


@router.put("/{premio_id}", response_model=Premio)
def update_premio(premio_id: int, premio_actualizado: PremioUpdate, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    premio = db.query(models.Premio).filter(models.Premio.id == premio_id).first()

    if not premio:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Premio {premio_id} no encontrado")

    for field, value in premio_actualizado.dict(exclude_unset=True).items():
        setattr(premio, field, value)

    db.commit()
    db.refresh(premio)

    return premio
