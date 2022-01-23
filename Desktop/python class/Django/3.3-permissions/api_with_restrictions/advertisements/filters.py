from django_filters import rest_framework as filters

from advertisements.models import Advertisement
from django_filters import DateFromToRangeFilter, CharFilter, ChoiceFilter


class AdvertisementFilter(filters.FilterSet):
    """Фильтры для объявлений."""
    STATUS_CHOICES = (
        (0, 'Regular'),
        (1, 'Manager'),
        (2, 'Admin'),
    )

    #status =  NumberFilter(field_name='status')
    status = ChoiceFilter(choices=STATUS_CHOICES)
    #status = CharFilter(field_name='status')
    created_at = DateFromToRangeFilter()


    class Meta:
        model = Advertisement
        fields = ['status', 'created_at']
        #fields = ['created_at']
