"""
imports
"""
import logging

# external imports
from flask import Flask, Blueprint
from flask_restful import Resource, Api


bp = Blueprint('api', __name__, url_prefix='/api/v1')
api = Api(bp)

def create_app(config_name):
    from . import resources
    app = Flask(__name__)

    app.config.from_object(config_name)

    app.register_blueprint(bp)

    return app

