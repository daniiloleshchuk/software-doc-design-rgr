from models import Vote


class PointsVotingStrategy:

    def register_vote(self, voting_data, voter, election):
        votes = []
        for candidate, points in voting_data.items():
            new_vote = Vote(voter_pk=voter,
                            points_count=points,
                            candidate_pk=candidate,
                            election_pk=election)
            new_vote._save()
            votes.append(new_vote)
        return votes
