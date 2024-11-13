from django.contrib.auth.models import User
from django.db import models
from .model_product import Product

class ProductLike(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="liked")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('product', 'user')  # Asegura que cada usuario pueda dar solo un like por producto.
