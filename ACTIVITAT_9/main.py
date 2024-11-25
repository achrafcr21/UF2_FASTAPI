from fastapi import FastAPI
from ACTIVITAT_9.crud.users import read_users

app = FastAPI()

@app.get("/users/")
async def get_users():
    return read_users()