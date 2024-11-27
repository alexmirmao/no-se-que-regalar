from django.shortcuts import render
from ..models.model_category import Category
from ..serializers.serializer_category import CategorySerializer
from rest_framework import viewsets
# Create your views here.

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.select_related('father_category').all()
    serializer_class = CategorySerializer
"""def get_all(request):
    objetos = Product.objects.all()  # Recupera todos los objetos del modelo
    return render(request, 'tu_template.html', {'objetos': objetos})"""