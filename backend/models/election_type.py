from app import db
from .abstract_model import AbstractModel


class ElectionType(AbstractModel):
    __tablename__ = 'election_types'

    pk = db.Column(db.Integer, primary_key=True)
    votes_cancelable = db.Column(db.Boolean, default=False, nullable=False)
    organization_members_only = db.Column(db.Boolean, default=False, nullable=False)
    age_from = db.Column(db.Integer, nullable=True)
    age_to = db.Column(db.Integer, nullable=True)
    voter_votes_count = db.Column(db.Integer, default=1, nullable=False)
