# RIFA SOCIAL APP

#1) Instalacion de dependencias
fastapi[all]
uvicorn[standard]
SQLAlchemy

#2) Conexión de la base de datos
utils.config.py
database.database.py
database.models.py
main.py: creamos el engine

#3) CRUD: Premios
schemas.premios.py
api.premios.py
api.collections/
main.py: colocamos MiddleWare y añadimos routers



# NOTAS DE LOS MODELOS
SERVICIO participacion
Premios:
- id
- nombre
- cantidad
- precio
- ...

- fecha_sorteo
- rifa_id
- ganador
- fecha_retiro
- foto

Rifas:
- id
- jugador
- contacto
- fecha_inscripcion
- lugar_inscripcion

- fecha_sorteo
- resultado_sorteo

Sorteo:
- id
- nombre
- fechas_creacion
- fecha_sorteo
- premios [array]



CLIENTE
Cliente:
-id
-nombre y apellido
-telefono
-cumpleaños (nullable=True)

COMODATO