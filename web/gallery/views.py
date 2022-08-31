from django.shortcuts import render
from rest_framework.generics import CreateAPIView , RetrieveUpdateAPIView

from web.gallery.models import Album
from web.gallery.serializers import AlbumSerializer, ImageSerializer


class CreateAlbumView(CreateAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer


class AlbumCRUDView(RetrieveUpdateAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer


class CreateImageView(CreateAPIView):
    queryset = Album.objects.all()
    serializer_class = ImageSerializer


class ImageCRUDView(RetrieveUpdateAPIView):
    queryset = Album.objects.all()
    serializer_class = ImageSerializer