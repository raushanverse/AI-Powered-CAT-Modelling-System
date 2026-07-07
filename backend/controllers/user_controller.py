from flask import jsonify
from services.user_service import get_all_users


def fetch_users():
    users = get_all_users()

    if users is None:
        return jsonify({
            "status": "error",
            "message": "Database Connection Failed"
        }), 500

    return jsonify({
        "status": "success",
        "count": len(users),
        "data": users
    }), 200