from database import supabase
from schemas.post import PostCreate
from dotenv import load_dotenv
from appwrite.client import Client
from appwrite.services.storage import Storage
from appwrite.id import ID
from appwrite.input_file import InputFile
import io
import os
import requests


load_dotenv()
bucket_id = os.getenv("BUCKET_ID")
storage_key = os.getenv("STORAGE_KEY")

# Initialize Appwrite client
def get_storage_image(image_id):
    file_url = f"https://cloud.appwrite.io/v1/storage/buckets/{bucket_id}/files/{image_id}/view?project=moviles"
    storage_response = requests.get(file_url, stream=True)
    temp_image_path = "temp_image.jpg"
    with open(temp_image_path, "wb") as f:
        for chunk in storage_response.iter_content(chunk_size=8192):
            f.write(chunk)

    return temp_image_path

# Taken from appwrite docs
def upload_image(image, file_name=None):
    client = Client()

    (client
    .set_endpoint('https://cloud.appwrite.io/v1')
    .set_project('moviles') 
    .set_key(storage_key) 
    )
    
    storage = Storage(client)
    img_id=ID.unique()
    temp_image_path = "temp_image.jpg"
    
    result = storage.create_file(
        bucket_id = bucket_id,
        file_id = img_id,
        file = InputFile.from_path(temp_image_path)
        )

    return result["$id"]