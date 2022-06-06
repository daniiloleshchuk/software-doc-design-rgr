import json

from typing import Type
from flask import request, jsonify
from flask_restful import reqparse

from models import Vote
from .abstract_controller import AbstractController
from services.vote_service import VoteService
from backend.logic.filters import FilterException


class VoteController(AbstractController):
    _parser = reqparse.RequestParser()

    @classmethod
    def get_model(cls) -> Type[Vote]:
        return Vote

    @classmethod
    def get_parser(cls) -> reqparse.RequestParser:
        return cls._parser

    @classmethod
    def post(cls) -> reqparse.RequestParser:
        data = json.dumps(request.data)
        vote_service = VoteService(data['election_id'])
        try:
            registered_vote = vote_service.register_vote(**data)
        except FilterException as err:
            return jsonify(str(err)), 400
        
        return jsonify(registered_vote)
