from typing import Any

from framework.resources.base_resource import BaseResource

from app.models.recommendations import Recommendations
from app.models.game import Game
from app.services.service_factory import ServiceFactory


class RecommendationResource(BaseResource):

    def __init__(self, config):
        super().__init__(config)

        self.data_service = ServiceFactory.get_service("RecommendationResourceDataService")
        self.database = "Games"
        self.collection = "games_info"
        self.key_field = "gameId"

        self.data_service.initialize(self.database)

    def get_recoms(self, user_id, num_recoms) -> Recommendations:

        d_service = self.data_service

        result = d_service.get_recommendations(user_id, num_recoms)

        recommendations = self.populate_recommendations(result, user_id)
        return recommendations

    @staticmethod
    def populate_recommendations(result, user_id):

        recommendations = []

        for row in result:
            game_model = Game(
                gameId=row['gameId'],
                title=row['title'],
                description=row['description'],
                image=row['image'],
                links={
                    "self": {"href": f"/games/{row['gameId']}"},
                    "image": {"href": row['image'] or "No image available"}
                }
            )
            print(game_model)
            recommendations.append(game_model)

        response_model = Recommendations(userId = user_id, games = recommendations)

        return response_model



