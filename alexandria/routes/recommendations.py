from flask import Blueprint
from flask import jsonify

from services.recommendation_service import RecommendationService

recommendations_bp = Blueprint(
    "recommendations",
    __name__
)


@recommendations_bp.route("/api/daily-tip")
def daily_tip():

    return jsonify(

        RecommendationService.daily_tip()

    )