from django.urls import path

from . import views

app_name = 'start'
urlpatterns = [
    path('', views.home, name='index'),
    path('weather/', views.weather, name='weather')
]