from pydantic import BaseModel
from typing import Optional

class PostCreate(BaseModel):
    name: str
    brand: str
    category: str
    image: str
    color: str
    size: str
    group: str
    price: str 
    thumbnail: Optional[str] = None

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
    thumbnail: Optional[str] = None

    class Config:
        from_attributes = True
