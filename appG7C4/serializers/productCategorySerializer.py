# Create a ProductCategorySerializer to serialize the ProductCategory model
from rest_framework import serializers
from ..models import ProductCategory

class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = ('id', 'name', 'description', 'image', 'created_at', 'user_id')