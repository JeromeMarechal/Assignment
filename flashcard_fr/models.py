import uuid

from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

user_cards = db.Table(
    "user_cards",
    db.Column("user_id", db.Integer, db.ForeignKey("user.id"), primary_key=True),
    db.Column("card_id", db.Integer, db.ForeignKey("card.id"), primary_key=True),
)


class User(UserMixin, db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    native_language = db.Column(db.String(50), nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    cards = db.relationship(
        "Card",
        secondary=user_cards,
        back_populates="users",
    )

    def __repr__(self):
        return f"<User {self.username}>"


class Card(db.Model):
    __tablename__ = "card"
    id = db.Column(db.Integer, primary_key=True)
    lang = db.Column(db.String(), nullable=False)
    word_fr = db.Column(db.String(100), nullable=False)
    word_lang = db.Column(db.String(100), nullable=False)
    definition = db.Column(db.Text, nullable=False)
    pos = db.Column(db.String(50), nullable=False)
    synonyms = db.Column(db.Text, nullable=False)
    example = db.Column(db.Text, nullable=False)
    example_translated = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.now())
    users = db.relationship(
        "User",
        secondary=user_cards,
        back_populates="cards",
    )

    def __repr__(self):
        return f"<Card {self.word_fr}/{self.word_lang} [{self.lang}]>"


class Meaning(db.Model):
    __tablename__ = "meaning"
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    user_id = db.Column(
        db.Integer, db.ForeignKey("user.id"), unique=True, nullable=False
    )
    current_word = db.Column(db.String(100), nullable=False)
    correct_answer = db.Column(db.String(100), nullable=False)
    choices = db.Column(db.Text, nullable=False)
    round = db.Column(db.Integer, default=1, nullable=False)
    score = db.Column(db.Integer, default=0, nullable=False)
    attempts = db.Column(db.Integer, default=0, nullable=False)
    all_time_score = db.Column(db.Integer, default=0, nullable=False)
