from typing import Type

from flask_restful import reqparse

from flask import request, jsonify, make_response
from models import Election
from .abstract_controller import AbstractController


class ElectionController(AbstractController):
    _parser = reqparse.RequestParser()

    @classmethod
    def get_model(cls) -> Type[Election]:
        return Election

    @classmethod
    def get_parser(cls) -> reqparse.RequestParser:
        return cls._parser

    @classmethod
    def post(cls):
        data = request.get_json()
        election = Election(**data)
        election._save()
        return jsonify(election)
