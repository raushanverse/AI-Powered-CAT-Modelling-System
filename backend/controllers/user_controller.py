from flask import jsonify, request
from utils.response import success_response, error_response
from constants.messages import (
    EMAIL_ALREADY_EXISTS,
    EMPLOYEE_ALREADY_EXISTS,
    USER_CREATED,
    USER_FETCHED,
    USER_FOUND,
    USER_NOT_FOUND,
    DATABASE_CONNECTION_ERROR
)
from marshmallow import ValidationError
from schemas.user_schema import UserSchema
EMAIL_ALREADY_EXISTS,
EMPLOYEE_ALREADY_EXISTS

from services.user_service import (
    email_exists,
    employee_exists,
    fetch_all_users,
    add_new_user,
    fetch_user_by_id
)



user_schema = UserSchema()


def fetch_users():
    users = fetch_all_users()

    if users is None:
        return error_response(
            DATABASE_CONNECTION_ERROR,
            500
        )

    return success_response(
        USER_FETCHED,
        users,
        200
    )


def add_user():
    data = request.get_json()

    try:
        validated_data = user_schema.load(data)

    except ValidationError as err:
        return error_response(err.messages, 400)

    if email_exists(validated_data["email"]):
        return error_response(
            EMAIL_ALREADY_EXISTS,
            409
        )

    if employee_exists(validated_data["employee_id"]):
        return error_response(
            EMPLOYEE_ALREADY_EXISTS,
            409
        )

    success = add_new_user(validated_data)

    if success:
        return success_response(
            USER_CREATED,
            None,
            201
        )

    return error_response(
        DATABASE_CONNECTION_ERROR,
        500
    )

def fetch_user(user_id):
    user = fetch_user_by_id(user_id)

    if user:
        return success_response(
            USER_FOUND,
            user,
            200
        )

    return error_response(
        USER_NOT_FOUND,
        404
    )