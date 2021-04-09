#!/usr/bin/python3
""" """
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request
from models import storage
from flask_jwt_extended import create_access_token, JWTManager


@app_views.route("/login", methods=["POST"])
def login():
    username = request.json.get("username", None)
    password = request.json.get("password", None)
    if username != "test" or password != "test":
        return jsonify({"msg": "Bad username or password"}), 401

    access_token = create_access_token(identity=username)
    return jsonify(access_token=access_token)
