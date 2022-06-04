from app import db
from .abstract_model import AbstractModel


class Election(AbstractModel):
    __tablename__ = 'elections'

    pk = db.Column(db.Integer, primary_key=True)
    start = db.Column(db.DateTime(timezone=True), nullable=False)
    end = db.Column(db.DateTime(timezone=True), nullable=False)
    type_pk = db.Column(db.ForeignKey('election_types.pk', ondelete='CASCADE'))
    type = db.relationship('ElectionType')
    regions_allowed = db.relationship('Region', secondary='election_allowed_regions')
    candidates = db.relationship('User', secondary='candidates_in_elections', back_populates='elections')


class ElectionAllowedRegions(db.Model):
    __tablename__ = 'election_allowed_regions'

    election_pk = db.Column(db.ForeignKey('elections.pk', ondelete='CASCADE'), primary_key=True)
    region_pk = db.Column(db.ForeignKey('regions.pk', ondelete='CASCADE'), primary_key=True)


class CandidatesInElections(db.Model):
    __tablename__ = 'candidates_in_elections'

    candidate_pk = db.Column(db.ForeignKey('users.pk', ondelete='CASCADE'), primary_key=True)
    election_pk = db.Column(db.ForeignKey('elections.pk', ondelete='CASCADE'), primary_key=True)
