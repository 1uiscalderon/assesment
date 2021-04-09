#!/usr/bin/python3
""" """
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request
from models import storage
from models.order import Order

taxes = 0.19


@app_views.route('/order/<order_id>', methods=['GET'], strict_slashes=False)
def order_by_id():
    """
    Retrieves a list of all User
    """
    all_orders_id = storage.get_cls_id(Order, order_id)
    if all_orders_id:
        list_order = []
        for order in all_orders_id:
            list_order.append(order.to_dict())
        return jsonify(list_order)
    abort(404)


@app_views.route('/orders', methods=['POST'], strict_slashes=False)
def post_order():
    """
    Creates an user
    """
    if not request.get_json():
        abort(400, description="Not a JSON")

    data = request.get_json()
    data["taxes"] = taxes * int(data.get("subtotal"))
    data["total"] = int(data.get("subtotal")) + int(data.get("taxes"))
    instance = Order(**data)
    instance.save()
    return make_response(jsonify(instance.to_dict()), 201)
