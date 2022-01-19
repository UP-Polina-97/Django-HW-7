from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from advertisements.models import Advertisement
from advertisements.serializers import AdvertisementSerializer
from advertisements.filters import AdvertisementFilter
from advertisements.permissions import IsOwnerOrReadOnly
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle
from django_filters.rest_framework import DjangoFilterBackend
from requests import request

class AdvertisementViewSet(ModelViewSet):
    """ViewSet для объявлений."""

    # TODO: настройте ViewSet, укажите атрибуты для кверисета,
    #   сериализаторов и фильтров
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer

    filterset_class = AdvertisementFilter
    #filterset_class = AdvertisementFilter(request.GET, queryset=Advertisement.objects.all())
    throttle_classes = [AnonRateThrottle, UserRateThrottle]


    #filter_backends = [DjangoFilterBackend, filters.SearchFilter, AdvertisementFilter]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['creator', 'created_at']

    def get_permissions(self):
        """Получение прав для действий."""
        if self.action in ["create", "update", "partial_update"]:
            return [IsAuthenticated(),
                    IsOwnerOrReadOnly()]
        return []
