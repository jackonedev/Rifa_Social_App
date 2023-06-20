from fastapi import FastAPI
from .database.database import engine
from .database import models
from fastapi.middleware.cors import CORSMiddleware
from .api import premios
#https://youtu.be/ToXOb-lpipM


models.Base.metadata.create_all(bind=engine)

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

@app.get("/")
def root():
    return {"message": "Hello World"}

