from rest_framework import serializers

from web.gallery.models import Album, Image


class AlbumSerializer(serializers.ModelSerializer):

    class Meta:
        model = Album
        fields = '__all__'


class ImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Image
        fields = ('pk', 'image_file', 'album_id')
