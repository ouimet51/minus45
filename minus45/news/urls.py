from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('hacker', views.hacker, name='hacker'),
    path('nytbiz', views.nytbiz, name='nytbiz')

]
