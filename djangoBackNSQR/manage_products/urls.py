from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from manage_products.views.view_product import ProductViewSet
from manage_products.views.view_category import CategoryViewSet
from manage_products.views.view_product_category import ProductCategoryViewSet


router = DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'category', CategoryViewSet)
router.register(r'products_categories', ProductCategoryViewSet)

urlpatterns = [
    path('', include(router.urls)),  # Rutas generadas por el DefaultRouter
]