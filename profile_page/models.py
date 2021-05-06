from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
import datetime
# place in profile_page models.py near class profile
# Title: Many-to-one relationships
# Author: n/a (Django Docs)
# Date Accessed: 03/17/21
# Date Published: n/a
# URL: https://docs.djangoproject.com/en/3.0/topics/db/examples/many_to_one/
# Software License: n/a
# place in profile_page models.py near class profile
# Title: One-to-one relationships
# Author: n/a (Django Docs)
# Date Accessed: 03/16/21
# Date Published: n/a
# URL: https://docs.djangoproject.com/en/3.1/topics/db/examples/one_to_one/
# Software License: n/a
# place in profile_page models.py near class profile
# Title: How to Extend Django User Model 
# Author: Vitor Freitas
# Date Accessed: 03/16/21
# Date Published: 07/22/16
# URL: https://simpleisbetterthancomplex.com/tutorial/2016/07/22/how-to-extend-django-user-model.html
# Software License: CC BY-NC-SA 3.0
class Class(models.Model):
    class_name = models.CharField(max_length=200)
    time = models.CharField(max_length=200)
    days = models.CharField(max_length=200)
    building = models.CharField(max_length=200)
    building_number = models.CharField(max_length=200)

    def __str__(self):
        return (self.class_name)

    class Meta:
        ordering = ['-days', 'class_name']


class profile(models.Model):
    profile = models.OneToOneField(User, on_delete = models.CASCADE, primary_key=True)
    classes = models.ManyToManyField(Class,blank=True)
    friends = models.ManyToManyField('self', related_name = "friends_list+", blank = True)
    friends_requests = models.ManyToManyField('FriendRequest', blank = True)
    schedule_sharing = models.BooleanField(default=False)

    def __str__(self):
        name = self.profile.get_full_name()
        if name == "":
            name = self.profile.username
        return name
    

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    for user in User.objects.all():
        profile.objects.get_or_create(profile=user)

class FriendRequest(models.Model):
    to_user = models.CharField(max_length = 200)
    from_user = models.CharField(max_length = 200)

    def __str__(self):
        return ("Request from user: " + self.from_user)

    class Meta:
        unique_together = ("to_user", "from_user")