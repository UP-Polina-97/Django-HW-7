from django_filters import rest_framework as filters

from advertisements.models import Advertisement
from django_filters import DateFromToRangeFilter, CharFilter


class AdvertisementFilter(filters.FilterSet):
    """Фильтры для объявлений."""
    #status =  NumberFilter(field_name='status')
    #status =  ChoiceFilter(choices=STATUS_CHOICES)
    status = CharFilter(field_name='status')
    created_at = DateFromToRangeFilter()


    # TODO: задайте требуемые фильтры

    class Meta:
        model = Advertisement
        fields = ['status', 'created_at']
        #fields = ['created_at']
