from app import db, MODEL_TO_TABLENAME
from .abstract_model import AbstractModel
from .vote import Vote


class User(AbstractModel):
    __tablename__ = MODEL_TO_TABLENAME.get('User')

    pk = db.Column(db.Integer, primary_key=True)
    region_pk = db.Column(db.Integer,
                          db.ForeignKey(MODEL_TO_TABLENAME.get('Region') + '.pk', ondelete='SET NULL'),
                          nullable=True)
    name = db.Column(db.String(50), nullable=False)
    age = db.Column(db.Integer, nullable=True)
    is_organization_member = db.Column(db.Boolean, default=False)
    region = db.relationship('Region')

    def _already_voted(self, election_pk):
        return Vote._does_user_voted(voter_pk=self.pk, election_pk=election_pk)
