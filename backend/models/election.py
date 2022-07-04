from datetime import datetime, timedelta, timezone

from app import db, MODEL_TO_TABLENAME
from .user import User
from .abstract_model import AbstractModel


class Election(AbstractModel):
    __tablename__ = MODEL_TO_TABLENAME.get('Election')

    pk = db.Column(db.Integer, primary_key=True)
    type_pk = db.Column(db.ForeignKey(MODEL_TO_TABLENAME.get('ElectionType') + '.pk', ondelete='CASCADE'), nullable=False)
    start = db.Column(db.DateTime(timezone=True), nullable=False)
    end = db.Column(db.DateTime(timezone=True), nullable=False)
    candidates = db.relationship('User', secondary=MODEL_TO_TABLENAME.get('CandidatesInElections'))
    type = db.relationship('ElectionType')

    def __init__(self, days_duration=1, candidates_pks=None, **kwargs):
        super(Election, self).__init__(**kwargs)
        self.start = datetime.now(timezone.utc)
        self.end = self.start + timedelta(days=days_duration)
        if candidates_pks:
            for candidate_pk in candidates_pks:
                self.candidates.append(User._get_by_pk(pk=candidate_pk))


class CandidatesInElections(db.Model):
    __tablename__ = MODEL_TO_TABLENAME.get('CandidatesInElections')

    candidate_pk = db.Column(db.ForeignKey(MODEL_TO_TABLENAME.get('User') + '.pk', ondelete='CASCADE'),
                             primary_key=True)
    election_pk = db.Column(db.ForeignKey(MODEL_TO_TABLENAME.get('Election') + '.pk', ondelete='CASCADE'),
                            primary_key=True)
