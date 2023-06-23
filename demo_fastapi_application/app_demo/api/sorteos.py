from fastapi import status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from typing import List, Optional

from ..database import models
from ..schemas.rifas import Rifa, RifaCreate, RifaUpdate, RifaOut
from ..database.database import get_db
from ..auth.oauth2 import get_current_user


router = APIRouter(
    prefix="/v1/sorteos",
    tags=['Sorteos']
)


# create a post path operation for creating a new sorteo

@router.post("/", status_code=status.HTTP_201_CREATED)
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

    print(rifa_ids)
    print(premio_ids)




    # db.add(rifa)
    # db.commit()
    # db.refresh(rifa)

    # return rifa