from database import supabase
from schemas.post import PostCreate
import os
from dotenv import load_dotenv
import requests
from appwrite.client import Client
from appwrite.services.storage import Storage

load_dotenv()

# Initialize Appwrite client
def get_storage_image(image_id):
    bucket_id = os.getenv("BUCKET_ID")
    file_url = f"https://cloud.appwrite.io/v1/storage/buckets/{bucket_id}/files/{image_id}/view?project=moviles"
    storage_response = requests.get(file_url, stream=True)
    temp_image_path = "temp_image.jpg"
    with open(temp_image_path, "wb") as f:
        for chunk in storage_response.iter_content(chunk_size=8192):
            f.write(chunk)

    return temp_image_path