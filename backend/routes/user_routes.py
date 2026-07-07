from flask import Blueprint
from controllers.user_controller import fetch_users

user_bp = Blueprint("user_bp", __name__)

@user_bp.route("/users", methods=["GET"])
def get_users():
    return fetch_users()