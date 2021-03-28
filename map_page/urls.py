from django.urls import path
from django.conf.urls import url                                                                                                                           

from . import views

app_name = 'map_page'
urlpatterns = [
    path('', views.map_page, name='map_page'),
    url(r'', views.default_map, name="default"),
]