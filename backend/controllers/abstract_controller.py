from abc import abstractmethod
from typing import Type

from flask import jsonify
from flask_restful import Resource, request, reqparse

from models.abstract_model import AbstractModel


class AbstractController(Resource):
    __abstract__ = True

    @classmethod
    @abstractmethod
    def get_model(cls) -> Type[AbstractModel]:
        raise NotImplementedError

    @classmethod
    @abstractmethod
    def get_parser(cls) -> reqparse.RequestParser:
        raise NotImplementedError

    def get(self):
        url_args = request.args
        pk = url_args.get('pk')
        if pk:
            return jsonify(self.get_model()._get_by_pk(pk=pk))
        else:
            return jsonify(self.get_model()._get_all())

    def post(self):
        request_data = self.get_parser().parse_args()
        obj = self.get_model()(**request_data)
        obj._save()
        return jsonify(obj)

    def put(self):
        url_args = request.args
        request_data = self.get_parser().parse_args()
        obj = self.get_model()._get_by_pk(pk=url_args.get('pk'))
        obj._save()
        if obj:
            for k, v in request_data.items():
                if v and hasattr(obj, k):
                    setattr(obj, k, v)
        else:
            obj = self.get_model()(**request_data)
        obj._save()
        return jsonify(obj), 200

    def delete(self):
        url_args = request.args
        obj = self.get_model()._get_by_pk(pk=url_args.get('pk'))
        if obj:
            obj._delete()
        return {'msg': 'deleted'}, 200
