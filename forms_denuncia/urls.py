from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from core.views import index, contact

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('contato/', contact, name='contato'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
