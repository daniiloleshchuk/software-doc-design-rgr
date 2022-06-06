from typing import Type

from flask_restful import reqparse

from models import ElectionType
from .abstract_controller import AbstractController


class ElectionTypeController(AbstractController):
    _parser = reqparse.RequestParser()

    @classmethod
    def get_model(cls) -> Type[ElectionType]:
        return ElectionType

    @classmethod
    def get_parser(cls) -> reqparse.RequestParser:
        return cls._parser
