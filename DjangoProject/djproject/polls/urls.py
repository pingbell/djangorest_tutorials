from django.urls import path

from . import views


urlpatterns = [
    path('default', views.default_method, name='default_method'),
    path('index', views.index, name='index'),
    path('base', views.base, name='base'),
    path('home', views.home, name='home'),
    path('list', views.list, name='list'),

]