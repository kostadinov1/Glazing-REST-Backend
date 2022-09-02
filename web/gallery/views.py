from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView

from web.gallery.models import Album, Image
from web.gallery.serializers import AlbumSerializer, ImageSerializer


class CreateAlbumView(CreateAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer


class AlbumsListView(ListAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer

class GetAlbumView(RetrieveAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer


class UploadImageViewSet(CreateAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer


class ImageCRUDView(RetrieveAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

