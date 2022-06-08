from abc import abstractmethod
from datetime import datetime, timezone
from math import inf
from models import User


class FilterException(Exception):
    def __init__(self, msg):
        self.msg = msg


class AbstractFilter:
    __abstract__ = True
    _next_filter = None

    def set_next(self, _filter):
        self._next_filter = _filter
        return _filter

    @abstractmethod
    def filter(self, **kwargs):
        if self._next_filter:
            return self._next_filter.filter(**kwargs)


class AgeFilter(AbstractFilter):
    def __init__(self, age_from, age_to) -> None:
        self.age_from = age_from or 0
        self.age_to = age_to or inf

    def filter(self, **kwargs):
        voter = User._get_by_pk(kwargs["voter_id"])
        if voter.age and not (self.age_from <= voter.age <= self.age_to):
            raise FilterException("Age not in allowed range")
        if self._next_filter:
            self._next_filter.filter(**kwargs)


class RegionFilter(AbstractFilter):
    def __init__(self, allowed_regions) -> None:
        self.allowed_regions = allowed_regions

    def filter(self, **kwargs):
        region = kwargs["region_id"]
        if region and region not in [allowed_region.pk for allowed_region in self.allowed_regions]:
            raise FilterException("Region not in allowed regions")
        if self._next_filter:
            self._next_filter.filter(**kwargs)


class VotesCancelableFilter(AbstractFilter):
    def __init__(self, votes_cancelable) -> None:
        self.votes_cancelable = votes_cancelable

    def filter(self, **kwargs):
        voter = User._get_by_pk(kwargs["voter_id"])
        election_id = kwargs["election_id"]
        if not self.votes_cancelable and voter._already_voted(election_id):
            raise FilterException("Changing votes is not allowed")
        if self._next_filter:
            self._next_filter.filter(**kwargs)


class DateFilter(AbstractFilter):
    def __init__(self, start, end) -> None:
        self.start = start
        self.end = end

    def filter(self, **kwargs):
        if not (self.start <= datetime.now(timezone.utc) <= self.end):
            raise FilterException("Voting is expired")
        if self._next_filter:
            self._next_filter.filter(**kwargs)

class PointsFilter(AbstractFilter):
    def __init__(self, points) -> None:
        self.points = points

    def filter(self, **kwargs):
        if sum(kwargs['voting_data'].values()) > self.points:
            raise FilterException("Total sum of points is bigger than limit")
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
