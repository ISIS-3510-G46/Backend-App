from pydantic import BaseModel
from typing import Optional

class Favorite(BaseModel):
    brand: str
    count: int
    latitude: Optional[float] = None
    longitude: Optional[float] = None

