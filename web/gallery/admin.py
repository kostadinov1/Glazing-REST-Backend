from django.contrib import admin

# Register your models here.
from web.gallery.models import Album, Image


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    pass


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    pass
