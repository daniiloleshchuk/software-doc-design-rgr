from datetime import datetime
from models import User


class FilterException(Exception):
    pass


class AgeFilter:
    def __init__(self, age_from, age_to) -> None:
        self.age_from = age_from
        self.age_to = age_to
        self.next_filter = None

    def set_next(self, next_filter):
        self.next_filter = next_filter
        return next_filter

    def filter(self, **kwargs):
        voter = User._get_by_pk(kwargs["voter_id"])
        if not (self.age_from <= voter.age <= self.age_to):
            raise FilterException("Age not in allowed range")
        if self.next_filter:
            self.next_filter.filter(**kwargs)


class RegionFilter:
    def __init__(self, allowed_regions) -> None:
        self.allowed_regions = allowed_regions
        self.next_filter = None

    def set_next(self, next_filter):
        self.next_filter = next_filter
        return next_filter

    def filter(self, **kwargs):
        region = kwargs["region"]
        if region and region not in self.allowed_regions:
            raise FilterException("Region not in allowed regions")
        if self.next_filter:
            self.next_filter.filter(**kwargs)


class VotesCancelableFilter:
    def __init__(self, votes_cancelable) -> None:
        self.votes_cancelable = votes_cancelable
        self.next_filter = None

    def set_next(self, next_filter):
        self.next_filter = next_filter
        return next_filter

    def filter(self, **kwargs):
        voter = User._get_by_pk(kwargs["voter_id"])
        election_id = kwargs["election_id"]
        if not self.votes_cancelable and voter.already_voted(election_id):
            raise FilterException("Changing votes is not allowed")
        if self.next_filter:
            self.next_filter.filter(**kwargs)


class DateFilter:
    def __init__(self, start, end) -> None:
        self.start = start
        self.end = end
        self.current_date = datetime.utcnow()
        self.next_filter = None

    def set_next(self, next_filter):
        self.next_filter = next_filter
        return next_filter

    def filter(self, **kwargs):
        if not (self.start <= self.current_date <= self.end):
            raise FilterException("Voting is expired")
        if self.next_filter:
            self.next_filter.filter(**kwargs)


class OrganizationFilter:
    def __init__(self, organization_members_only) -> None:
        self.organization_members_only = organization_members_only
        self.next_filter = None

    def set_next(self, next_filter):
        self.next_filter = next_filter
        return next_filter

    def filter(self, **kwargs):
        voter = User._get_by_pk(kwargs["voter_id"])
        if self.organization_members_only and voter.is_organization_member:
            raise FilterException("Only organization members allowed")
        if self.next_filter:
            self.next_filter.filter(**kwargs)
