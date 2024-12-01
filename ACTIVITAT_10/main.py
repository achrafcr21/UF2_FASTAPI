from fastapi import FastAPI
from crud.crud_word import get_all_themes, get_random_word_by_theme
from schemas.word import ThemeOption, WordOption

app = FastAPI()

# Endpoint per obtenir totes les temàtiques
@app.get("/penjat/tematica/opcions", response_model=list[ThemeOption])
async def get_themes():
    return get_all_themes()

# Endpoint per obtenir una paraula segons la temàtica
@app.get("/penjat/tematica/{option}", response_model=list[WordOption])
async def get_word(option: str):
    return get_random_word_by_theme(option)