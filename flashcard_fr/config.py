import os

from dotenv import load_dotenv

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
load_dotenv()


class Config:
    # Secret key for session management (override in production via env var)
    SECRET_KEY = os.getenv("SECRET_KEY", "dev-secret-key")

    # Database connection URI; defaults to a local SQLite file
    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DATABASE_URI", f"sqlite:///{os.path.join(BASE_DIR, 'flashcards.db')}"
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False
