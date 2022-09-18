from django.contrib import admin

# Register your models here.
from web.services.models import Service, CompanyInfo


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'id', 'created_on')
    list_filter = ('name', 'id', 'created_on')


@admin.register(CompanyInfo)
class CompanyInfoAdmin(admin.ModelAdmin):
    list_display = ('name', 'id',)
    list_filter = ('name', 'id',)
