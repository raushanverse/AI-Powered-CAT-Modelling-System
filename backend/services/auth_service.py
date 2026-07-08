from repositories.user_repository import get_user_by_email
from utils.password import verify_password


def authenticate_user(email, password):
    user = get_user_by_email(email)

    if user is None:
        return None

    if not verify_password(password, user["password"]):
        return None

    return user