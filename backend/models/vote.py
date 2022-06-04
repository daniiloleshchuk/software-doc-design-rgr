from app import db
from .abstract_model import AbstractModel


class Vote(AbstractModel):
    __tablename__ = 'votes'

    pk = db.Column(db.Integer, primary_key=True)
    voter_pk = db.Column(db.ForeignKey('users.pk', ondelete='CASCADE'))
    voter = db.relationship('User', foreign_keys=(voter_pk,))
    candidate_pk = db.Column(db.ForeignKey('users.pk', ondelete='CASCADE'))
    candidate = db.relationship('User', foreign_keys=(candidate_pk,))
    election_pk = db.Column(db.ForeignKey('elections.pk', ondelete='CASCADE'))
    election = db.relationship('Election', foreign_keys=(election_pk,))
    points_count = db.Column(db.Integer, default=1, nullable=False)
    datetime = db.Column(db.DateTime, nullable=True)
