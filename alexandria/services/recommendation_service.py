import random
import json

from services.article_service import ArticleService


class RecommendationService:

    @staticmethod
    def daily_tip():

        with open("data/daily_tips.json", encoding="utf8") as f:

            tips = json.load(f)

        return random.choice(tips)

    @staticmethod
    def recommendations(age_days):

        articles = ArticleService.get_articles()

        return [

            article

            for article in articles

            if article["age_min"] <= age_days <= article["age_max"]

        ]