"""
imports
"""
import logging

# external imports
from flask import Flask
from flask_restful import Resource, Api

# app level imports
from .settings import *
from .resources import GitProfile


def create_app(config_name):
    app = Flask(__name__)

    app.config.from_object(config_name)

    api = Api(app)
    api.add_resource(GitProfile, '/repos/<string:organization>')

    return app

