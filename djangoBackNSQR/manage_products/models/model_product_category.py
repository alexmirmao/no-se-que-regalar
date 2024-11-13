from django.db import models
from .model_product import Product
from .model_category import Category

# Create your models here.
class ProductCategory(models.Model):
    product_category_id = models.AutoField(primary_key=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_categories')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category_products')
    modified_datetime = models.DateTimeField(auto_now=True)
    created_datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Product ID: {self.product_id} - Category ID: {self.category_id}"