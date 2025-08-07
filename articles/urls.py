from django.urls import path
from . import views

app_name = "articles"

urlpatterns = [
    path("<int:id>/edit", views.edit, name="edit"),
    path("new/", views.new, name="new"),
    path("<int:id>", views.detail, name="detail"),
    path("", views.index, name="index"),
    
]