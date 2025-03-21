from repository.post_repo import create_post, get_posts, get_posts_by_categ, get_post_id
from schemas.post import PostCreate

def register_post(post: PostCreate): #Validations?
    return create_post(post)


def get_all_posts(): 
    return get_posts()


def get_posts_by_category(category_name):
    return get_posts_by_categ(category_name)

def get_post_by_id(id):
    return get_post_id(id)
