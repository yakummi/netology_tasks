from django_filters.rest_framework import DjangoFilterBackend, DateFromToRangeFilter, FilterSet
from .models import Advertisement


class AdvertisementFilter(FilterSet):
    created_at = DateFromToRangeFilter()

    class Meta:
        model = Advertisement
        fields = ['created_at', 'creator']