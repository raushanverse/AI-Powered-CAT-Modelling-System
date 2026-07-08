from constants.messages import (
    EMAIL_ALREADY_EXISTS,
    EMPLOYEE_ALREADY_EXISTS
)
from repositories.user_repository import (
    get_all_users,
    create_user,
    get_user_by_id
)
from repositories.user_repository import (
    get_user_by_email,
    get_user_by_employee_id
)
EMAIL_ALREADY_EXISTS,
EMPLOYEE_ALREADY_EXISTS
from utils.password import hash_password

def email_exists(email):
    return get_user_by_email(email)


def employee_exists(employee_id):
    return get_user_by_employee_id(employee_id)

def fetch_all_users():
    """
    Business Logic:
    Fetch all users
    """

    return get_all_users()


def add_new_user(data):
    print("BEFORE HASH:", data["password"])

    data["password"] = hash_password(data["password"])

    print("AFTER HASH:", data["password"])

    return create_user(data)


def fetch_user_by_id(user_id):
    """
    Business Logic:
    Fetch User By ID
    """

    return get_user_by_id(user_id)