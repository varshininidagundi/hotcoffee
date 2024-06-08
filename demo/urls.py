
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
admin.site.site_header = "HOT-CAFE Admin"
admin.site.site_title = "HOT-CAFE Admin's Portal"
admin.site.index_title = "Welcome to Varshini HOT-CAFE Admin's Portal"

urlpatterns = [
    path("admin", admin.site.urls),
    path('', include('home.urls'))
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
