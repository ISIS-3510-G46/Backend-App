from fastapi import FastAPI
from routers import post_router, favorite_router

app = FastAPI()

# Include routes here:
app.include_router(post_router.router, prefix="", tags=["Posts"])
app.include_router(favorite_router.router, prefix="", tags=["favorites"])



@app.get("/")
def home():
    return {"message": "Welcome to the FastAPI + Supabase E-commerce API!"}
