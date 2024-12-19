from typing import Any

from framework.resources.base_resource import BaseResource

from app.models.recommendations import Recommendations
from app.models.game import Game
from app.services.service_factory import ServiceFactory


from typing import List
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import random

class RecommendationResource(BaseResource):

    def __init__(self, config):
        super().__init__(config)
        self.data_service = ServiceFactory.get_service("RecommendationResourceDataService")
        self.database = "Game"
        self.collection = "games_info"
        self.key_field = "gameId"
        self.data_service.initialize(self.database)

    def get_recoms(self, user_id, num_recoms) -> Recommendations:
        user_favorites = self.data_service.get_user_favorites(user_id)
        if not user_favorites:
            return self.get_random_recommendations(num_recoms)
        
        all_games = self.data_service.get_all_games()
        recommendations = self.compute_recommendations(user_favorites, all_games, num_recoms)
        return recommendations

    def get_random_recommendations(self, num_recoms) -> Recommendations:
        all_games = self.data_service.get_all_games()
        random_games = random.sample(all_games, num_recoms)
        return Recommendations(userId=user_id, games=random_games)

    def compute_recommendations(self, user_favorites: List[Game], all_games: List[Game], num_recoms: int) -> Recommendations:
        favorite_descriptions = [game.description for game in user_favorites]
        all_descriptions = [game.description for game in all_games]

        vectorizer = TfidfVectorizer()
        tfidf_matrix = vectorizer.fit_transform(favorite_descriptions + all_descriptions)

        favorite_matrix = tfidf_matrix[:len(favorite_descriptions)]
        all_matrix = tfidf_matrix[len(favorite_descriptions):]

        similarity_scores = cosine_similarity(favorite_matrix, all_matrix)
        avg_similarity_scores = similarity_scores.mean(axis=0)

        top_indices = avg_similarity_scores.argsort()[-num_recoms:][::-1]
        recommended_games = [all_games[i] for i in top_indices]

        return Recommendations(userId=user_id, games=recommended_games)


