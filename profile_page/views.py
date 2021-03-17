from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from .forms import ScheduleForm
from .models import Class, profile
from django.contrib.auth.models import User


def profile(request):
    return HttpResponse("Display Profile Info Here")

def edit_info(request): 
    if request.method == 'POST':
        classesToBeDeleted = request.POST.getlist('class[]')
        for classDelete in classesToBeDeleted: #classDelete is a string name of class to be deleted
            obj = Class.objects.get(class_name = classDelete)
            request.user.profile.classes.remove(obj) #only works if there are no duplicate names in students classes
            request.user.save()    
    return HttpResponseRedirect('/profile_page/schedule/')

def privacy(request):
    return HttpResponse("Privacy Settings")

def schedule(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ScheduleForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
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