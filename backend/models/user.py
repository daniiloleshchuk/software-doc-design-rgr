from app import db
from .abstract_model import AbstractModel


class User(AbstractModel):
    __tablename__ = 'users'

    pk = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    age = db.Column(db.Integer, nullable=True)
    region_pk = db.Column(db.Integer, db.ForeignKey('regions.pk', ondelete='SET NULL'), nullable=True)
    region = db.relationship('Region')
    organizations = db.relationship('Organization', secondary='users_in_orgs', back_populates='members')
    elections = db.relationship('Election', secondary='candidates_in_elections', back_populates='candidates')


class UsersInOrganizations(db.Model):
    __tablename__ = 'users_in_orgs'

    user_pk = db.Column(db.ForeignKey('users.pk', ondelete='CASCADE'), primary_key=True)
    organization_pk = db.Column(db.ForeignKey('organizations.pk', ondelete='CASCADE'), primary_key=True)
