from app import db, MODEL_TO_TABLENAME
from .abstract_model import AbstractModel


class User(AbstractModel):
    __tablename__ = MODEL_TO_TABLENAME.get('User')

    pk = db.Column(db.Integer, primary_key=True)
    region_pk = db.Column(db.Integer,
                          db.ForeignKey(MODEL_TO_TABLENAME.get('Region') + '.pk', ondelete='SET NULL'),
                          nullable=True)
    name = db.Column(db.String(50), nullable=False)
    age = db.Column(db.Integer, nullable=True)
    region = db.relationship('Region')
    elections = db.relationship('Election',
                                secondary=MODEL_TO_TABLENAME.get('CandidatesInElections'),
                                back_populates='candidates')
    organizations = db.relationship('Organization',
                                    secondary= MODEL_TO_TABLENAME.get('UsersInOrganizations'),
                                    back_populates='members')


class UsersInOrganizations(db.Model):
    __tablename__ = MODEL_TO_TABLENAME.get('UsersInOrganizations')

    user_pk = db.Column(db.ForeignKey(MODEL_TO_TABLENAME.get('User') + '.pk', ondelete='CASCADE'),
                        primary_key=True)
    organization_pk = db.Column(db.ForeignKey(MODEL_TO_TABLENAME.get('Organization') + '.pk', ondelete='CASCADE'),
                                primary_key=True)
