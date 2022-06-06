from app import db, MODEL_TO_TABLENAME
from .abstract_model import AbstractModel


class Election(AbstractModel):
    __tablename__ = MODEL_TO_TABLENAME.get('Election')

    pk = db.Column(db.Integer, primary_key=True)
    type_pk = db.Column(db.ForeignKey(MODEL_TO_TABLENAME.get('ElectionType') + '.pk', ondelete='CASCADE'))
    start = db.Column(db.DateTime(timezone=True), nullable=False)
    end = db.Column(db.DateTime(timezone=True), nullable=False)
    type = db.relationship('ElectionType')
    candidates = db.relationship('User', secondary=MODEL_TO_TABLENAME.get('CandidatesInElections'))


class CandidatesInElections(db.Model):
    __tablename__ = MODEL_TO_TABLENAME.get('CandidatesInElections')

    candidate_pk = db.Column(db.ForeignKey(MODEL_TO_TABLENAME.get('User') + '.pk', ondelete='CASCADE'),
                             primary_key=True)
    election_pk = db.Column(db.ForeignKey(MODEL_TO_TABLENAME.get('Election') + '.pk', ondelete='CASCADE'),
                            primary_key=True)
