from flask import Blueprint
from flask import render_template

from services.child_service import ChildService
from services.milestone_service import MilestoneService

milestones_bp = Blueprint(
    "milestones",
    __name__
)


@milestones_bp.route("/milestones")
def milestones():

    child = ChildService.get_child(1)

    recommended = MilestoneService.recommended(
        child["age_days"]
    )

    upcoming = MilestoneService.upcoming(
        child["age_days"]
    )

    return render_template(

        "milestones.html",

        child=child,

        recommended=recommended,

        upcoming=upcoming

    )