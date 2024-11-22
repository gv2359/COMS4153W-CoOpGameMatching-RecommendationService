from framework.services.service_factory import BaseServiceFactory
import app.resources.recommendation_resource as notification_resource
from framework.services.data_access.MySQLRDBDataService import MySQLRDBDataService


# TODO -- Implement this class
class ServiceFactory(BaseServiceFactory):

    def __init__(self):
        super().__init__()

    @classmethod
    def get_service(cls, service_name):
        #
        # TODO -- The terrible, hardcoding and hacking continues.
        #
        if service_name == 'RecommendationResource':
            result = notification_resource.RecommendationResource(config=None)
        elif service_name == 'RecommendationResourceDataService':
            context = dict(user="root", password="dbpassuser",
                           host="w4153.cl9cloxvh1sk.us-east-1.rds.amazonaws.com", port=3306)
            data_service = MySQLRDBDataService(context=context)
            result = data_service
        else:
            result = None

        return result
