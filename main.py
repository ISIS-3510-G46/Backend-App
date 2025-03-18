from fastapi import FastAPI
from routers import post_router

app = FastAPI()

# Include routes here:
app.include_router(post_router.router, prefix="", tags=["Posts"])



@app.get("/")
def home():
    return {"message": "Welcome to the FastAPI + Supabase E-commerce API!"}
