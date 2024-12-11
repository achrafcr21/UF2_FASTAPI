from fastapi import FastAPI
from database import db_connection



app = FastAPI()

@app.get("/penjat/boto")
async def boto_comencar_partida():
    conn = db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT word FROM word WHERE word = 'començar partida'")
    text = cursor.fetchone()
    conn.close()
    return {"text": text[0]} if text else {"text": ""}
    


#endpoint pels intents:
@app.get("/penjat/intents/{log_id}")
async def obtenir_intents(log_id: int):
    conn = db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM attempt WHERE log_id = %s AND is_correct = false", (log_id,))
    intents = cursor.fetchone()
    conn.close()
    return {"incorrect_attempts": intents[0]}


#endpoint alphabet
@app.get("/penjat/alfabet/{lang}")
async def obtenir_alfabet(lang: str):
    conn = db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT letter FROM alphabet WHERE lang = %s", (lang,))
    letters = cursor.fetchall()
    conn.close()
    return {"alphabet": [row[0] for row in letters]}


@app.get("/penjat/paraula")
async def obtenir_paraula_aleatoria():
    conn = db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT word FROM word")
    paraules = cursor.fetchall()
    conn.close()
    return {"word": random.choice(paraules)[0]} if paraules else {"word": ""}