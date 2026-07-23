import json


class BadgeService:

    FILE = "data/badges.json"

    @classmethod
    def badges(cls):

        with open(cls.FILE) as f:

            return json.load(f)