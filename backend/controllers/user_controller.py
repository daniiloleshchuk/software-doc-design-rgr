from typing import Type

from flask_restful import reqparse

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
