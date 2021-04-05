from django.urls import path

from . import views

app_name = 'start'
urlpatterns = [
    path('', views.index_view, name='index'),
    path('weather/', views.weather, name='weather')
]