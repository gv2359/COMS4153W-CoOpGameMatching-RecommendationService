from fastapi import APIRouter

from app.models.recommendation import Recommendation
from app.resources.recommendation_resource import RecommendationResource
from app.services.service_factory import ServiceFactory

router = APIRouter()


@router.get("/recommendation")
async def get_notifications(user_id: str) -> Recommendation:

    # TODO Do lifecycle management for singleton resource
    res = ServiceFactory.get_service("RecommendationResource")
    result = res.get_by_key(user_id)
    return result
