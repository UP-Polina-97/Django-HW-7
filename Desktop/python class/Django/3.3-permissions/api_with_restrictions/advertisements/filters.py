from django_filters import rest_framework as filters

from advertisements.models import Advertisement
from django_filters import DateFromToRangeFilter


class AdvertisementFilter(filters.FilterSet):
    """Фильтры для объявлений."""
    status = DateFromToRangeFilter()
    created_at = DateFromToRangeFilter()


    # TODO: задайте требуемые фильтры

    class Meta:
        model = Advertisement
        fields = ['status', 'created_at']
