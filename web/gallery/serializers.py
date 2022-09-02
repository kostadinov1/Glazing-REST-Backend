from rest_framework import serializers

from web.gallery.models import Album, Image


class ImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Image
        fields = '__all__'


class AlbumSerializer(serializers.ModelSerializer):
    image_set = ImageSerializer(many=True)

    class Meta:
        model = Album
        fields = '__all__'
