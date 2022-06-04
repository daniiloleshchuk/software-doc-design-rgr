from app import db
from .abstract_model import AbstractModel


class Organization(AbstractModel):
    __tablename__ = 'organizations'

    pk = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    members = db.relationship('User', secondary='users_in_orgs', back_populates='organizations')
