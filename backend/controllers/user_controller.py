from typing import Type

from flask_restful import reqparse
from flask import request, jsonify, make_response

from models import User
from .abstract_controller import AbstractController


class UserController(AbstractController):
    _parser = reqparse.RequestParser()

    @classmethod
    def get_model(cls) -> Type[User]:
        return User

    @classmethod
    def get_parser(cls) -> reqparse.RequestParser:
        return cls._parser

    @classmethod
    def post(cls):
        data = request.get_json()
        if User.query.filter_by(passport_id=data['passport_id']).first():
            return make_response("User already exists", 400)
        new_user = User(**data)
        new_user._save()
        return jsonify(new_user)
