from flask import Flask

from config import Config

from database.database import db

app = Flask(__name__)

app.config.from_object(Config)

db.init_app(app)

from database.models import *

with app.app_context():
    db.create_all()

from routes.home import home_bp
from routes.dashboard import dashboard_bp
from routes.onboarding import onboarding_bp

app.register_blueprint(home_bp)
app.register_blueprint(dashboard_bp)
app.register_blueprint(onboarding_bp)

if __name__ == "__main__":
    app.run(debug=True)