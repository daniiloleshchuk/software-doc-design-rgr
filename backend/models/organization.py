from app import db, MODEL_TO_TABLENAME
from .abstract_model import AbstractModel


class Organization(AbstractModel):
    __tablename__ = MODEL_TO_TABLENAME.get('Organization')

    pk = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    members = db.relationship('User',
                              secondary=MODEL_TO_TABLENAME.get('UsersInOrganizations'),
                              back_populates='organizations')
