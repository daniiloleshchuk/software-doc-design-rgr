import logic.filters as filters


from models import Election
from logic.voting_strategy.points_voting import PointsVotingStrategy
from logic.voting_strategy.regular_voting import RegularVotingStrategy


class VoteService:
    def __init__(self, election_pk):
        election = Election._get_by_pk(election_pk)
        self.filters = None
        self.voting_strategy = (PointsVotingStrategy() if election.type.voter_votes_count > 1
                                else RegularVotingStrategy())
        self.init_filters(election)

    def init_filters(self, election):
        _filters = (filters.AgeFilter(election.type.age_from, election.type.age_to),
                    filters.OrganizationFilter(election.type.organization_members_only),
                    filters.RegionFilter(election.type.regions_allowed),
                    filters.VotesCancelableFilter(election.type.votes_cancelable),
                    filters.DateFilter(election.start, election.end))

        for _filter in _filters[1:]:
            if filter:
                _filters[0].set_next(_filter)

        self.filters = _filters[0]

    def register_vote(self, voting_data, voter_id, election_id, region_id=None, **kwargs):
        self.filters.filter(voting_data, voter_id, election_id, region_id)
        return self.voting_strategy.register_vote(voting_data, voter_id, election_id)
