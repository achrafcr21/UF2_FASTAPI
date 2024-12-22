from fastapi import FastAPI, HTTPException
from crud import create_user, get_user, update_user, delete_user
from crud import create_word, get_word, get_alphabet_by_language

# Crear aplicació FastAPI
app = FastAPI()

# ------------------ CRUD per a "users" ------------------
@app.post("/users/")
async def create_new_user(user: dict):
    result = create_user(user)
    if result:
        return {"message": "Usuari creat correctament!"}
    else:
        raise HTTPException(status_code=400, detail="Error al crear l'usuari.")

@app.get("/users/{user_id}")
async def read_user(user_id: int):
    user = get_user(user_id)
    if user:
        return user
    else:
        raise HTTPException(status_code=404, detail="Usuari no trobat.")

@app.put("/users/{user_id}")
async def update_existing_user(user_id: int, user_data: dict):
    result = update_user(user_id, user_data)
    if result:
        return {"message": "Usuari actualitzat correctament!"}
    else:
        raise HTTPException(status_code=400, detail="Error al actualitzar l'usuari.")

@app.delete("/users/{user_id}")
async def delete_existing_user(user_id: int):
    result = delete_user(user_id)
    if result:
        return {"message": "Usuari esborrat correctament!"}
    else:
        raise HTTPException(status_code=404, detail="Usuari no trobat.")

# ------------------ CRUD per a "word" ------------------
@app.post("/words/")
async def create_new_word(word_data: dict):
    result = create_word(word_data)
    if result:
        return {"message": "Paraula afegida correctament!"}
    else:
        raise HTTPException(status_code=400, detail="Error al afegir la paraula.")

@app.get("/words/random")
async def get_random_word():
    word = get_word()
    if word:
        return {"random_word": word}
    else:
        raise HTTPException(status_code=404, detail="No s'han trobat paraules.")

# ------------------ Endpoint per a "alphabet" ------------------
@app.get("/alphabet/{lang}")
async def get_alphabet(lang: str):
    letters = get_alphabet_by_language(lang)
    if letters:
        return {"alphabet": letters}
    else:
        raise HTTPException(status_code=404, detail="No s'ha trobat cap alfabet per aquest idioma.")