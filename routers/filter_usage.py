# api/routes/filter_usage.py
from fastapi import APIRouter
from schemas.filter_usage import FilterUsage
from services.filter_usage_service import register_filter_usage

router = APIRouter()


@router.post("/filter_usage")
async def create_usage(evt: FilterUsage):
    return register_filter_usage(evt)
