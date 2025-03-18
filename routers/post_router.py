from typing import List
from fastapi import APIRouter, HTTPException
from services.post_service import register_post, get_all_posts, get_posts_by_category
from schemas.post import PostCreate, PostResponse

router = APIRouter()


""" Aca implementamos los API endpoints que tienen que ver con posts 
    TODO: Falta ver si el endpoint de crear post funciona correctamente.

    Cada ruta (en este momento para acceder seria localhost:8000/RUTA, por ejemplo: localhost:8000/clothing)
    Manda a service que solo tiene las declaraciones de los metodos (pero alli pueden hacer verificaciones anteriores si se requiere)
    Luego service manda a post_repo (en la caperta repository) que finalmente hace la consulta a la BD postgreSQL desplegada en Supabase.
    Para esto usa el schema de post, que parsea las respuestas del modelo de datos.
    Finalmente retorna aqui para que lo consuma la aplicacion front (Kotlin o Flutter)

"""


@router.post("/create-post/", response_model=PostResponse)
def create_post(post: PostCreate):
    try:
        new_post = register_post(post)
        return new_post
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))



@router.get("/clothing", response_model=List[PostResponse])
def get_all_clothing():
    try:
        all_posts = get_all_posts()
        return all_posts
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    



@router.get("/clothing/category/{category_name}", response_model=List[PostResponse])
def get_clothing_by_category(category_name: str):
    posts_by_category = get_posts_by_category(category_name)
    if not posts_by_category:
        raise HTTPException(status_code=404, detail="No posts found.")
    return posts_by_category 
