from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('web.core.urls')),
    path('api/gallery/', include('web.gallery.urls')),
    path('api/products/', include('web.products.urls')),
    path('api/services/', include('web.services.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
