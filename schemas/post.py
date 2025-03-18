from pydantic import BaseModel

class PostCreate(BaseModel):
    name: str
    brand: str
    category: str
    image: str
    color: str
    size: str
    group: str
    price: str 

class PostResponse(BaseModel):
    id: int
    name: str
    brand: str
    category: str
    image: str
    color: str
    size: str
    group: str
    price: str 

    class Config:
        from_attributes = True
