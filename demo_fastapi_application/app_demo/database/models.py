from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, LargeBinary
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP
from .database import Base

class Cliente(Base):
    __tablename__ = "clientes"
    id = Column(Integer, primary_key=True, nullable=False)
    nombre = Column(String, nullable=False)
    apellido = Column(String, nullable=False)
    telefono = Column(String, nullable=False)
    fecha_cumple = Column(String, nullable=True)
    fecha_registro = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text('now()'))
    
    
class Premio(Base):
    __tablename__ = "premios"
    id = Column(Integer, primary_key=True, nullable=False)
    nombre = Column(String, nullable=False)
    descripcion = Column(String, nullable=False)
    cantidad = Column(Integer, nullable=False, default=1)
    precio_dcto = Column(String, nullable=False, default="$3000/20%")
    auspiciante = Column(String, nullable=False, default="Anónimo")
    imagen = Column(LargeBinary, nullable=True)
    imagen_url = Column(String, nullable=True)
    fecha_registro = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text('now()'))

class Rifa(Base):
    __tablename__ = "rifas"
    id = Column(Integer, primary_key=True, nullable=False)
    jugador = Column(String, nullable=False)#TODO: When a rifa is purchased, it is verified if the player exists in the customer table, if it does not exist, a new customer is created
    contacto = Column(String, nullable=False)
    fecha_registro = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text('now()'))
    lugar_registro = Column(String, nullable=False)

"""
To implement the TODO statement, you can use SQLAlchemy's exists() function to check if a player exists in the Customer table. If the player does not exist, you can create a new Customer object and add it to the session. Here's an example implementation:

``
from sqlalchemy import exists
from models import Customer, Rifa

# Assume `session` is a SQLAlchemy session object

# Get the player name from the Rifa object
player_name = rifa.player_name

# Check if the player exists in the Customer table
player_exists = session.query(exists().where(Customer.name == player_name)).scalar()

if not player_exists:
    # If the player does not exist, create a new Customer object
    customer = Customer(name=player_name)

    # Add the new Customer object to the session
    session.add(customer)

# Commit the changes to the database
session.commit()
``

In this example, we first get the player name from the Rifa object. We then use SQLAlchemy's exists() function to check if the player exists in the Customer table. If the player does not exist, we create a new Customer object with the player's name and add it to the session. Finally, we commit the changes to the database.
"""