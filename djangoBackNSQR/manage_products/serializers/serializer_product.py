# serializers.py
from rest_framework import serializers
from ..models.model_product import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
