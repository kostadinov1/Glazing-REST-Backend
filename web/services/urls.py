from django.urls import path

from web.services.views import ServiceListView, GetServiceView

urlpatterns = (
    path('all-services/', ServiceListView.as_view(), name='get all services'),
    path('service/<int:pk>/', GetServiceView.as_view(), name='get service'),

)