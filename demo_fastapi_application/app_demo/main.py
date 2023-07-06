from fastapi import FastAPI
# from .database.database import engine
# from .database import models
from fastapi.middleware.cors import CORSMiddleware
from .api import premios, clientes, rifas, users, auth, sorteos
import requests, psycopg2
#https://youtu.be/ToXOb-lpipM

# models.Base.metadata.create_all(bind=engine)

app = FastAPI()


origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(premios.router)
app.include_router(clientes.router)
app.include_router(rifas.router)
app.include_router(users.router)
app.include_router(auth.router)
app.include_router(sorteos.router)

@app.get("/")
def root():
    base_url = "http://localhost:8000/v1"
    # create a requests for creating a user
    response = requests.post(f"{base_url}/users/", json={"email": "test2@test.com", "password": "test"})
    print(response.json())

    # let's login the user - from now on it has 30 minutes to use the token
    response = requests.post(f"{base_url}/login/", data={"username": "test2@test.com", "password": "test"})
    print(response.json())
    # get the access token
    access_token = response.json()["access_token"]
    # create a header with the token
    headers = {"Authorization": f"Bearer {access_token}"}

    # let's create some rifas
    for i in range(5):
        requests.post(f"{base_url}/rifas/", 
                      headers=headers,
                      json={"jugador": "Alejandra Z", "telefono": "351556677", "fecha_cumple": None})
    for i in range(3):
        requests.post(f"{base_url}/rifas/", 
                      headers=headers,
                      json={"jugador": "Hector Hernandez", "telefono": "3512232233", "fecha_cumple": "15/05/1980"})
    for i in range(10):
        requests.post(f"{base_url}/rifas/", 
                      headers=headers,
                      json={"jugador": "Santiago", "telefono": "+543516104545", "fecha_cumple": "20/05"})
    for i in range(4):
        requests.post(f"{base_url}/rifas/", 
                      headers=headers,
                      json={"jugador": "Fabricio Tomaselli", "telefono": "351-3511111", "fecha_cumple": "3 de febrero"})

    # let's create some premios
    requests.post(f"{base_url}/premios/", 
                  headers=headers,
                  json={"nombre": "Ganaste una cena para dos personas en Menorca Bar",
                        "descripcion": "Cena para dos personas en Menorca Bar, incluye entrada, plato principal, postre y bebida",
                        "precio": 18000})
    requests.post(f"{base_url}/premios/",
                  headers=headers,
                  json={"nombre": "Ganaste una botella de vino Malbec de finca Mendocina",
                        "descripcion": "Botella de vino de regalo más descuento del 30% en la segunda unidad",
                        "precio": 7500})
    requests.post(f"{base_url}/premios/",
                  headers=headers,
                   json={"nombre": "3 litros de birra artesanal Cordobesa",
                         "precio": 2500,
                         "auspiciante": "La Casa del Chopp!",
                         "cantidad": 3,
                         "descripcion": "3 botellas de 1 litro de cerveza artesanal Cordobesa"})
 



    return {"message": "Hello World"}

