# serializers.py
from rest_framework import serializers
from ..models.model_product_category import ProductCategory
from ..models.model_product import Product
from ..models.model_category import Category

class ProductCategorySerializer(serializers.ModelSerializer):
    # Si deseas mostrar el nombre o algún campo específico de Product y Category en lugar del ID, puedes personalizar aquí.
    product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())

    class Meta:
        model = ProductCategory
        fields = ['product_category_id', 'product', 'category', 'modified_datetime', 'created_datetime']
