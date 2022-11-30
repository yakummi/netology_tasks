from django_filters.rest_framework import DjangoFilterBackend, DateFromToRangeFilter, FilterSet
from .models import Advertisement
from advertisements.models import Advertisement, AdvertisementStatusChoices


class AdvertisementFilter(FilterSet):
    created_at = DateFromToRangeFilter()
    status = ChoiceFilter(field_name='status', choices=AdvertisementStatusChoices.choices)

    class Meta:
        model = Advertisement
        fields = ['created_at', 'creator', 'status']