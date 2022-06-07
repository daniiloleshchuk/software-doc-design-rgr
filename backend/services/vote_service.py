import logic.filters as filters


from models import Election, ElectionType
from logic.voting_strategy.points_voting import PointsVotingStrategy
from logic.voting_strategy.regular_voting import RegularVotingStrategy


class VoteService:
    def __init__(self, election_pk):
        election = Election._get_by_pk(election_pk)
        election_type = ElectionType._get_by_pk(election.type_pk)
        self.filters = None
        self.voting_strategy = (PointsVotingStrategy() if election_type.voter_votes_count > 1
                                else RegularVotingStrategy())
        self.init_filters(election, election_type)

    def init_filters(self, election, election_type):
        _filters = (filters.AgeFilter(election_type.age_from, election_type.age_to),
                    filters.OrganizationFilter(election_type.organization_members_only),
                    filters.RegionFilter(election_type.regions_allowed),
                    filters.VotesCancelableFilter(election_type.votes_cancelable),
                    filters.DateFilter(election.start, election.end))

        for idx, _filter in enumerate(_filters[:-1]):
            _filter.set_next(_filters[idx + 1])

        self.filters = _filters[0]

    def register_vote(self, voting_data, voter_id, election_id, region_id=None, **kwargs):
        self.filters.filter(voting_data=voting_data, voter_id=voter_id,
                            election_id=election_id, region_id=region_id)
        return self.voting_strategy.register_vote(voting_data, voter_id, election_id)
