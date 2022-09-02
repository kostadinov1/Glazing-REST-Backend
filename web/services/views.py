from django.shortcuts import render
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView

from web.services.models import Service
from web.services.serializers import ServiceSerializer


class CreateServiceView(CreateAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


class ServiceListView(ListAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


class GetServiceView(RetrieveAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

