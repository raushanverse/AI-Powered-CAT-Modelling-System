from flask import request
from schemas.login_schema import LoginSchema
from marshmallow import ValidationError

from services.auth_service import authenticate_user
from utils.response import success_response, error_response
from constants.messages import (
    LOGIN_SUCCESS,
    INVALID_CREDENTIALS
)

login_schema = LoginSchema()


def login():
    data = request.get_json()

    try:
        validated_data = login_schema.load(data)

    except ValidationError as err:
        return error_response(err.messages, 400)

    user = authenticate_user(
        validated_data["email"],
        validated_data["password"]
    )

    if user is None:
        return error_response(
            INVALID_CREDENTIALS,
            401
        )

    return success_response(
        LOGIN_SUCCESS,
        {
            "user_id": user["user_id"],
            "full_name": user["full_name"],
            "email": user["email"],
            "role": user["role"]
        },
        200
    )