from app import db, MODEL_TO_TABLENAME
from .abstract_model import AbstractModel


class ElectionType(AbstractModel):
    __tablename__ = MODEL_TO_TABLENAME.get('ElectionType')

    pk = db.Column(db.Integer, primary_key=True)
    votes_cancelable = db.Column(db.Boolean, default=False, nullable=False)
    organization_members_only = db.Column(db.Boolean, default=False, nullable=False)
    age_from = db.Column(db.Integer, nullable=True)
    age_to = db.Column(db.Integer, nullable=True)
    voter_votes_count = db.Column(db.Integer, default=1, nullable=False)
    regions_allowed = db.relationship('Region', secondary=MODEL_TO_TABLENAME.get('ElectionTypeAllowedRegions'))


class ElectionTypeAllowedRegions(db.Model):
    __tablename__ = MODEL_TO_TABLENAME.get('ElectionTypeAllowedRegions')

    election_type_pk = db.Column(db.ForeignKey(MODEL_TO_TABLENAME.get('ElectionType') + '.pk', ondelete='CASCADE'),
                                 primary_key=True)
    region_pk = db.Column(db.ForeignKey(MODEL_TO_TABLENAME.get('Region') + '.pk', ondelete='CASCADE'), primary_key=True)
