from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.postgres.fields import ArrayField

class Class(models.Model):
    class_name = models.CharField(max_length=200)
    time = models.CharField(max_length=200)
    days = models.CharField(max_length=200)
    building = models.CharField(max_length=200)
    building_number = models.CharField(max_length=200)
   
    def __str__(self):
        return (self.class_name)

class profile(models.Model):
    profile = models.OneToOneField(User, on_delete = models.CASCADE, primary_key=True)
    classes = models.ManyToManyField(Class,blank=True)

    def __str__(self):
        return self.profile.username


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    # if created:
    #     Profile.objects.create(user=instance)
    try:
        instance.profile.save()
    except:
        profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()