from rest_framework import viewsets, permissions
from .models import *
from .serializers import *
from django_filters.rest_framework import DjangoFilterBackend
from .filters import ProductFilter
from rest_framework.filters import SearchFilter

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_class = ProductFilter
    search_fields = ['product_name']
    permission_classes = [permissions.IsAuthenticated]
    ordering_fields = ['price', 'created_date', 'product_name']
