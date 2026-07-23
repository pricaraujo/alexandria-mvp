from database.models import Child

from utils.age import age_in_days
from utils.age import age_text


class ChildService:

    @staticmethod
    def get_child(user_id):

        child = Child.query.filter_by(
            user_id=user_id
        ).first()

        if child:

            return {

                "id": child.id,

                "name": child.name,

                "birthday": child.birthday,

                "age_days": age_in_days(child.birthday),

                "age": age_text(child.birthday)

            }

        return None