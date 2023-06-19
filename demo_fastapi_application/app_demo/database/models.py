from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP
from .database import Base

class Cliente(Base):
    __tablename__ = "clientes"
    id = Column(Integer, primary_key=True, nullable=False)
    nombre_apellido = Column(String, nullable=False)
    telefono = Column(String, nullable=False)
    fecha_cumple = Column(String, nullable=True)
    fecha_registro = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text('now()'))
    
    
    
    
    
    # for rifa
    # owner_id = Column(Integer, ForeignKey(
    #     "users.id", ondelete="CASCADE"), nullable=False)