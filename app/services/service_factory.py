import os
from framework.services.service_factory import BaseServiceFactory
import app.resources.recommendation_resource as recommendation_resource
from app.services.DataAccess.RecommendationServiceDataService import RecommendationDataService


# TODO -- Implement this class
class ServiceFactory(BaseServiceFactory):

    def __init__(self):
        super().__init__()

    @classmethod
    def get_service(cls, service_name):
        #
        # TODO -- The terrible, hardcoding and hacking continues.
        #

        context = {
            "host": os.getenv("DB_HOST"),
            "port": int(os.getenv("DB_PORT")),
            "user": os.getenv("DB_USER"),
            "password": os.getenv("DB_PASSWORD"),
        }

        if service_name == 'RecommendationResource':
            result = recommendation_resource.RecommendationResource(config=None)
        elif service_name == 'RecommendationResourceDataService':
            data_service = RecommendationDataService(context=context)
            result = data_service
        else:
            result = None

        return result
