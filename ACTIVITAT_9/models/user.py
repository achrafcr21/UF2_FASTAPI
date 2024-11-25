from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
    surname: str

    class Config:
        orm_mode = True