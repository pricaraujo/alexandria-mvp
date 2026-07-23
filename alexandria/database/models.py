from datetime import datetime

from database.database import db


# ==========================================================
# User
# ==========================================================

class User(db.Model):

    __tablename__ = "users"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    name = db.Column(
        db.String(100),
        nullable=False
    )

    email = db.Column(
        db.String(120),
        unique=True,
        nullable=False
    )

    xp = db.Column(
        db.Integer,
        default=0
    )

    level = db.Column(
        db.Integer,
        default=1
    )

    streak = db.Column(
        db.Integer,
        default=0
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    children = db.relationship(
        "Child",
        backref="parent",
        lazy=True
    )

    progress = db.relationship(
        "Progress",
        backref="user",
        lazy=True
    )

    badges = db.relationship(
        "UserBadge",
        backref="user",
        lazy=True
    )

    def __repr__(self):

        return f"<User {self.name}>"

# ==========================================================
# Child
# ==========================================================

class Child(db.Model):

    __tablename__ = "children"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id"),
        nullable=False
    )

    name = db.Column(
        db.String(100),
        nullable=False
    )

    birthday = db.Column(
        db.Date,
        nullable=False
    )

    avatar = db.Column(
        db.String(120),
        default="default_child.png"
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    def __repr__(self):

        return f"<Child {self.name}>"

# ==========================================================
# Articles
# ==========================================================

class Article(db.Model):

    __tablename__ = "articles"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    title = db.Column(
        db.String(200),
        nullable=False
    )

    summary = db.Column(
        db.Text
    )

    content = db.Column(
        db.Text
    )

    category = db.Column(
        db.String(80)
    )

    reading_time = db.Column(
        db.Integer,
        default=5
    )

    xp_reward = db.Column(
        db.Integer,
        default=20
    )

    age_min = db.Column(
        db.Integer,
        default=0
    )

    age_max = db.Column(
        db.Integer,
        default=2190
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    def __repr__(self):

        return f"<Article {self.title}>"

# ==========================================================
# Reading Progress
# ==========================================================

class Progress(db.Model):

    __tablename__ = "progress"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id")
    )

    article_id = db.Column(
        db.Integer,
        db.ForeignKey("articles.id")
    )

    completed = db.Column(
        db.Boolean,
        default=False
    )

    xp_earned = db.Column(
        db.Integer,
        default=0
    )

    completed_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    article = db.relationship(
        "Article",
        lazy=True
    )

# ==========================================================
# Badges
# ==========================================================

class Badge(db.Model):

    __tablename__ = "badges"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    name = db.Column(
        db.String(100)
    )

    description = db.Column(
        db.String(250)
    )

    icon = db.Column(
        db.String(50)
    )

    def __repr__(self):

        return f"<Badge {self.name}>"

# ==========================================================
# User Badges
# ==========================================================

class UserBadge(db.Model):

    __tablename__ = "user_badges"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id")
    )

    badge_id = db.Column(
        db.Integer,
        db.ForeignKey("badges.id")
    )

    earned_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    badge = db.relationship(
        "Badge",
        lazy=True
    )

# ==========================================================
# Quiz (Prepared for MVP)
# ==========================================================

class Quiz(db.Model):

    __tablename__ = "quizzes"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    title = db.Column(
        db.String(150)
    )

    category = db.Column(
        db.String(80)
    )

    age_min = db.Column(
        db.Integer,
        default=0
    )

    age_max = db.Column(
        db.Integer,
        default=2190
    )

    xp_reward = db.Column(
        db.Integer,
        default=30
    )

# ==========================================================
# Quiz Attempts
# ==========================================================

class QuizAttempt(db.Model):

    __tablename__ = "quiz_attempts"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id")
    )

    quiz_id = db.Column(
        db.Integer,
        db.ForeignKey("quizzes.id")
    )

    score = db.Column(
        db.Integer,
        default=0
    )

    completed_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

# ==========================================================
# Daily Challenges
# ==========================================================

class DailyChallenge(db.Model):

    __tablename__ = "daily_challenges"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    title = db.Column(
        db.String(150)
    )

    description = db.Column(
        db.Text
    )

    xp_reward = db.Column(
        db.Integer,
        default=25
    )

# ==========================================================
# User Challenge Progress
# ==========================================================

class UserChallenge(db.Model):

    __tablename__ = "user_challenges"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id")
    )

    challenge_id = db.Column(
        db.Integer,
        db.ForeignKey("daily_challenges.id")
    )

    completed = db.Column(
        db.Boolean,
        default=False
    )

    completed_at = db.Column(
        db.DateTime
    )

# ==========================================================
# Future Tables (v2)
# ==========================================================

"""
Prepared for future releases:

- Notifications
- Healthcare Providers
- Organizations
- Favorite Articles
- Child Growth Records
- Vaccination Records
- Parenting Journal
- Community Posts
- AI Conversations
"""
