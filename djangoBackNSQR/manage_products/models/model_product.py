from django.db import models

# Create your models here.
class Product(models.Model):
    product_id        = models.AutoField(primary_key=True)
    product_name      = models.CharField(max_length=50)
    description       = models.CharField(max_length=400)
    product_url       = models.CharField(max_length=250)
    url_image         = models.CharField(max_length=250)
    price             = models.DecimalField(max_digits=6, decimal_places=2)
    likes             = models.IntegerField()
    modified_datetime = models.DateTimeField(auto_now_add=True)
    created_datetime  = models.DateTimeField(auto_now_add=True)

    

    def __str__(self):
         return f"ID: {self.product_id} - Ttitle: {self.product_name} - Description: {self.description} - Price: {self.price} - Saved: {self.likes}"