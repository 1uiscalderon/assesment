#!/usr/bin/python3
""" Blueprint for API """
from flask import Blueprint

app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')

from api.v1.views.user import *
from api.v1.views.order import *
from api.v1.views.shipping import *
from api.v1.views.payment import *
from api.v1.views.auth import *
