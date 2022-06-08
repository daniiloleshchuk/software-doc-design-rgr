from app import db, MODEL_TO_TABLENAME
from .abstract_model import AbstractModel


class Vote(AbstractModel):
    __tablename__ = MODEL_TO_TABLENAME.get('Vote')

    pk = db.Column(db.Integer, primary_key=True)
    voter_pk = db.Column(db.ForeignKey(MODEL_TO_TABLENAME.get('User') + '.pk', ondelete='CASCADE'))
    candidate_pk = db.Column(db.ForeignKey(MODEL_TO_TABLENAME.get('User') + '.pk', ondelete='CASCADE'))
    election_pk = db.Column(db.ForeignKey(MODEL_TO_TABLENAME.get('Election') + '.pk', ondelete='CASCADE'))
    voter = db.relationship('User', foreign_keys=(voter_pk,))
    candidate = db.relationship('User', foreign_keys=(candidate_pk,))
    election = db.relationship('Election', foreign_keys=(election_pk,))
    points_count = db.Column(db.Integer, default=1, nullable=False)
    datetime = db.Column(db.DateTime, nullable=True)

    @classmethod
    def _does_user_voted(cls, voter_pk, election_pk):
        return True if cls.query.filter_by(voter_pk=voter_pk, election_pk=election_pk).all() else False

    @classmethod
    def remove_user_votes(cls, voter_pk, election_pk):
        votes = cls.query.filter_by(voter_pk=voter_pk, election_pk=election_pk)
        votes.delete()
