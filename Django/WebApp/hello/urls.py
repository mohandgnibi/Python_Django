from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("ithri", views.ithri, name="ithri"),
    path("med", views.med, name="med")
]
