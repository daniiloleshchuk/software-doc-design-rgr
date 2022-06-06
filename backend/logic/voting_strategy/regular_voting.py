from models import Vote


class RegularVotingStrategy:

    def register_vote(self, voting_data, voter, election):
        candidate = voting_data.keys()[0]
        new_vote = Vote(voter_pk=voter,
                        candidate_pk=candidate,
                        election_pk=election)
        new_vote._save()
        return new_vote
