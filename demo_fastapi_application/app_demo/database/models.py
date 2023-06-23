from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, ARRAY
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.orm import relationship
from .database import Base
from typing import List



class Cliente(Base):
    __tablename__ = "clientes"
    id = Column(Integer, primary_key=True, nullable=False)
    nombre = Column(String, nullable=False)
    apellido = Column(String, nullable=True)
    telefono = Column(String, nullable=False, unique=True)
    email = Column(String, nullable=True)
    fecha_cumple = Column(String, nullable=True)
    fecha_registro = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text('now()'))
    
    
class Premio(Base):
    __tablename__ = "premios"
    id = Column(Integer, primary_key=True, nullable=False)
    nombre = Column(String, nullable=False)
    cantidad = Column(Integer, nullable=False, default=1)
    precio = Column(Integer, nullable=False, default=3000)
    descuento = Column(Integer, nullable=True)
    auspiciante = Column(String, nullable=False, default="Anónimo")
    descripcion = Column(String, nullable=False)
    imagen_url = Column(String(500), nullable=True, index=True)
    fecha_registro = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text('now()'))
    en_sorteo = Column(Boolean, nullable=False, default=False)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)

class Rifa(Base):
    __tablename__ = "rifas"
    id = Column(Integer, primary_key=True, nullable=False)
    jugador = Column(String, nullable=False)# "nombre y apellido"
    telefono = Column(String, nullable=False)
    fecha_registro = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text('now()'))
    lugar_registro = Column(String, nullable=False, default='Lima - Gral. Paz')
    en_sorteo = Column(Boolean, nullable=False, default=False)

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, nullable=False)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text('now()'))

class Sorteo(Base):
    __tablename__ = "sorteos"
    id = Column(Integer, primary_key=True, nullable=False)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    rifas_id = Column(ARRAY(Integer), nullable=False, unique=True)
    premios_id = Column(ARRAY(Integer), nullable=False, unique=True)
    fecha_registro = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text('now()'))
    sorteado = Column(Boolean, nullable=False, default=False)

    owner = relationship("User")#, back_populates="sorteos")
    
class Sorteo_SC(Base):
    __tablename__ = "sorteos_realizados"
    id = Column(Integer, primary_key=True, nullable=False)
    rifas_id = Column(ARRAY(Integer), ForeignKey("sorteos.rifas_id", ondelete="CASCADE"), nullable=False)
    premios_id = Column(ARRAY(Integer),ForeignKey("sorteos.premios_id", ondelete="CASCADE"), nullable=False)
    fecha_registro = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text('now()'))
    fecha_sorteo = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text('now()'))
    lugar_sorteo = Column(String, nullable=False, default='Lima - Gral. Paz')
    auspciante = Column(String, nullable=False, default='Anónimo')
    contacto = Column(String, nullable=False, default='Telefono:')
    ganadores = Column(ARRAY(String), nullable=False)