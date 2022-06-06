from typing import Type

from flask_restful import reqparse

from models import Vote
from .abstract_controller import AbstractController


class VoteController(AbstractController):
    _parser = reqparse.RequestParser()

    @classmethod
    def get_model(cls) -> Type[Vote]:
        return Vote

    @classmethod
    def get_parser(cls) -> reqparse.RequestParser:
        return cls._parser
