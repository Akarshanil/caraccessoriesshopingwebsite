from django.db import models

# Create your models here.
class categorysave(models.Model):
    categoryname=models.CharField(max_length=30,null=True,blank=True)
    categoryimage=models.ImageField(upload_to='profile')
    description=models.CharField(max_length=100,null=True,blank=True)
class productsave(models.Model):
    procategoryname=models.CharField(max_length=60,null=True,blank=True)
    productname=models.CharField(max_length=60,null=True,blank=True)
    proquantity=models.IntegerField(null=True,blank=True)
    proprice=models.IntegerField(null=True,blank=True)
    productimage=models.ImageField(upload_to="productimage")
    prodescription = models.CharField(max_length=100,null=True,blank=True)
    popularity_score = models.IntegerField(default=0)
    is_trending = models.BooleanField(default=False)
    created_date = models.DateField(auto_now_add=True)  # Add this field for the creation date

