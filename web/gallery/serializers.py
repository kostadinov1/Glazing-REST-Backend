from rest_framework import serializers

from web.gallery.models import Album, Image


class ImageSerializer(serializers.ModelSerializer):
    image_file = serializers.ImageField()
    class Meta:
        model = Image
        fields = ('image_file', 'album_id')


class AlbumSerializer(serializers.ModelSerializer):
    image_set = ImageSerializer(many=True)

    class Meta:
        model = Album
        fields = '__all__'
