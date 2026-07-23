from flask import Blueprint
from flask import jsonify

from services.challenge_service import ChallengeService
from services.badge_service import BadgeService

game_bp = Blueprint(
    "game",
    __name__
)


@game_bp.route("/api/challenge")
def challenge():

    return jsonify(

        ChallengeService.today()

    )


@game_bp.route("/api/badges")
def badges():

    return jsonify(

        BadgeService.badges()

    )