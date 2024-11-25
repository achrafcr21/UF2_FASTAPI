from fastapi import FastAPI
from db_connect.database import read_users

app = FastAPI()

@app.get("/users/")
async def get_users():
    return read_users()
