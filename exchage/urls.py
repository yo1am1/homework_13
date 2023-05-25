from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("links/", views.display, name="display"),
    path("calculate/", views.calculate, name="calculate"),
]
