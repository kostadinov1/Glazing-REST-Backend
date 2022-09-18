from django.urls import path

from web.gallery.views import CreateAlbumView, GetAlbumView, UploadImageViewSet, ImageCRUDView, AlbumsListView

urlpatterns = (
    path('albums/', AlbumsListView.as_view(), name='albums'),
    path('album/<int:pk>/', GetAlbumView.as_view(), name='get album'),

    path('create-album/', CreateAlbumView.as_view(), name='create album'),
    path('edit-album/<int:pk>/', GetAlbumView.as_view(), name='edit album'),

    path('upload-image/<int:pk>/', UploadImageViewSet.as_view(), name='create image'),
    path('edit-image/<int:pk>/', ImageCRUDView.as_view(), name='edit image'),


)