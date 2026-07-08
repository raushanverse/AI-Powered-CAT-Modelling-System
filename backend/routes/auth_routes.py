from flask import Blueprint
from controllers.auth_controller import login

auth_bp = Blueprint("auth_bp", __name__)

@auth_bp.route("/login", methods=["POST"])
def user_login():
    return login()