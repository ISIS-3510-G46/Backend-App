from fastapi import HTTPException
from database import supabase  # mismo helper que Favoritos
from schemas.filter_usage import FilterUsage
import logging


def add_filter_usage(evt: FilterUsage):
    """
    Guarda la aplicación de un filtro:
      1) inserta evento crudo en tabla `filter_usage_events`
      2) incrementa contador por (filter_type, filter_value) en `filter_usage`
    """
    try:
        # 1. tabla eventos crudos (cada clic)
        supabase.table("filter_usage_events").insert(
            {
                "filter_type": evt.filter_type.lower(),
                "filter_value": evt.filter_value.lower(),
                "latitude": evt.latitude,
                "longitude": evt.longitude,
            }
        ).execute()

        # 2. contador acumulado
        existing = (
            supabase.table("filter_usage")
            .select("*")
            .eq("filter_type", evt.filter_type.lower())
            .eq("filter_value", evt.filter_value.lower())
            .execute()
        )

        if existing.data:
            current = existing.data[0]["count"]
            supabase.table("filter_usage").update({"count": current + 1}).eq(
                "filter_type", evt.filter_type.lower()
            ).eq("filter_value", evt.filter_value.lower()).execute()
        else:
            supabase.table("filter_usage").insert(
                {
                    "filter_type": evt.filter_type.lower(),
                    "filter_value": evt.filter_value.lower(),
                    "count": 1,
                }
            ).execute()

        return {"success": True}

    except Exception as e:
        logging.error(f"Add filter usage failed: {e}")
        raise HTTPException(status_code=500, detail="Internal Error")
