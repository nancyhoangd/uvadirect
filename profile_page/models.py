from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
import datetime

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