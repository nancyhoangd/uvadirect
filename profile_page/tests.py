from django.test import TestCase
from django.test import Client
from .models import *
from .forms import *



class testScheduleForm(TestCase):

    def test_valid_form(self):
        response = self.client.post("/profile_page/schedule",data={'class_name':'CS3240', 'time':"11:00",'meeting_Days':("Monday","Monday") ,'building':'Rice','building_room':'102'})
        self.assertEqual(response.status_code, 301)

    def test_valid_schedule(self):
        form = ScheduleForm(data={'class_name':'CS3240', 'time':"11:00",'meeting_Days':("Monday","Monday") ,'building':'Rice','building_room':'102'})
        self.assertTrue(form.is_valid())

    def test_no_meeting_time(self):
        form = ScheduleForm(data={'class_name':'CS3240','meeting_Days':("Monday","Monday") ,'building':'Rice','building_room':'102'})
        self.assertFalse(form.is_valid())

    def test_no_class_name(self):
        form = ScheduleForm(data={'time': "11:00", 'meeting_Days':("Monday","Monday") ,'building': 'Rice', 'building_room': '102'})
        self.assertFalse(form.is_valid())

    def test_no_building(self):
        form = ScheduleForm(data={'class_name':'CS3240', 'time': "11:00", 'meeting_Days':("Monday","Monday")  ,'building_room': '102'})
        self.assertFalse(form.is_valid())

    def test_no_room(self):
        form = ScheduleForm(data={'class_name':'CS3240', 'time':"11:00",'meeting_Days':("Monday","Monday")  ,'building':'Rice'})
        self.assertFalse(form.is_valid())

class testFriendForm(TestCase):

    def test_valid_form(self):
        response = self.client.post("/profile_page/friends", data = {'form_user_name':'James'})
        self.assertEqual(response.status_code, 301)

    def test_valid_friend(self):
        form = FriendForm(data = {'form_user_name':'James'})
        self.assertTrue(form.is_valid())

    def test_invalid_friend(self):
        form = FriendForm(data = {'form_user_name':''})
        self.assertFalse(form.is_valid())

class testPrivacyForm(TestCase):

    def test_valid_form(self):
        response = self.client.post("/profile_page/privacy", data = {'allow':(True, "Allow location sharing with friends")})
        self.assertEqual(response.status_code, 301)

    def test_valid_setting(self):
        form = PrivacyForm(data = {'allow':(True)})
        self.assertTrue(form.is_valid())

    def test_false_setting(self):
        form = PrivacyForm(data = {'allow': (False)})
        self.assertTrue(form.is_valid())


# Create your tests here.
