from django.shortcuts import render
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView

from web.services.models import Service, CompanyInfo
from web.services.serializers import ServiceSerializer, CompanyInfoSerializer


class CreateServiceView(CreateAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


class ServiceListView(ListAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


class GetServiceView(RetrieveAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


class GetCompanyInfoView(RetrieveAPIView):
    queryset = CompanyInfo.objects.all()
    serializer_class = CompanyInfoSerializer