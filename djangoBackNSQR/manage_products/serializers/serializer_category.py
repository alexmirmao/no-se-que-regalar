# serializers.py
from rest_framework import serializers
from ..models.model_category import Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
