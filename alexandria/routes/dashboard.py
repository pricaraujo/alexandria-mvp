from flask import Blueprint
from flask import render_template

from database.models import User

from services.child_service import ChildService
from services.article_service import ArticleService
from services.milestone_service import MilestoneService

dashboard_bp = Blueprint(
    "dashboard",
    __name__
)


@dashboard_bp.route("/dashboard")
def dashboard():

    user = User.query.first()

    child = ChildService.get_child(user.id)

    articles = ArticleService.get_articles()

    recommended = MilestoneService.recommended(
        child["age_days"]
    )

    progress = min(
        (user.xp % 100),
        100
    )

    return render_template(

        "dashboard.html",

        user=user,

        child=child,

        articles=articles,

        recommended=recommended,

        progress=progress

    )
