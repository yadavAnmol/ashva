from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from journeys import views   # ✅ import views only once

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home, name="home"),  
    path("journeys/", views.journeys, name="journeys"),
    path("add/", views.add_photo, name="add"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
]

# serve uploaded files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
