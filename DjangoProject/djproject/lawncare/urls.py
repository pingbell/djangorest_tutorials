from django.urls import path

from . import views

app_name = 'polls'

urlpatterns = [
    path('display', views.display, name='display'),
    path('index', views.index, name='index'),


]

