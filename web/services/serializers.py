from rest_framework import serializers

from web.services.models import Service, CompanyInfo


class ServiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Service
        fields = '__all__'


class CompanyInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = CompanyInfo
        fields = '__all__'
