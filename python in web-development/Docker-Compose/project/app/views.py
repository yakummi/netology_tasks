from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import LimitOffsetPagination
from app.models import Product, Stock
from app.serializers import ProductSerializer, StockSerializer

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = ['title', 'description', ]
    filterset_fields = ['title', 'description', ]
    pagination_class = LimitOffsetPagination


class StockViewSet(ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = ['products__title', 'products__description']
    filterset_fields = ['products']
    pagination_class = LimitOffsetPagination