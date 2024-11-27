from django.db import models
from .model_father_category import FatherCategory

# Create your models here.
class Category(models.Model):
    category_id       = models.AutoField(primary_key=True)
    category_name     = models.CharField(max_length=30)
    father_category   = models.ForeignKey(FatherCategory, on_delete=models.CASCADE, null=True, related_name='father_category')
    modified_datetime = models.DateTimeField(auto_now_add=True)
    created_datetime  = models.DateTimeField(auto_now_add=True)

    

    def __str__(self):
         return f"ID: {self.category_id} - Ttitle: {self.category_name}"