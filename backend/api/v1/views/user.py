#!/usr/bin/python3
""" """
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request
from models import storage
from models.user import User


@app_views.route('/users/all', methods=['GET'], strict_slashes=False)
def users():
    """
    Retrieves a list of all User
    """
    all_users = storage.get(User)
    list_users = []
    for user in all_users:
        list_users.append(user.to_dict())
    return jsonify(list_users)


@app_views.route('/user', methods=['POST'], strict_slashes=False)
def post_user():
    """
    Creates an user
    """
    if not request.get_json():
        abort(400, description="Not a JSON")

    data = request.get_json()
    instance = User(**data)
    instance.save()
    return make_response(jsonify(instance.to_dict()), 201)
