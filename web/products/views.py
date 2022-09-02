from django.shortcuts import render
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView

from web.products.models import Product
from web.products.serializers import ProductSerializer


class CreateProductView(CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductListView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class GetProductView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

