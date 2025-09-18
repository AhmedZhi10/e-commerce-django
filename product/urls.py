from django.urls import path
from .views import (
    AudienceListView,
    CategoryListView,
    ProductListView,
    ProductByAudienceView,
)

urlpatterns = [
    path("audiences/", AudienceListView.as_view(), name="audience-list"),
    path("categories/", CategoryListView.as_view(), name="category-list"),
    path("products/", ProductListView.as_view(), name="product-list"),
    path("products/<str:audience>/", ProductByAudienceView.as_view(), name="product-by-audience"),
]
