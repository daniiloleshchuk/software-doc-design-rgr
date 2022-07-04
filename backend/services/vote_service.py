import logic.filters as filters


from models import Election, ElectionType, Vote
from logic.voting_strategy.points_voting import PointsVotingStrategy
from logic.voting_strategy.regular_voting import RegularVotingStrategy


class VoteService:
    def __init__(self, election_pk):
        election = Election._get_by_pk(election_pk)
        election_type = ElectionType._get_by_pk(election.type_pk)
        self.filters = None
        self.voting_strategy = (PointsVotingStrategy() if election_type.voter_votes_count > 1
                                else RegularVotingStrategy())
        self.init_filters(election)

    def init_filters(self, election):
        _filters = (filters.AgeFilter(election.type.age_from, election.type.age_to),
                    filters.CandidatesFilter(election.candidates),
                    filters.OrganizationFilter(election.type.organization_members_only),
                    filters.RegionFilter(election.type.regions_allowed),
                    filters.PointsFilter(election.type.voter_votes_count),
                    filters.VotesCancelableFilter(election.type.votes_cancelable),
                    filters.DateFilter(election.start, election.end))

        for idx, _filter in enumerate(_filters[:-1]):
            _filter.set_next(_filters[idx + 1])

        self.filters = _filters[0]

    def register_vote(self, voting_data, voter_pk, election_pk, region_pk=None, **kwargs):
        self.filters.filter(voting_data=voting_data, voter_id=voter_pk, election_id=election_pk, region_id=region_pk)
        Vote.remove_user_votes(voter_pk=voter_pk, election_pk=election_pk)
        return self.voting_strategy.register_vote(voting_data, voter_pk, election_pk)
