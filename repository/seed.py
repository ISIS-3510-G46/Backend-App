import pandas as pd
import random
from faker import Faker

fake = Faker()

""" SEED used for generating fake posts for the postgreSQL database
"""

# Possible values
categories = ["Nublado", "Frio", "Lluvia", "Calor", "Oferta"]
brands = ["Nike", "Adidas", "Puma", "Zara", "Levi's", "Fila", "Ralph Lauren", "Tommy Hilfiger", "Lacoste"]
colors = ["Rojo", "Negro", "Azul", "Gris", "Amarillo"]
sizes = ["XS", "S", "M", "L", "XL"]
groups = ["Hombre", "Mujer", "Niños", "Niñas"]


image_mapping = {
    "T-Shirt": "https://ayapromotions.mx/wp-content/uploads/2021/03/playera-pc-cr-mc-joven-100algodon-jade_1.png",
    "Jeans": "https://www.pngarts.com/files/6/Jeans-PNG-High-Quality-Image.png",
    "Sneakers": "https://www.pngarts.com/files/4/Sneaker-PNG-Image.png",
    "Jacket": "https://www.pngplay.com/wp-content/uploads/15/Jacket-Red-Leather-PNG-Photo-Image.png",
    "Dress": "https://pngimg.com/d/dress_PNG147.png",
    "Cap": "https://pngimg.com/d/cap_PNG5671.png",
    "Hoodie": "https://png.pngtree.com/png-clipart/20240103/original/pngtree-red-hoodie-isolated-png-image_14006380.png"
}

# 30 samples
data = []
for i in range(1, 50):
    product_name = random.choice(list(image_mapping.keys()))
    data.append({
        "id": str(i),
        "name": product_name,
        "brand": random.choice(brands),
        "category": random.choice(categories),
        "image": image_mapping[product_name],
        "color": random.choice(colors),
        "size": random.choice(sizes),
        "group": random.choice(groups),
        "price": f"{random.randint(10000, 200000):,}" 
    })

df = pd.DataFrame(data)
df.to_csv("repository/seed_for_supabase.csv", index=False)
