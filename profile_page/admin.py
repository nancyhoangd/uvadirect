from django.contrib import admin
from .models import profile, Class
from django.contrib.auth.admin import UserAdmin

# add classes as well
UserAdmin.list_display += ('profile',)
UserAdmin.list_filter += ('profile',)

admin.site.register(profile)
admin.site.register(Class)