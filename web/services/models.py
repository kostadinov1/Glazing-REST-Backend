from django.db import models


class Service(models.Model):
    name = models.CharField(max_length=30, null=False, blank=False)
    description = models.TextField(max_length=300, null=True, blank=True)
    work_duration = models.PositiveIntegerField(null=True, blank=True)
    price = models.PositiveIntegerField(null=False, blank=False)
    image = models.ImageField(upload_to='service_images', null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)


class CompanyInfo(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=5000, null=True, blank=True)
    address = models.TextField(max_length=300, null=True, blank=True)
    phone = models.TextField(max_length=300, null=True, blank=True)
    mobile_phone = models.TextField(max_length=300, null=True, blank=True)

