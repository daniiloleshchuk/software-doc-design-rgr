import logic.filters as filters


from models import Election
from logic.voting_strategy.points_voting import PointsVotingStrategy
from logic.voting_strategy.regular_voting import RegularVotingStrategy


class VoteService:
    def __init__(self, election_id):

        election = Election._get_by_pk(election_id)
        election_type = election.type
        if election_type.voter_votes_count > 1:
            self.set_voting_strategy(PointsVotingStrategy())
        else:
            self.set_voting_strategy(RegularVotingStrategy())

        age_filter = filters.AgeFilter(
            election_type.age_from, election_type.age_to)
        organization_filter = filters.OrganizationFilter(
            election_type.organization_members_only)
        region_filter = filters.RegionFilter(election_type.regions_allowed)
        already_voted_filter = filters.VotesCancelableFilter(
            election_type.votes_cancelable)
        date_filter = filters.DateFilter(election.start, election.end)

        age_filter \
            .set_next(organization_filter)\
            .set_next(region_filter) \
            .set_next(date_filter) \
            .set_next(already_voted_filter)

        self.set_filters(age_filter)

    def set_voting_strategy(self, voting_counter):
        self.voting_counter = voting_counter

    def set_filters(self, filters):
        self.filters = filters

    def register_vote(self, voting_data, voter_id, election_id, region_id=None, **kwargs):
        self.filters.filter(voting_data, voter_id,
                            election_id, region_id)
        return self.voting_counter.register_vote(voting_data, voter_id, election_id)
