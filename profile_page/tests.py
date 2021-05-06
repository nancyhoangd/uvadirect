from django.test import TestCase
from django.test import Client
from .models import *
from .forms import *
from django.contrib.auth.models import User

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

    def test_no_meeting_days(self):
        form = ScheduleForm(data={'class_name':'CS3240', 'time':"11:00", 'building':'Rice','building_room':'102'})
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

    def test_no_fields(self):
        form = ScheduleForm(data={})
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

class testUser(TestCase):
    def setup_user(self):
        self.user1 = User.objects.create_user(username='tester', email='tester@tester.com', password='testerpassword')
        self.user2 = User.objects.create_user(username='tester2', email='tester2@tester.com', password='testerpassword2')

    def setup_profile(self):
        self.profile1 = profile.objects.create(profile = user1)

    def setup_class(self):
        self.class1 = Class.objects.create(class_name="Test", time = "Test", days = "Test", building = "Test", building_number = "Test")
    
    def test_user_login(self):
        # client should be able to login with existing credentials
        self.setup_user()
        logged_in = self.client.login(username='tester', password='testerpassword')
        self.assertTrue(logged_in)

    def test_user_login_unexisting(self):
        # client should not be able to login with unexisting credentials
        logged_in = self.client.login(username='random', password='random')
        self.assertFalse(logged_in)

    def test_if_user_has_profile(self):
        # when a user logins, a profile for the user should be created
        self.setup_user()
        self.client.login(username='tester', password='testerpassword')
        self.assertIsInstance(self.user1.profile, profile)

    def test_user_has_name(self):
        # tests that username can be accessed
        self.setup_user()
        self.client.login(username='tester', password='testerpassword')
        self.assertEquals(self.user1.username, "tester")

    def test_if_user_has_scheduling_sharing(self):
        # when a user logins, the field schedule sharing should be false by default
        self.setup_user()
        self.client.login(username='tester', password='testerpassword')
        self.assertFalse(self.user1.profile.schedule_sharing)

    def test_user_privacy(self):
        # user's scheduling sharing settings should be true
        self.setup_user()
        self.user1.schedule_sharing = True
        self.assertTrue(self.user1.schedule_sharing)

    def test_add_class_to_user(self):
        # tests to make sure that a user can add a class
        self.setup_user()
        self.setup_class()
        self.client.login(user="tester", password="testerpassword")
        self.user1.profile.classes.add(self.class1)
        self.assertTrue(self.user1.profile.classes.filter(class_name="Test").exists())
        self.assertEquals(self.class1.__str__(), "Test")

    def test_add_multiple_classes_to_user(self):
        # tests to see if multiple classes can be added to a user's list of classes
        self.setup_user()
        self.setup_class()
        self.client.login(user="tester", password="testerpassword")
        self.user1.profile.classes.add(self.class1)
        self.class2 = Class.objects.create(class_name="Test2", time = "Test", days = "Test", building = "Test", building_number = "Test")
        self.class3 = Class.objects.create(class_name="Test3", time = "Test", days = "Test", building = "Test", building_number = "Test")
        self.user1.profile.classes.add(self.class2)
        self.user1.profile.classes.add(self.class3)
        self.assertEquals(len(self.user1.profile.classes.all()), 3)

    def test_add_friend_to_user(self):
        # tests to make sure that a user1 has user2 as a friend
        self.setup_user()     
        self.user1.profile.friends.add(self.user2.profile)
        self.user2.profile.friends.add(self.user1.profile)
        self.assertTrue(self.user2.profile in self.user1.profile.friends.all())  

    def test_add_friend_request_to_user(self):
        # tests adding a friend request to a user
        self.setup_user()
        self.friend_request = FriendRequest.objects.create(to_user=self.user1.username, from_user = self.user2.username)
        self.user1.profile.friends_requests.add(self.friend_request)
        self.assertTrue(self.friend_request in self.user1.profile.friends_requests.all())

class testRedirects(TestCase):
    def setup_user(self):
        self.user1 = User.objects.create_user(username='tester', email='tester@tester.com', password='testerpassword')
        self.user2 = User.objects.create_user(username='tester2', email='tester2@tester.com', password='testerpassword2')

    def test_redirect_schedule_page(self):
        self.setup_user()
        self.client.login(user="tester", password="testerpassword")
        response = self.client.post("/profile_page/schedule", follow = True)
        self.assertEquals(response.status_code, 200)

    def test_redirect_map_page(self):
        self.setup_user()
        self.client.login(user="tester", password="testerpassword")
        response = self.client.post("/map_page/default", follow = True)
        self.assertEquals(response.status_code, 200)

    def test_redirect_friends_page(self):
        self.setup_user()
        self.client.login(user="tester", password="testerpassword")
        response = self.client.post("/profile_page/friends", follow = True)
        self.assertEquals(response.status_code, 200)

    def test_redirect_friends_schedule_page(self):
        self.setup_user()
        self.client.login(user="tester", password="testerpassword")
        response = self.client.post("/profile_page/friends_schedule", follow = True)
        self.assertEquals(response.status_code, 200)

    def test_redirect_privacy_page(self):
        self.setup_user()
        self.client.login(user="tester", password="testerpassword")
        response = self.client.post("/profile_page/privacy", follow = True)
        self.assertEquals(response.status_code, 200)

    def test_redirect_about_page(self):
        self.setup_user()
        self.client.login(user="tester", password="testerpassword")
        response = self.client.post("/start/#about", follow = True)
        self.assertEquals(response.status_code, 200)

    def test_redirect_start_page(self):
        self.setup_user()
        self.client.login(user="tester", password="testerpassword")
        response = self.client.post("/start/", follow = True)
        self.assertEquals(response.status_code, 200)