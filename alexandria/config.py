import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))


class Config:

    SECRET_KEY = "alexandria-mvp"

    SQLALCHEMY_DATABASE_URI = (
        "sqlite:///" +
        os.path.join(BASE_DIR, "alexandria.db")
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False