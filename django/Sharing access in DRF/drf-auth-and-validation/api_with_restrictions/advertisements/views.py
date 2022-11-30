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
        if self.action == 'create' or self.request.user.is_staff:
            return [IsAuthenticated(), ]
        if self.action in ["update", "partial_update", "destroy", ]:
            return [IsAuthenticated(), IsOwnerOrReadOnly()]

        return []

    def list(self, request, *args, **kwargs):
        if self.request.user:
            queryset_draft = Advertisement.objects.filter(
                creator__id=self.request.user.id,
                status='DRAFT'
            )
            queryset = self.queryset.union(queryset_draft)
            queryset = Advertisement.objects.filter(id__in=queryset.values('id'))
            queryset = self.filter_queryset(queryset)
            page = self.paginate_queryset(queryset)

            if page is not None:
                serializer = self.get_serializer(page, many=True)
                return self.get_paginated_response(serializer.data)

            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data)

        return super().list(request, *args, **kwargs)