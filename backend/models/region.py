from app import db, MODEL_TO_TABLENAME
from .abstract_model import AbstractModel


class Region(AbstractModel):
    __tablename__ = MODEL_TO_TABLENAME.get('Region')

    pk = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
