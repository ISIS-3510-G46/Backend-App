from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

# mockss
clothing_posts = [
    {"id":"1", "name": "T-Shirt", "price": "20,000", "brand": "Nike", "category": "summer" , "image": "https://assets.adidas.com/images/w_600,f_auto,q_auto/92103a27abea4abbb23ccc98cbbd2c4c_9366/Camiseta_de_Local_Al_Nassr_FC_24-25_Ronaldo_Amarillo_JP0459_02_laydown.jpg"},
    {"id":"2", "name": "Jeans", "price": "22,000", "brand": "Levi's", "category": "casual", "image": "https://i.pinimg.com/736x/fb/e0/2e/fbe02ee07f0f0327a7b9670862c6c11f.jpg"},
    {"id":"3", "name": "Tenis", "price": "22,333", "brand": "Puma",   "category": "sale", "image": "https://static.vecteezy.com/system/resources/thumbnails/036/575/605/small/puma-black-sneakers-isolated-png.png"},
    {"id":"4", "name": "Jeans", "price": "22,000", "brand": "Levi's", "category": "casual", "image": "https://i.pinimg.com/736x/fb/e0/2e/fbe02ee07f0f0327a7b9670862c6c11f.jpg"},
    {"id":"5", "name": "Jeans", "price": "22,000", "brand": "Levi's", "category": "casual", "image": "https://i.pinimg.com/736x/fb/e0/2e/fbe02ee07f0f0327a7b9670862c6c11f.jpg"},
    {"id":"6", "name": "Jeans", "price": "22,000", "brand": "Levi's", "category": "casual", "image": "https://i.pinimg.com/736x/fb/e0/2e/fbe02ee07f0f0327a7b9670862c6c11f.jpg"},
    {"id":"7", "name": "Jeans", "price": "22,000", "brand": "Levi's", "category": "casual", "image": "https://i.pinimg.com/736x/fb/e0/2e/fbe02ee07f0f0327a7b9670862c6c11f.jpg"},

]

# Data model
class ClothingPost(BaseModel):
    id: str
    name: str
    price: str
    brand: str
    category: str
    image: str

@app.get("/clothing", response_model=List[ClothingPost])
def get_clothing():
    return clothing_posts 



# ✅ Fetch clothing items by category
@app.get("/clothing/category/{category_name}", response_model=List[ClothingPost])
def get_clothing_by_category(category_name: str):
    filtered_posts = [post for post in clothing_posts if post["category"].lower() == category_name.lower()]
    return filtered_posts