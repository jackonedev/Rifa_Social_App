from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, LargeBinary, Date  
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP
from .database import Base



class Cliente(Base):
    __tablename__ = "clientes"
    id = Column(Integer, primary_key=True, nullable=False)
    nombre = Column(String, nullable=False)
    apellido = Column(String, nullable=True)
    telefono = Column(String, nullable=False, unique=True)
    fecha_cumple = Column(Date, nullable=True)
    fecha_registro = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text('now()'))
    
    
class Premio(Base):
    __tablename__ = "premios"
    id = Column(Integer, primary_key=True, nullable=False)
    nombre = Column(String, nullable=False)
    descripcion = Column(String, nullable=False)
    cantidad = Column(Integer, nullable=False, default=1)
    precio = Column(Integer, nullable=False, default=3000)
    descuento = Column(Integer, nullable=False, default=25)
    auspiciante = Column(String, nullable=False, default="Anónimo")
    imagen = Column(LargeBinary, nullable=True)
    imagen_url = Column(String(500), nullable=True, index=True)
    fecha_registro = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text('now()'))

class Rifa(Base):
    __tablename__ = "rifas"
    id = Column(Integer, primary_key=True, nullable=False)
    jugador = Column(String, nullable=False)# "nombre y apellido"
    telefono = Column(String, nullable=False)
    fecha_cumple = Column(Date, nullable=True)
    fecha_registro = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text('now()'))
    lugar_registro = Column(String, nullable=False)
