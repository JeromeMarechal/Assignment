from typing import Tuple, Union, Optional
from models import db, User
from sqlalchemy.exc import IntegrityError


class UserRepository:
    @staticmethod
    def get_user_by_username(username: str) -> Optional[User]:
        user: Optional[User] = User.query.filter_by(username=username).first()
        return user

    @staticmethod
    def user_exists(username: str) -> bool:
        return User.query.filter_by(username=username).first() is not None

    @staticmethod
    def user_email_exists(email: str) -> bool:
        return User.query.filter_by(email=email).first() is not None

    @staticmethod
    def createUser(username: str, email: str, native_language: str, password_hash: str) -> Tuple[bool, Union[User, str]]:
        user: User = User(
            username=username,
            email=email,
            native_language=native_language,
            password_hash=password_hash,
        )

        try:
            db.session.add(user)
            db.session.commit()
        except IntegrityError:
            db.session.rollback()
            return False, "username or email already exists"
        return True, user
