from __future__ import annotations

from typing import List

from app import db


class AbstractModel(db.Model):
    __abstract__ = True

    @classmethod
    def _get_by_pk(cls, pk) -> AbstractModel:
        return cls.query.filter_by(pk=pk).first()

    @classmethod
    def _get_all(cls) -> List[AbstractModel]:
        return cls.query.all()

    def _save(self) -> None:
        db.session.add(self)
        db.session.commit()

    def _delete(self) -> None:
        db.session.delete(self)
        db.session.commit()
