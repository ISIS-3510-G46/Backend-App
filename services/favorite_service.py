from repository.favorite_repo import add_favorite
from schemas.favorite import Favorite

def register_favorite(favorite: Favorite):
    return add_favorite(favorite)

