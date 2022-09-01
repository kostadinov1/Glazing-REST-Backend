from django.urls import path

from web.gallery.views import CreateAlbumView, AlbumCRUDView, UploadImageViewSet, ImageCRUDView, AlbumsListView

urlpatterns = (
    path('albums/', AlbumsListView.as_view(), name='albums'),
    path('album/', AlbumCRUDView.as_view(), name='get album'),

    path('create-album/', CreateAlbumView.as_view(), name='create album'),
    path('edit-album/<int:pk>/', AlbumCRUDView.as_view(), name='edit album'),

    path('upload-image/', UploadImageViewSet.as_view(), name='create image'),
    path('edit-image/<int:pk>/', ImageCRUDView.as_view(), name='edit image'),


)