from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

"""
ARCHIVO DE PRUEBAS (Usado antes como backend):

- Solo para pruebas, lo estuve usando para testear kotlin.
- Los endpoints funcionan bien toca ver como meter y sacar la info de una bd.
- Posiblemente agregar mas variables y entidades.
- Si o si necesitamos las variables: 
    - id:str
    - name: str
    - price: str
    - brand: str    
    - category: str : Nublado | Frio | Lluvia | Calor | Oferta
    - image: str    : URL
    - color: str    : Cualquier color textual (Rojo, Negro, Azul, etc)
    - size: str     : XS | S | M | L | XL
    - group: str    : Hombre | Mujer 

""" 

# mockss
clothing_posts = [
    {"id":"1", "name": "T-Shirt", "price": "20,000", "brand": "Nike", "category": "Nublado" , "image": "https://assets.adidas.com/images/w_600,f_auto,q_auto/92103a27abea4abbb23ccc98cbbd2c4c_9366/Camiseta_de_Local_Al_Nassr_FC_24-25_Ronaldo_Amarillo_JP0459_02_laydown.jpg", "color":"Rojo", "size":"S", "group": "Hombre"},
    {"id":"2", "name": "Jeans", "price": "22,000", "brand": "Levi's", "category": "Nublado", "image": "https://i.pinimg.com/736x/fb/e0/2e/fbe02ee07f0f0327a7b9670862c6c11f.jpg", "color":"Rojo", "size":"S", "group": "Hombre"},
    {"id":"3", "name": "Tenis", "price": "22,333", "brand": "Puma",   "category": "Frio", "image": "https://static.vecteezy.com/system/resources/thumbnails/036/575/605/small/puma-black-sneakers-isolated-png.png", "color":"Rojo", "size":"S", "group": "Hombre"},
    {"id":"4", "name": "Jeans", "price": "22,000", "brand": "Levi's", "category": "Frio", "image": "https://i.pinimg.com/736x/fb/e0/2e/fbe02ee07f0f0327a7b9670862c6c11f.jpg", "color":"Rojo", "size":"S", "group": "Hombre"},
    {"id":"5", "name": "Jeans", "price": "22,000", "brand": "Levi's", "category": "Lluvia", "image": "https://i.pinimg.com/736x/fb/e0/2e/fbe02ee07f0f0327a7b9670862c6c11f.jpg", "color":"Negro", "size":"S", "group": "Hombre"},
    {"id":"6", "name": "Jeans", "price": "22,000", "brand": "Levi's", "category": "Calor", "image": "https://i.pinimg.com/736x/fb/e0/2e/fbe02ee07f0f0327a7b9670862c6c11f.jpg", "color":"Azul", "size":"S", "group": "Mujer"},
    {"id":"7", "name": "Jeans", "price": "22,000", "brand": "Levi's", "category": "Oferta", "image": "https://i.pinimg.com/736x/fb/e0/2e/fbe02ee07f0f0327a7b9670862c6c11f.jpg", "color":"Rojo", "size":"S", "group": "Hombre"},

]

# Data model
class ClothingPost(BaseModel):
    id: str
    name: str
    price: str
    brand: str
    category: str
    image: str
    color: str
    size: str
    group: str




@app.get("/clothing", response_model=List[ClothingPost])
def get_clothing():
    return clothing_posts 



@app.get("/clothing/category/{category_name}", response_model=List[ClothingPost])
def get_clothing_by_category(category_name: str):
    filtered_posts = [post for post in clothing_posts if post["category"].lower() == category_name.lower()]
    return filtered_posts