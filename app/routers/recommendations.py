from fastapi import APIRouter, Query, HTTPException, BackgroundTasks
from fastapi.openapi.models import Response
from fastapi.responses import JSONResponse

from app.models.recommendations import Recommendations
from app.models.user_activity import UserActivity
from app.resources.recommendation_resource import RecommendationResource
from app.services.service_factory import ServiceFactory

router = APIRouter()


@router.get("/recommendations/{user_id}", response_model=Recommendations)
async def get_recommendations(user_id: str, num_recoms: int = Query(5, ge=1)) -> Recommendations:
    try:
        res = ServiceFactory.get_service("RecommendationResource")
        recoms = res.get_recoms(user_id, num_recoms)

        if not recoms:
            raise HTTPException(status_code=404, detail="No games")

        print(f"Fetched recommendations for user_id {user_id}: {recoms}")
        return recoms

    except Exception as e:
        raise HTTPException(status_code=500, detail="An error occurred while fetching the game.")

@router.post("/user_activity", status_code=202)
async def update_activity(user_activity: UserActivity):
    try:

        res = ServiceFactory.get_service("RecommendationResource")

        #background_tasks.add_task(res.update_recoms, user_activity)

        response = JSONResponse(
            content=user_activity.dict(),
            status_code=202
        )

        return response

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))