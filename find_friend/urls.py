from django.urls import path

from . import views

app_name = 'find_friend'
urlpatterns = [
    path('', views.find_friend, name='find_friend'),
]