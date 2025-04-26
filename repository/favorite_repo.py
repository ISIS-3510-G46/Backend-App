from fastapi import HTTPException
from database import supabase
from schemas.favorite import Favorite
import logging

def add_favorite(favorite: Favorite):
    try:
        lower_brand = favorite.brand.lower()

        event_data = {"brand": lower_brand, "latitude": favorite.latitude, "longitude": favorite.longitude}
        supabase.table("favorite_events").insert(event_data).execute()
        existing = supabase.table("favorites").select("*").eq("brand", lower_brand).execute()

        if existing.data and len(existing.data) > 0:
            current_count = existing.data[0]["count"]
            supabase.table("favorites").update({"count": current_count + 1}).eq("brand", lower_brand).execute()
        else:
            supabase.table("favorites").insert({"brand": lower_brand, "count": 1}).execute()

        return {"success": True}

    except Exception as e:
        logging.error(f"Add favorite failed: {e}")
        raise HTTPException(status_code=500, detail=f"Internal Error: {str(e)}")

