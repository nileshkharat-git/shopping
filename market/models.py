from django.db import models
from main.models import Accounts

class ProductType(models.Model):
    p_type = models.CharField(max_length=255)
    
    def __str__(self):
        return self.p_type

class Products(models.Model):
    product_id=models.IntegerField(primary_key=True)
    product_name=models.CharField(max_length=255)
    product_type=models.ForeignKey(ProductType,on_delete=models.CASCADE)
    product_details=models.TextField(null=True)
    product_price = models.FloatField()
    product_image=models.ImageField(blank=True,null=True,upload_to="products")

    def __str__(self):
        return f"{self.product_id}.{self.product_name}"

class MyCart(models.Model):
    user=models.ForeignKey(Accounts,on_delete=models.CASCADE)
    product_name=models.CharField(max_length=255)
    quantity = models.IntegerField()
    total = models.IntegerField()
    payment_method=models.CharField(max_length=100,null=True)
    purchesed=models.BooleanField(default=False)
    
    def __str__(self):
        return str(self.user)