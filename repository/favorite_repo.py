from fastapi import HTTPException
from database import supabase
from schemas.favorite import Favorite


def add_favorite(favorite: Favorite):
    try:
        lower_brand = favorite.brand.lower()
        
        response = supabase.table("Favorite").select("*").eq("brand", lower_brand).execute()

        if response.data and len(response.data) > 0:
                existing_favorite = response.data[0]
                current_count = existing_favorite["count"]
                
                update_response = supabase.table("Favorite").update({"count": current_count + 1}).eq(
                     "id", existing_favorite["id"]).execute()
                
                return {"success": True, "msg": update_response}
        else:
            insert_response = supabase.table("Favorite").insert({
                 "brand": lower_brand, 
                 "count": 1
                 }).execute()
            
            return {"success": True, "msg": insert_response}
                
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
