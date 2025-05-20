from database import supabase
from schemas.post import PostCreate
from storage import get_storage_image
from services.color_classifier import get_dominant_color
from services.thumbnail_generator import generate_thumbnail



def create_post(post: PostCreate):
    post_image = get_storage_image(post.image) # Get image from storage
    dominant_color = get_dominant_color(post_image) # Get clothing color
    img_thumbnail_id = generate_thumbnail(post_image) # Generate thumbnail

    response = supabase.table("Post").insert({
        "name": post.name,
        "brand": post.brand,
        "category": post.category,
        "image": post.image,
        "color": dominant_color,
        "size": post.size,
        "group": post.group,
        "price": post.price,
        "thumbnail": img_thumbnail_id,
        "userId": post.userId
    }).execute()
    return response.data[0]

def get_posts():
    response = supabase.table("Post").select("*").execute()
    return response.data

def get_posts_by_categ(category_name):
    print(category_name)
    # Query to fetch clothing items by category
    response = supabase.table("Post").select("*").eq("category", category_name).execute()
    return response.data

def get_post_id(post_id: int):
    response = supabase.table("Post").select("*").eq("id", post_id).execute()
    return response.data[0] if response.data else None
