from datetime import datetime

from database.database import db


class User(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(100))

    email = db.Column(db.String(100))

    xp = db.Column(db.Integer, default=0)

    level = db.Column(db.Integer, default=1)

    streak = db.Column(db.Integer, default=0)


class Child(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))

    name = db.Column(db.String(100))

    birthday = db.Column(db.Date)


class Article(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    title = db.Column(db.String(200))

    summary = db.Column(db.Text)

    category = db.Column(db.String(50))

    age_min = db.Column(db.Integer)

    age_max = db.Column(db.Integer)

    xp_reward = db.Column(db.Integer, default=15)


class Progress(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(db.Integer)

    article_id = db.Column(db.Integer)

    completed = db.Column(db.Boolean, default=False)

    completed_at = db.Column(db.DateTime, default=datetime.utcnow)

class Badge(db.Model):

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    name = db.Column(
        db.String(80)
    )

    description = db.Column(
        db.String(200)
    )

    icon = db.Column(
        db.String(100)
    )


class UserBadge(db.Model):

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    user_id = db.Column(
        db.Integer
    )

    badge_id = db.Column(
        db.Integer
    )

    earned_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )