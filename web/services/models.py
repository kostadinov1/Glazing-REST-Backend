from django.db import models


class Service(models.Model):
    name = models.CharField(max_length=30, null=False, blank=False)
    description = models.TextField(max_length=300, null=True, blank=True)
    work_duration = models.PositiveIntegerField(null=True, blank=True)
    price = models.PositiveIntegerField(null=False, blank=False)
    created_on = models.DateTimeField(auto_now_add=True)