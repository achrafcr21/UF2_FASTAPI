from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    Nom: str
    edat: int
    ciutat: str

@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}

@app.post("/items/")
def create_item(item: Item):
    return {"Nom": item.name, "edat": item.price, "ciutat": item.ciutat}