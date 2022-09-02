from django.urls import path

from web.products.views import ProductListView, GetProductView

urlpatterns = (
    path('all-products/', ProductListView.as_view(), name='get all products'),
    path('product/<int:pk>/', GetProductView.as_view(), name='get product'),

)