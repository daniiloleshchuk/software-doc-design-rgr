from models import Election, Vote


class ElectionStatsService:
    @classmethod
    def get_election_stats_by_pk(cls, election_pk):
        election = Election._get_by_pk(pk=election_pk)
        candidates = election.candidates
        statistic = {}
        for candidate in candidates:
            votes = Vote.query.filter_by(election_pk=election_pk, candidate_pk=candidate.pk).all()
            total_points = sum([vote.points_count for vote in votes])
            statistic[candidate] = total_points
        return statistic
