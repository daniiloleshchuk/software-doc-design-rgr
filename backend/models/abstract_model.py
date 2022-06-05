from abc import abstractmethod
from app import db


class AbstractModel(db.Model):
    __abstract__ = True

    @classmethod
    def get_by_pk(cls, pk):
        return cls.query.filter_by(pk=pk).first()

    @classmethod
    def get_all(cls):
        return cls.query.all()

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
