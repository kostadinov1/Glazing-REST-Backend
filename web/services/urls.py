from django.urls import path

from web.services.views import ServiceListView, GetServiceView, GetCompanyInfoView

urlpatterns = (
    path('all-services/', ServiceListView.as_view(), name='get all services'),
    path('service/<int:pk>/', GetServiceView.as_view(), name='get service'),
    path('company-info/<int:pk>/', GetCompanyInfoView.as_view(), name='get company info'),

)