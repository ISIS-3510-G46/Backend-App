from pydantic import BaseModel
from typing import Optional

class Favorite(BaseModel):
    brand: str
    count: int

