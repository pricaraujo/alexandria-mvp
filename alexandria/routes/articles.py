from flask import Blueprint
from flask import render_template
from flask import request

from services.article_service import ArticleService

articles_bp = Blueprint(
    "articles",
    __name__
)


@articles_bp.route("/articles")
def articles():

    search = request.args.get("search")

    if search:

        data = ArticleService.search(search)

    else:

        data = ArticleService.get_articles()

    return render_template(

        "articles.html",

        articles=data

    )


@articles_bp.route("/articles/<int:id>")
def article(id):

    article = ArticleService.get_article(id)

    return render_template(

        "article.html",

        article=article

    )