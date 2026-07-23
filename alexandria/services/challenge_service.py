import json
import random


class ChallengeService:

    FILE = "data/challenges.json"

    @classmethod
    def today(cls):

        with open(cls.FILE) as f:

            challenges = json.load(f)

        return random.choice(challenges)
