import json


class ArticleService:

    FILE = "data/articles.json"

    @classmethod
    def get_articles(cls):

        with open(cls.FILE, encoding="utf8") as f:

            return json.load(f)

    @classmethod
    def get_article(cls, article_id):

        articles = cls.get_articles()

        for article in articles:

            if article["id"] == article_id:

                return article

        return None

    @classmethod
    def search(cls, query):

        query = query.lower()

        return [

            article

            for article in cls.get_articles()

            if query in article["title"].lower()

            or query in article["category"].lower()

        ]