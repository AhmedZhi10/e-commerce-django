from rest_framework import serializers
from .models import Audience, Category, Product


class AudienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Audience
        fields = ["id", "name"]


class CategorySerializer(serializers.ModelSerializer):
    audience = AudienceSerializer(read_only=True)

    class Meta:
        model = Category
        fields = ["id", "name", "audience"]


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)

    class Meta:
        model = Product
        fields = [
            "id", "name", "price", "description",
            "size", "color", "stock", "created_at", "category"
        ]
