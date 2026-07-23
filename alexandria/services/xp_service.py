class XPService:

    LEVELS = [

        0,
        100,
        250,
        450,
        700,
        1000,
        1400,
        1800,
        2400,
        3000

    ]

    @classmethod
    def add_xp(cls, user, value):

        user.xp += value

        level = 1

        for minimum in cls.LEVELS:

            if user.xp >= minimum:

                level += 1

        user.level = level

        return {

            "xp":user.xp,

            "level":user.level

        }

    @classmethod
    def next_level(cls, user):

        for minimum in cls.LEVELS:

            if minimum > user.xp:

                return minimum

        return cls.LEVELS[-1]