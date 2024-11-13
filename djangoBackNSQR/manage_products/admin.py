from django.contrib import admin
from .models.model_product import Product
from .models.model_category import Category
from .models.model_product_category import ProductCategory
from .models.model_product_like import ProductLike

# Register your models here.

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(ProductCategory)
admin.site.register(ProductLike)
