from PIL import Image
import os
from storage import upload_image

def generate_thumbnail(image, size=(200, 200)):
    img_file = Image.open(image)
    img_copy = img_file.copy()
    img_copy.thumbnail(size, Image.LANCZOS)
    img_stored_id = upload_to_storage(img_copy)
    os.remove(image)
    return img_stored_id


def upload_to_storage(image):
    # Upload image to appwrite storage
    img_stored_id = upload_image(image)
    return img_stored_id
