from fastapi import status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from typing import List, Optional
from datetime import datetime

from ..database import models
from ..schemas.clientes import Cliente, ClienteCreate, ClienteUpdate
from ..database.database import get_db

router = APIRouter(
    prefix="/v1/clientes",
    tags=['Clientes']
)


# Create
@router.post("/", status_code=status.HTTP_201_CREATED, response_model=Cliente)
def create_cliente(cliente: ClienteCreate, db: Session = Depends(get_db)):
    # Verificar el formato con el que llega cliente.fecha_cumple
    if cliente.fecha_cumple:
        cliente.fecha_cumple = datetime.strptime(cliente.fecha_cumple, '%d/%m/%Y')
    else:
        cliente.fecha_cumple = None
    db_cliente = models.Cliente(**cliente.dict())
    db.add(db_cliente)
    db.commit()
    db.refresh(db_cliente)
    return db_cliente

# Read all
@router.get("/", response_model=List[Cliente])
def read_clientes(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    clientes = db.query(models.Cliente).offset(skip).limit(limit).all()
    return clientes

# Read one
@router.get("/{cliente_id}", response_model=Cliente)
def read_cliente(cliente_id: int, db: Session = Depends(get_db)):
    db_cliente = db.query(models.Cliente).filter(models.Cliente.id == cliente_id).first()
    if not db_cliente:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Cliente not found")
    return db_cliente

# Update
@router.put("/{cliente_id}", response_model=Cliente)
def update_cliente(cliente_id: int, cliente_actualizado: ClienteUpdate, db: Session = Depends(get_db)):
    cliente = db.query(models.Cliente).filter(models.Cliente.id == cliente_id).first()

    if not cliente:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Cliente {cliente_id} no encontrado")

    for field, value in cliente_actualizado.dict(exclude_unset=True).items():
        setattr(cliente, field, value)

    db.commit()
    db.refresh(cliente)

    return cliente

# Delete
@router.delete("/{cliente_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_cliente(cliente_id: int, db: Session = Depends(get_db)):
    db_cliente = db.query(models.Cliente).filter(models.Cliente.id == cliente_id)
    if not db_cliente.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Cliente not found")
    db_cliente.delete(synchronize_session=False)
    db.commit()
    return None