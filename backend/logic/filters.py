from abc import abstractmethod
from datetime import datetime
from models import User, Region


class FilterException(Exception):
    pass


class AbstractFilter:
    __abstract__ = True
    _next_filter = None

    def set_next(self, _filter):
        self._next_filter = _filter
        return _filter

    @abstractmethod
    def filter(self, request):
        if self._next_filter:
            return self._next_filter.filter(request)


class AgeFilter(AbstractFilter):
    def __init__(self, age_from, age_to) -> None:
        self.age_from = age_from
        self.age_to = age_to

    def filter(self, **kwargs):
        voter = User._get_by_pk(kwargs["voter_id"])
        if not (self.age_from <= voter.age <= self.age_to):
            raise FilterException("Age not in allowed range")
        if self._next_filter:
            self._next_filter.filter(**kwargs)


class RegionFilter(AbstractFilter):
    def __init__(self, allowed_regions) -> None:
        self.allowed_regions = allowed_regions

    def filter(self, **kwargs):
        region = kwargs["region"]
        if region and region not in self.allowed_regions:
            raise FilterException("Region not in allowed regions")
        if self._next_filter:
            self._next_filter.filter(**kwargs)


class VotesCancelableFilter(AbstractFilter):
    def __init__(self, votes_cancelable) -> None:
        self.votes_cancelable = votes_cancelable

    def filter(self, **kwargs):
        voter = User._get_by_pk(kwargs["voter_id"])
        election_id = kwargs["election_id"]
        if not self.votes_cancelable and voter.already_voted(election_id):
            raise FilterException("Changing votes is not allowed")
        if self._next_filter:
            self._next_filter.filter(**kwargs)


class DateFilter(AbstractFilter):
    def __init__(self, start, end) -> None:
        self.start = start
        self.end = end
        self.current_date = datetime.utcnow()

    def filter(self, **kwargs):
        if not (self.start <= self.current_date <= self.end):
            raise FilterException("Voting is expired")
        if self._next_filter:
            self._next_filter.filter(**kwargs)


class OrganizationFilter(AbstractFilter):
    def __init__(self, organization_members_only) -> None:
        self.organization_members_only = organization_members_only

    def filter(self, **kwargs):
        voter = User._get_by_pk(kwargs["voter_id"])
        if self.organization_members_only and voter.is_organization_member:
            raise FilterException("Only organization members allowed")
        if self._next_filter:
            self._next_filter.filter(**kwargs)
