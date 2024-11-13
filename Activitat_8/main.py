from fastapi import FastAPI
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
def read_item(item_id: int):
    return {"item_id": item_id}

@app.post("/items/")
def create_item(item: Item):
    return {"Nom": item.Nom, "edat": item.edat, "ciutat": item.ciutat}