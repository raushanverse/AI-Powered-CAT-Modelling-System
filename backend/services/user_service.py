from repositories.user_repository import (
    get_all_users,
    create_user,
    get_user_by_id
)


def fetch_all_users():
    return get_all_users()


def add_new_user(data):
    # Future:
    # Validation
    # Password Hashing
    # Business Rules

    return create_user(data)


def fetch_user(user_id):
    return get_user_by_id(user_id)