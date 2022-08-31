from django.urls import path

from web.gallery.views import CreateAlbumView, AlbumCRUDView, CreateImageView, ImageCRUDView, AlbumsListView

urlpatterns = (
    path('albums/', AlbumsListView.as_view(), name='albums'),
    path('create-album/', CreateAlbumView.as_view(), name='create album'),
    path('edit-album/<int:pk>/', AlbumCRUDView.as_view(), name='edit album'),

    path('create-image/', CreateImageView.as_view(), name='create image'),
    path('edit-image/<int:pk>/', ImageCRUDView.as_view(), name='edit image'),


)