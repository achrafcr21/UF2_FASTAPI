from fastapi import FastAPI
from crud import get_boto_comencar_partida, get_intents, get_alfabet, get_paraula_aleatoria

app = FastAPI()

# Endpoint per al botó "Començar partida"
@app.get("/penjat/boto")
async def boto_comencar_partida():
    text = get_boto_comencar_partida()
    return {"text": text}

# Endpoint per obtenir intents incorrectes
@app.get("/penjat/intents/{log_id}")
async def obtenir_intents(log_id: int):
    intents = get_intents(log_id)
    return {"incorrect_attempts": intents}

# Endpoint per obtenir l'alfabet segons idioma
@app.get("/penjat/alfabet/{lang}")
async def obtenir_alfabet(lang: str):
    letters = get_alfabet(lang)
    return {"alphabet": letters}

# Endpoint per obtenir una paraula aleatòria
@app.get("/penjat/paraula")
async def obtenir_paraula_aleatoria():
    paraula = get_paraula_aleatoria()
    return {"word": paraula}