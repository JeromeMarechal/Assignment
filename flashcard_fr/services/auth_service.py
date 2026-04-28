from werkzeug.security import check_password_hash, generate_password_hash

from models import User
from repositories.user.user_repository import UserRepository


class AuthService:
    @staticmethod
    def login(username: str, password: str) -> tuple[bool, str | User]:
        if not username:
            return False, "must provide a username"

        if not password:
            return False, "must provide a password"

        user = UserRepository.get_user_by_username(username)

        if not user:
            return False, "Username not found"

        if not check_password_hash(user.password_hash, password):
            return False, "Invalid password"

        return True, user

    @staticmethod
    def register(
        username: str,
        email: str,
        native_language: str,
        password: str,
        confirmation_password: str,
    ) -> tuple[bool, str | User]:

        if not username:
            return False, "must provide a username"
        if not email:
            return False, "must provide an email"
        if not native_language:
            return False, "must provide a native language"
        if not password:
            return False, "must provide a password"
        if not confirmation_password:
            return False, "must confirm your password"

        if password != confirmation_password:
            return False, "passwords do not match"

        if UserRepository.user_exists(username):
            return False, "username already exists"

        if UserRepository.user_email_exists(email):
            return False, "email already exists"

        password_hash = generate_password_hash(password)

        success, result = UserRepository.createUser(
            username, email, native_language, password_hash
        )

        if not success:
            return False, result

        return True, result
