from fastapi import FastAPI
from routers import post_router, favorite_router
from routers import filter_usage

app = FastAPI()

# Include routes here:
app.include_router(post_router.router, prefix="", tags=["Posts"])
app.include_router(favorite_router.router, prefix="", tags=["favorites"])
app.include_router(filter_usage.router)



@app.get("/")
def home():
    return {"message": "Welcome to the FastAPI + Supabase E-commerce API!"}

# Usar menos workers si tienes poca RAM
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        app, 
        host="0.0.0.0", 
        port=8000,
        workers=1,  # Reducir workers si tienes poca RAM
        access_log=False  # Reducir logs si es necesario
    )