from django.shortcuts import render
from ..models.model_product import Product
from ..models.model_product_category import ProductCategory
from ..models.model_product_like import ProductLike
from ..models.model_category import Category
from rest_framework.decorators import action
from rest_framework.response import Response
from ..serializers.serializer_product import ProductSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
# Create your views here.

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    @action(detail=False, methods=['get'], url_path='order-by-likes')
    def order_by_likes(self, request):
        """
        Acción para ordenar productos por la cantidad de likes.
        """
        # Recuperar los productos ordenados por likes en orden descendente
        products = Product.objects.all().order_by('-times_saved')[:15]
        serializer = self.get_serializer(products, many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=['get'], url_path='by-category/(?P<category_id>[^/.]+)')
    def filter_by_category(self, request, category_id=None):
        """
        Acción personalizada para devolver productos asociados a una categoría específica usando la tabla intermedia.
        """
        # Filtrar los productos usando la tabla intermedia product_category
        product_ids = ProductCategory.objects.filter(category_id=category_id).values_list('product_id', flat=True)
        products = Product.objects.filter(product_id__in=product_ids)
        
        serializer = self.get_serializer(products, many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=['get'], url_path='by-category-name/(?P<category_name>[^/.]+)')
    def filter_by_category_name(self, request, category_name=None):
        """
        Acción personalizada para devolver productos asociados a una categoría específica usando la tabla intermedia.
        """
        # Filtrar los productos usando la tabla intermedia product_category
        category_ids = Category.objects.filter(category_name=category_name).values_list('category_id', flat=True)
        product_ids = ProductCategory.objects.filter(category_id__in=category_ids).values_list('product_id', flat=True)
        products = Product.objects.filter(product_id__in=product_ids)
        
        serializer = self.get_serializer(products, many=True)
        return Response(serializer.data)
    
    @action(detail=True, methods=['post'], permission_classes=[IsAuthenticated], url_path='like')
    def like_product(self, request, pk=None):
        """
        Endpoint para dar like a un producto, solo accesible a usuarios autenticados.
        """
        product = self.get_object()
        user = request.user

        # Verifica si el usuario ya dio un like a este producto
        if ProductLike.objects.filter(product=product, user=user).exists():
            return Response({'status': 'Ya has dado like a este producto'}, status=status.HTTP_400_BAD_REQUEST)

        # Si no existe, crea un nuevo registro de like
        ProductLike.objects.create(product=product, user=user)
        product.likes += 1  # Incrementa el contador de likes si tienes este campo en el modelo
        product.save()

        return Response({'status': 'like agregado'}, status=status.HTTP_200_OK)
    
    @action(detail=True, methods=['post'], permission_classes=[IsAuthenticated], url_path='dislike')
    def dislike_product(self, request, pk=None):
        product = self.get_object()
        user = request.user

        # Busca el like del usuario para este producto
        like = ProductLike.objects.filter(user=user, product=product).first()

        if like:
            like.delete()
            return Response({'status': 'like eliminado'}, status=status.HTTP_200_OK)
        else:
            return Response({'status': 'no existe un like para eliminar'}, status=status.HTTP_400_BAD_REQUEST)