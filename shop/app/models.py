#build a django app with one page that show 3 products a user can enter quantity click buy complete stripe and then see their paid order on the same page
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=200)
    selling_price = models.FloatField()
    image = models.ImageField(upload_to='productimg')

    def __str__(self):
        return self.title

class OrderProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order #{self.id} - {self.product.title} ({self.quantity})"