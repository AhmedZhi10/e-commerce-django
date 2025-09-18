from rest_framework import generics, filters
from drf_spectacular.utils import extend_schema
from django_filters.rest_framework import DjangoFilterBackend

from .models import Product, Category, Audience
from .serializers import ProductSerializer, CategorySerializer, AudienceSerializer


# -----------------------
# Audience List
# -----------------------
@extend_schema(responses=AudienceSerializer)
class AudienceListView(generics.ListAPIView):
    queryset = Audience.objects.all()
    serializer_class = AudienceSerializer


# -----------------------
# Category List
# -----------------------
@extend_schema(responses=CategorySerializer)
class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.select_related("audience").all()
    serializer_class = CategorySerializer


# -----------------------
# All Products
# -----------------------
@extend_schema(responses=ProductSerializer)
class ProductListView(generics.ListAPIView):
    queryset = Product.objects.select_related("category__audience").all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    filterset_fields = ["category__name", "size", "color"]
    ordering_fields = ["price", "created_at"]
    search_fields = ["name", "description", "color"]


# -----------------------
# Products filtered by audience (men, women, kids)
# -----------------------
@extend_schema(responses=ProductSerializer)
class ProductByAudienceView(generics.ListAPIView):
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    filterset_fields = ["category__name", "size", "color"]
    ordering_fields = ["price", "created_at"]
    search_fields = ["name", "description", "color"]

    def get_queryset(self):
        audience_name = self.kwargs["audience"]
        return (
            Product.objects
            .select_related("category", "category__audience")
            .filter(category__audience__name__iexact=audience_name)
        )
