from django.urls import path

from . import views

urlpatterns = [
    path('', views.default_method, name='default_method'),
]