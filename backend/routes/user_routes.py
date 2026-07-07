from flask import Blueprint
from controllers.user_controller import fetch_users, add_user
from controllers.user_controller import (
    fetch_users,
    add_user,
    fetch_user
)

user_bp = Blueprint("user_bp", __name__)

@user_bp.route("/users", methods=["GET"])
def get_users():
    return fetch_users()

@user_bp.route("/users", methods=["POST"])
def create_new_user():
    return add_user()

@user_bp.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    return fetch_user(user_id)