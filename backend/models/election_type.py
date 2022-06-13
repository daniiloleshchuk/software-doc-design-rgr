from app import db, MODEL_TO_TABLENAME
from .region import Region
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

    def __init__(self, regions_allowed_pks=None, **kwargs):
        super(ElectionType, self).__init__(**kwargs)
        if regions_allowed_pks:
            for region_pk in regions_allowed_pks:
                self.regions_allowed.append(Region._get_by_pk(pk=region_pk))


class ElectionTypeAllowedRegions(AbstractModel):
    __tablename__ = MODEL_TO_TABLENAME.get('ElectionTypeAllowedRegions')

    election_type_pk = db.Column(db.ForeignKey(MODEL_TO_TABLENAME.get('ElectionType') + '.pk', ondelete='CASCADE'),
                                 primary_key=True)
    region_pk = db.Column(db.ForeignKey(MODEL_TO_TABLENAME.get('Region') + '.pk', ondelete='CASCADE'), primary_key=True)
