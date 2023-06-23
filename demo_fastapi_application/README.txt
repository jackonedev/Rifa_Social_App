# RIFA SOCIAL APP

#1) Instalacion de dependencias
fastapi[all]
uvicorn[standard]
SQLAlchemy
pytest
passlib[bcrypt]
python-jose[cryptography]

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

#4) CRUD: Clientes
schemas.clientes.py
api.clientes.py: utilizamos utils.tools para define_date en POST request
utils.tools.py: funciones de validacion de datos
tests/test_utils.py: fichero test driven app_demo/utils/tools.py

#5) CRUD: Rifas
schemas.rifas.py: los modelos pydantic difieren del modelo sqalchemy
api.rifas.py: parte de la información recopilada se registra en el modelo Clientes
api.collections/: creamos backup

#6) Validaciones
telefono: a través de patrón regex en el modelo Pydantic
fecha_cumple: validacion del request body antes de crear el registro en la tabla
EmailStr: objeto standard pydantic
HtmlUrl: objeto estandar pydantic

#7) Testing
test/database.py: creación de una base de datos rifa_app_test con conexión overrid
test/test_premios.py: utilizando sesion con esquema modular se crearon los primeros test
test/test_utils.py: fichero test driven app_demo/utils/tools.py

#8) Autenticación
database/models.py: creacion del modelo User, Sorteo
schemas/users.py: creación del modelo para User y token
api/user.py: endpoint for creating users and get a particular user
api/auth.py: endpoint for login user
collections/: backup updated
auth/oauth2.py: module for managing user token
utils/utils.py: tools for cryptography processing


#9) Migraciones
Agregar la tabla de sorteos
Agregar las columnas de sorteado(bool)

#10) Deployment

#11) Presentacion