from fastapi import FastAPI, Body
from pydantic import BaseModel, Field
#https://youtu.be/ToXOb-lpipM?t=4959


class Premio(BaseModel):
    id: int = Field(..., example="1")
    content: str = Field(..., example="Premio 1")
    autor:str  = None
    fecha:str = None
    imagen:str = None



app = FastAPI()



@app.get("/")
def root():
    return {"message": "Hello World"}


@app.get("/v1/premios")
def get_premios():
    return {"message": "Estos son los premios"}


@app.get("/v1/premios/{premio_id}")
def get_premio(premio_id: int):
    return {"message": f"Este es el premio {premio_id}"}

@app.post("/v1/premios")
def create_premio(premio_nuevo: Premio):#para qué sirve embed=True en Body parametros
    print(premio_nuevo.dict())
    return {"nuevo_premio": f"Se creo el premio contenido {premio_nuevo.content}, autor {premio_nuevo.autor}, fecha {premio_nuevo.fecha}"}

@app.put("/v1/premios/{premio_id}")
def update_premio(premio_id: int):
    return {"message": f"Premio {premio_id} actualizado"}

@app.delete("/v1/premios/{premio_id}")
def delete_premio(premio_id: int):
    return {"message": f"Premio {premio_id} eliminado"}









