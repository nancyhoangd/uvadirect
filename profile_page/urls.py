from django.urls import path

from . import views

app_name = 'profile_page'
urlpatterns = [
    path('', views.profile, name='profile'),
    path('edit_info/', views.edit_info, name='edit_info'),
    path('privacy/', views.privacy, name='privacy'),
    path('schedule/', views.schedule, name='schedule'),
]