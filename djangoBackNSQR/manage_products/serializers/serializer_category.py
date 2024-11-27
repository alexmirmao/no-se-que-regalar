# serializers.py
from rest_framework import serializers
from ..models.model_category import Category
from ..models.model_father_category import FatherCategory

class CategorySerializer(serializers.ModelSerializer):
    father_category_name = serializers.CharField(source='father_category.father_category_name', read_only=True)
    father_category = serializers.PrimaryKeyRelatedField(queryset=FatherCategory.objects.all())

    class Meta:
        model = Category
        fields = [
            'category_id',
            'category_name',
            'father_category',
            'father_category_name',
            'modified_datetime',
            'created_datetime',
        ]
