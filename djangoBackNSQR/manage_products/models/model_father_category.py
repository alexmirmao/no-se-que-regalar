from django.db import models

# Create your models here.
class FatherCategory(models.Model):
    father_category_id  = models.AutoField(primary_key=True)
    father_category_name= models.CharField(max_length=30)
    modified_datetime   = models.DateTimeField(auto_now_add=True)
    created_datetime    = models.DateTimeField(auto_now_add=True)

    

    def __str__(self):
         return f"ID: {self.father_category_id} - Ttitle: {self.father_category_name}"