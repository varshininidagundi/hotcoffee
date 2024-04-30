from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='product_images/') 
    
    def __str__(self):
        return self.name

class Cart(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    qty = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.product.name
