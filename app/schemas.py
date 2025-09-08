from pydantic import BaseModel

class PersonBase(BaseModel):
    name: str
    age: int
    city: str

class PersonCreate(PersonBase):
    pass

class PersonResponse(PersonBase):
    id: int

    class Config:
        orm_mode = True
