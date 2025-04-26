from fastapi import APIRouter, Depends, HTTPException
from schemas.favorite import Favorite
from services.favorite_service import register_favorite

router = APIRouter(prefix="/favorites", tags=["favorites"])


@router.post("/add")
def add_favorite(favorite: Favorite):
    try:
        new_post = register_favorite(favorite)
        return new_post
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))