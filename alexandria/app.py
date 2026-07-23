from flask import Flask

from config import Config

from database.database import db

# ==========================
# Initialize Flask
# ==========================

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

# ==========================
# Database Models
# ==========================

from database.models import (
    User,
    Child,
    Article,
    Progress,
    Badge,
    UserBadge
)

# ==========================
# Blueprints
# ==========================

from routes.home import home_bp
from routes.dashboard import dashboard_bp
from routes.onboarding import onboarding_bp
from routes.articles import articles_bp
from routes.child import child_bp
from routes.milestones import milestones_bp
from routes.game import game_bp

# Optional (coming later)
# from routes.quiz import quiz_bp
# from routes.profile import profile_bp

# ==========================
# Register Blueprints
# ==========================

app.register_blueprint(home_bp)

app.register_blueprint(onboarding_bp)

app.register_blueprint(dashboard_bp)

app.register_blueprint(articles_bp)

app.register_blueprint(child_bp)

app.register_blueprint(milestones_bp)

app.register_blueprint(game_bp)

# app.register_blueprint(quiz_bp)
# app.register_blueprint(profile_bp)

# ==========================
# Create Database
# ==========================

with app.app_context():

    db.create_all()

# ==========================
# Seed Development Data
# ==========================

def create_demo_user():

    """
    Creates a demo user so the prototype
    works without authentication.
    """

    if User.query.first():

        return

    from datetime import date

    user = User(

        name="Emily Smith",

        email="demo@alexandria.app",

        xp=120,

        level=2,

        streak=3

    )

    db.session.add(user)

    db.session.commit()

    child = Child(

        user_id=user.id,

        name="Oliver",

        birthday=date(2025, 12, 20)

    )

    db.session.add(child)

    db.session.commit()


with app.app_context():

    create_demo_user()

# ==========================
# Context Processor
# Makes navigation available
# ==========================

@app.context_processor
def global_context():

    return {

        "app_name": "Alexandria"

    }

# ==========================
# Error Pages
# ==========================

@app.errorhandler(404)
def page_not_found(error):

    return (

        "<h1>404</h1><p>Page not found.</p>",

        404

    )


@app.errorhandler(500)
def internal_error(error):

    db.session.rollback()

    return (

        "<h1>500</h1><p>Internal server error.</p>",

        500

    )

# ==========================
# Health Check
# ==========================

@app.route("/health")
def health():

    return {

        "status": "ok",

        "app": "Alexandria MVP"

    }

# ==========================
# Run
# ==========================

if __name__ == "__main__":

    app.run(

        debug=True,

        host="0.0.0.0",

        port=5000

    )
