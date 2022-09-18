from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=30, null=False, blank=False)
    description = models.TextField(max_length=300, null=True, blank=True)
    price = models.PositiveIntegerField(null=False, blank=False)
    image = models.ImageField(upload_to='product_images', null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)