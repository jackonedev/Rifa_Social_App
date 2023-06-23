from fastapi import FastAPI
from .database.database import engine
from .database import models
from fastapi.middleware.cors import CORSMiddleware
from .api import premios, clientes, rifas, users, auth, sorteos
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
    return {"message": "Hello World"}

