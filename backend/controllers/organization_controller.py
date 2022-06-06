from typing import Type

from flask_restful import reqparse

from models import Organization
from .abstract_controller import AbstractController


class OrganizationController(AbstractController):
    _parser = reqparse.RequestParser()

    @classmethod
    def get_model(cls) -> Type[Organization]:
        return Organization

    @classmethod
    def get_parser(cls) -> reqparse.RequestParser:
        return cls._parser
