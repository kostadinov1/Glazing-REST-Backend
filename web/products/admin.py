from django.contrib import admin

# Register your models here.
from web.products.models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'id', 'created_on')
    list_filter = ('name', 'id', 'created_on')

