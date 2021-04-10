from django.urls import path

from . import views

app_name = 'profile_page'
urlpatterns = [
    path('', views.profile_view, name='profile'),
    path('edit_info/', views.edit_info, name='edit_info'),
    path('privacy/', views.privacy, name='privacy'),
    path('schedule/', views.schedule, name='schedule'),
    path('friends/', views.add_friend, name = 'add_friend'),
    path('friends/remove/', views.remove_friend, name ='remove_friend'),
    path('friends/accept_or_decline_request/', views.accept_or_decline_request, name ='accept_or_decline_request'),
]