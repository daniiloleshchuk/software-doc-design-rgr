import datetime
from typing import Type

from flask_restful import reqparse

from flask import request, jsonify, make_response, Response
from models import Election, ElectionType
from .abstract_controller import AbstractController


class ElectionController(AbstractController):
    _parser = reqparse.RequestParser()
    _parser.add_argument('days_duration', type=int, required=False)
    _parser.add_argument('type_pk', type=int, required=False)

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

    @classmethod
    def put(cls):
        return Response(status=405)

