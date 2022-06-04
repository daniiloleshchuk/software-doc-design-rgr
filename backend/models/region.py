from app import db
from .abstract_model import AbstractModel


class Region(AbstractModel):
    __tablename__ = 'regions'

    pk = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
