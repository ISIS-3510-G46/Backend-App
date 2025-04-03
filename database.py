import os
from dotenv import load_dotenv
from supabase import create_client, Client

# Load environment variables from .env
load_dotenv()
url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")


# Create a Supabase client
supabase: Client = create_client(url, key)


# Check connection -> Should return the posts
response = supabase.table("Post").select("*").execute()
existing_posts = supabase.table("Post").select("id").execute()
print("Supabase Connected, query test:", response)
print("Refreshing ids:", existing_posts)

