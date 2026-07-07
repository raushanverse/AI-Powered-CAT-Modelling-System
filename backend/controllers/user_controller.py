from flask import jsonify, request
from services.user_service import get_all_users, create_user
from services.user_service import (
    get_all_users,
    create_user,
    get_user_by_id
)


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

def add_user():
    data = request.get_json()

    success = create_user(data)

    if success:
        return jsonify({
            "status": "success",
            "message": "User created successfully"
        }), 201

    return jsonify({
        "status": "error",
        "message": "Failed to create user"
    }), 500

def fetch_user(user_id):
    user = get_user_by_id(user_id)

    if user:
        return jsonify({
            "status": "success",
            "data": user
        }), 200

    return jsonify({
        "status": "error",
        "message": "User not found"
    }), 404