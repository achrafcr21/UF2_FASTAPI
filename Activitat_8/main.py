from fastapi import FastAPI, Response, status
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class Item(BaseModel):
    Nom: str
    edat: int
    ciutat: str
    alçada: float
    pes: float
    any_neixament: Optional[int] = None
    

@app.get("/")
def read_item():
    return {"Hola profe"}


@app.get("/items/{item_id}")
def read_item(item_id: int, response: Response):
    # Suposem que estem buscant un ítem específic, si no el trobem, retornem un error 404.
    if item_id != 1:  # Asumim que només tenim un ítem amb id 1.
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"error": "Item no trobat"}
    return {"item_id": item_id}

@app.post("/items/")
def create_item(item: Item):
    return {"Nom": item.Nom, "edat": item.edat, "ciutat": item.ciutat}