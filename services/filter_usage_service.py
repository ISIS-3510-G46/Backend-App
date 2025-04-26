from repository.filter_usage_repo import add_filter_usage
from schemas.filter_usage import FilterUsage


def register_filter_usage(evt: FilterUsage):
    return add_filter_usage(evt)
