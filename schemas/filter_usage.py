from pydantic import BaseModel
from typing import Optional


class FilterUsage(BaseModel):
    filter_type: str
    filter_value: str
    latitude: Optional[float]
    longitude: Optional[float]
