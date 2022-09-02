from django.contrib import admin

# Register your models here.
from web.gallery.models import Album, Image


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ('name', 'id', 'created_on')
    list_filter = ('name', 'id', 'created_on')


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'image_file', 'created_on', 'album_id')
    list_filter = ('album_id', 'created_on')
