from pydantic import BaseModel

# Esquema per a les temàtiques
class ThemeOption(BaseModel):
    option: str

# Esquema per a la paraula retornada segons la temàtica
class WordOption(BaseModel):
    option: str