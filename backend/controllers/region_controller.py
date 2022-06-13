from typing import Type

from flask_restful import reqparse

from models import Region
from .abstract_controller import AbstractController


class RegionController(AbstractController):
    _parser = reqparse.RequestParser()
    _parser.add_argument('name', type=str, required=False)

    @classmethod
    def get_model(cls) -> Type[Region]:
        return Region

    @classmethod
    def get_parser(cls) -> reqparse.RequestParser:
        return cls._parser
