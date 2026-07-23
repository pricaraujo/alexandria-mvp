from flask import Blueprint
from flask import render_template

onboarding_bp = Blueprint(
    "onboarding",
    __name__
)


@onboarding_bp.route("/onboarding")
def onboarding():

    return render_template(
        "onboarding.html"
    )