from datetime import date


class StreakService:

    @staticmethod
    def update(user):

        user.streak += 1

        return user.streak