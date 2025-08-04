from django.urls import path
from django.contrib import admin
from .views import about, home


urlpatterns = [
    path("about/", about),
    path("", home),
    path("admin/", admin.site.urls)
]
