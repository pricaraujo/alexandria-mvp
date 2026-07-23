import json


class MilestoneService:

    FILE = "data/milestones.json"

    @classmethod
    def get_all(cls):

        with open(cls.FILE, encoding="utf8") as f:

            return json.load(f)

    @classmethod
    def recommended(cls, age_days):

        milestones = cls.get_all()

        return [

            milestone

            for milestone in milestones

            if milestone["age_min"] <= age_days <= milestone["age_max"]

        ]

    @classmethod
    def upcoming(cls, age_days):

        milestones = cls.get_all()

        return [

            milestone

            for milestone in milestones

            if milestone["age_min"] > age_days

        ][:5]