from typing import Any

from framework.resources.base_resource import BaseResource

from app.models.recommendation import Recommendation
from app.services.service_factory import ServiceFactory


class RecommendationResource(BaseResource):

    def __init__(self, config):
        super().__init__(config)

        self.data_service = ServiceFactory.get_service("RecommendationResourceDataService")
        self.database = "recommendations"
        self.collection = "recommendation_info"
        self.key_field = "user_id"

    def get_by_key(self, game_id) -> Recommendation:

        d_service = self.data_service

        result = d_service.get_data_object(self.database, self.collection, self.key_field, key_value = game_id)
        print(result)

        result = Recommendation(**result)
        return result


