# RIFA SOCIAL APP

#1) Instalacion de dependencias
fastapi[all]
uvicorn[standard]
SQLAlchemy


SERVICIO participacion
Premios:
- id
- nombre
- descripcion (por si son descuentos, o promos con descuento pack-descontado)
- precio|descuento ($0001|$3000/20%) 
- fecha_ingreso
- auspiciante
- imagen (nullable=True)

- fecha_sorteo
- cantidad

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

COMODATO