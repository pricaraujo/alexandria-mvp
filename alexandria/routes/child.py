from flask import Blueprint
from flask import render_template

from services.child_service import ChildService

child_bp = Blueprint(
    "child",
    __name__
)


@child_bp.route("/child")
def child():

    # Prototype:
    # later replace with logged user

    child = ChildService.get_child(1)

    return render_template(

        "child.html",

        child=child

    )