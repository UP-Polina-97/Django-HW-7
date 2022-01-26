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


    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer

    filterset_class = AdvertisementFilter
    filter_backends = [DjangoFilterBackend]

#not sure if its needed here or not....(22-23)
    throttle_classes = [AnonRateThrottle, UserRateThrottle]
    filterset_fields = ['creator', 'created_at']

    def get_permissions(self):
        """Получение прав для действий."""
        if self.action in ["create", "update", "partial_update"]:
            return [IsAuthenticated()]
        if self.action in ["update", "partial_update", "destroy"]:
            return [IsOwnerOrReadOnly()]
        return []
