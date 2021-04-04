from django import forms

class ScheduleForm(forms.Form):
    DAYS = (
        ("Monday", "Monday"), 
        ("Tuesday", "Tuesday"),
        ("Wednesday", "Wednesday"),
        ("Thursday", "Thursday"),
        ("Friday", "Friday"),
        ("Asynchronous", "Asynchronous"),
    )
    class_name = forms.CharField(label='Class Name', max_length=100)
    time = forms.CharField(label="Meeting Time", max_length=100)
    meeting_Days = forms.MultipleChoiceField(choices=DAYS)
    building = forms.CharField(label="Building Name", max_length=100)
    building_room = forms.CharField(label="Building Room", max_length=100)

class FriendForm(forms.Form):
    form_user_name = forms.CharField(label= 'Enter a username to send a friend request')

class PrivacyForm(forms.Form):
    CHOICES = (
        (True, "Allow location sharing with friends"),
        (False, "Do not allow location sharing with friends")
    )
    allow = forms.ChoiceField(label = 'Allow location sharing with friends?', choices = CHOICES)