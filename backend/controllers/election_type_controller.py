from typing import Type

from flask import Response
from flask_restful import reqparse

from models import ElectionType
from .abstract_controller import AbstractController


class ElectionTypeController(AbstractController):
    _parser = reqparse.RequestParser()
    _parser.add_argument('age_from', type=int, required=False)
    _parser.add_argument('age_to', type=int, required=False)
    _parser.add_argument('organization_members_only', type=bool, required=False)
    _parser.add_argument('regions_allowed_pks', type=int, action='append', required=False)
    _parser.add_argument('voter_votes_count', type=int, required=False)
    _parser.add_argument('votes_cancelable', type=int, required=False)


    @classmethod
    def get_model(cls) -> Type[ElectionType]:
        return ElectionType

    @classmethod
    def get_parser(cls) -> reqparse.RequestParser:
        return cls._parser

    @classmethod
    def put(cls):
        return Response(status=405)
