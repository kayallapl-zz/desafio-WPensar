from django.contrib import admin
from django.conf.urls import url, include
from django.urls import path

urlpatterns = [
    url(r'^store/', include("store.urls")),
    path('admin/', admin.site.urls),
]