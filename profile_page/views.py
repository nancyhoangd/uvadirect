from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from .forms import ScheduleForm, FriendForm, PrivacyForm
from .models import Class, profile, FriendRequest
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.core.exceptions import ObjectDoesNotExist


def profile(request):
    return HttpResponse("Display Profile Info Here")

def edit_info(request): 
    if request.method == 'POST':
        classesToBeDeleted = request.POST.getlist('class[]')
        for classDelete in classesToBeDeleted: #classDelete is a string name of class to be deleted
            # obj = Class.objects.get(class_name = classDelete)
            obj = request.user.profile.classes.get(class_name = classDelete)
            request.user.profile.classes.remove(obj) 
            request.user.save() 
            obj.delete()
    return HttpResponseRedirect('/profile_page/schedule/')

def privacy(request):
    if request.method == 'POST':
        form = PrivacyForm(request.POST)
        if form.is_valid():
            privacy = form.cleaned_data['allow']
            print(privacy)
            if privacy == "True":
                request.user.profile.location_sharing = True
            else:
                request.user.profile.location_sharing = False
            request.user.profile.save()
        return HttpResponseRedirect('/profile_page/privacy/')
    else:
        form = PrivacyForm()
    return render(request, 'mapsite/privacy.html/', {'form': form})

def schedule(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ScheduleForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            newClass = Class()
            newClass.class_name = form.cleaned_data['class_name']
            newClass.time = form.cleaned_data['time']
            newClass.days = form.cleaned_data['meeting_Days']
            newClass.building = form.cleaned_data['building']
            newClass.building_number = form.cleaned_data['building_room']
            newClass.save()

            request.user.profile.classes.add(newClass)
            request.user.save()
            return HttpResponseRedirect('/profile_page/schedule/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ScheduleForm()
    return render(request, 'mapsite/schedule.html/', {'form': form })

def add_friend(request):
    if request.method == 'POST':
        form = FriendForm(request.POST)
        if form.is_valid():
            try: 
                friend_object = User.objects.get(username = form.cleaned_data['form_user_name'])
                try:
                    friend_request = FriendRequest()
                    friend_request.to_user = friend_object.username
                    friend_request.from_user = request.user.username
                    friend_request.status = False
                    friend_request.save()
                    friend_object.profile.friends_requests.add(friend_request)
                    request.user.profile.friends_requests.add(friend_request)
                    friend_object.save()
                    request.user.save() 
                except IntegrityError: 
                    return HttpResponse("Already sent a friend request to " + friend_object.username)
            except ObjectDoesNotExist: 
                return HttpResponse("Account with username does not exist, try again")
            return HttpResponseRedirect('/profile_page/friends/')
    else:
        form = FriendForm()
    return render(request, 'mapsite/friends.html', {'form': form})

def remove_friend(request): 
    if request.method == 'POST':
        friendsToBeDeleted = request.POST.getlist('friend[]')
        for friendDelete in friendsToBeDeleted:
            friend_profile = User.objects.get(username = friendDelete)
            request.user.profile.friends.remove(friend_profile.profile) 
            request.user.save() 
    return HttpResponseRedirect('/profile_page/friends/')

def accept_or_decline_request(request): 
    if request.method == 'POST' and 'Accept' in request.POST:
        requestsToAccept = request.POST.getlist('request[]')
        for currentRequestUsername in requestsToAccept:
            friend_profile = User.objects.get(username = currentRequestUsername)
            currentFriendRequest = FriendRequest.objects.get(from_user = currentRequestUsername, to_user = request.user.username)
            request.user.profile.friends_requests.remove(currentFriendRequest)
            friend_profile.profile.friends_requests.remove(currentFriendRequest)
            # FriendRequest.objects.remove(currentFriendRequest)
            request.user.profile.friends.add(friend_profile.profile)
            friend_profile.profile.friends.add(request.user.profile)
            request.user.save()
            friend_profile.save()
    if request.method == 'POST' and 'Decline' in request.POST:
        requestsToDecline = request.POST.getlist('request[]')
        for currentRequestUsername in requestsToDecline:
            currentFriendRequest = FriendRequest.objects.get(from_user = currentRequestUsername, to_user = request.user.username)
            friend_profile = User.objects.get(username = currentRequestUsername)
            friend_profile.profile.friends_requests.remove(currentFriendRequest)
            friend_profile.save()
            request.user.profile.friends_requests.remove(currentFriendRequest)
            request.user.save()
            # FriendRequest.objects.remove(currentFriendRequest)
            currentFriendRequest.delete()
    return HttpResponseRedirect('/profile_page/friends/')