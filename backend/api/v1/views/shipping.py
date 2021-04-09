#!/usr/bin/python3
""" """
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request
from models import storage
from models.shipping import Shipping


@app_views.route('/shipping', methods=['POST'], strict_slashes=False)
def post_shipping():
    """
    Creates shipping
    """
    if not request.get_json():
        abort(400, description="Not a JSON")

    data = request.get_json()
    instance = Shipping(**data)
    instance.save()
    return make_response(jsonify(instance.to_dict()), 201)
