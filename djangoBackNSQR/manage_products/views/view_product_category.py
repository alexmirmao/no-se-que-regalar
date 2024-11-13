from django.shortcuts import render
from ..models.model_product_category import ProductCategory
from ..serializers.serializer_product_category import ProductCategorySerializer
from rest_framework import viewsets
# Create your views here.

class ProductCategoryViewSet(viewsets.ModelViewSet):
    queryset = ProductCategory.objects.select_related('product', 'category').all()
    serializer_class = ProductCategorySerializer
"""def get_all(request):
    objetos = Product.objects.all()  # Recupera todos los objetos del modelo
    return render(request, 'tu_template.html', {'objetos': objetos})"""