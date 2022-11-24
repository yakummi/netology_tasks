from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from .filters import AdvertisementFilter
from .models import Advertisement
from .permissions import IsOwnerOrReadOnly
from .serializers import AdvertisementSerializer

class AdvertisementViewSet(ModelViewSet):
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = AdvertisementFilter

    def get_permissions(self):
        if self.request.user.is_staff:
            return [IsAuthenticated()]
        if self.action == 'create':
            return [IsAuthenticated(), ]
        if self.action in ["update", "partial_update", "destroy", ]:
            return [IsAuthenticated(), IsOwnerOrReadOnly()]
        return []
