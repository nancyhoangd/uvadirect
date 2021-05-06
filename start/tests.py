from django.urls import resolve
from django.test import TestCase, RequestFactory, override_settings
from django.test import Client
from profile_page.models import *
from profile_page.views import *
from start.views import *
from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save




class ClassRequestTest(TestCase):

    def setUp(self):
        Class.objects.update_or_create(class_name = "CS3240", time = "11:00", days = "Monday", building = "Rice", building_number = "102")
        Class.objects.update_or_create(class_name = "CS4102", time = "1:00", days = "Wednesday", building = "Chem", building_number = "105")
    def test_class_request(self):
        self.assertTrue(Class.objects.filter(class_name = "CS3240").exists())
        self.assertTrue(Class.objects.filter(time="11:00").exists())
        self.assertTrue(Class.objects.filter(days = "Monday").exists())
        self.assertTrue(Class.objects.filter(class_name="CS4102").exists())
        self.assertTrue(Class.objects.filter(time="1:00").exists())
        self.assertTrue(Class.objects.filter(days="Wednesday").exists())
        self.assertTrue(Class.objects.filter(class_name = "CS3240", time = "11:00", days = "Monday", building = "Rice", building_number = "102").exists())
        self.assertTrue(Class.objects.filter(class_name = "CS4102", time = "1:00", days = "Wednesday", building = "Chem", building_number = "105").exists())

class SingleFieldClassTest_Name(TestCase):
    def setUp(self):
        Class.objects.update_or_create(class_name = "CS3240")
        Class.objects.update_or_create(class_name = "CS4102")
    def test_class_request(self):
        self.assertTrue(Class.objects.filter(class_name = "CS3240").exists())
        self.assertTrue(Class.objects.filter(class_name="CS4102").exists())
        self.assertFalse(Class.objects.filter(time = "11:00").exists())
        self.assertFalse(Class.objects.filter(time = "1:00").exists())

class SingleFieldClassTest_Time(TestCase):
    def setUp(self):
        Class.objects.update_or_create(time = "11:00")
        Class.objects.update_or_create(time = "1:00")
    def test_class_request(self):
        self.assertFalse(Class.objects.filter(class_name = "CS3240").exists())
        self.assertFalse(Class.objects.filter(class_name="CS4102").exists())
        self.assertTrue(Class.objects.filter(time = "11:00").exists())
        self.assertTrue(Class.objects.filter(time = "1:00").exists())

class SingleFieldClassTest_Days(TestCase):
    def setUp(self):
        Class.objects.update_or_create(days = "Monday")
        Class.objects.update_or_create(days = "Wednesday")
    def test_class_request(self):
        self.assertFalse(Class.objects.filter(class_name = "CS3240").exists())
        self.assertFalse(Class.objects.filter(class_name="CS4102").exists())
        self.assertTrue(Class.objects.filter(days = "Monday").exists())
        self.assertTrue(Class.objects.filter(days = "Wednesday").exists())

class SingleFieldClassTest_Building(TestCase):
    def setUp(self):
        Class.objects.update_or_create(building = "Rice")
        Class.objects.update_or_create(building = "Wilsdorf")
    def test_class_request(self):
        self.assertFalse(Class.objects.filter(days = "Monday").exists())
        self.assertFalse(Class.objects.filter(days = "Wednesday").exists())
        self.assertTrue(Class.objects.filter(building = "Rice").exists())
        self.assertTrue(Class.objects.filter(building = "Wilsdorf").exists())

class SingleFieldClassTest_BuildingNumber(TestCase):
    def setUp(self):
        Class.objects.update_or_create(building_number = "102")
        Class.objects.update_or_create(building_number = "0")
    def test_class_request(self):
        self.assertFalse(Class.objects.filter(building = "Rice").exists())
        self.assertFalse(Class.objects.filter(building = "Wilsdorf").exists())
        self.assertTrue(Class.objects.filter(building_number = "102").exists())
        self.assertTrue(Class.objects.filter(building_number = "0").exists())

class FriendRequestTest(TestCase):
    def setUp(self):
        FriendRequest.objects.update_or_create(to_user = "James", from_user = "James")

    def test_friend_request(self):
        self.assertTrue(FriendRequest.objects.filter(to_user = "James", from_user = "James").exists())

class SingleFieldFriendRequest_To(TestCase):
    def setUp(self):
        FriendRequest.objects.update_or_create(to_user = "yes")

    def test_user_only(self):
        self.assertTrue(FriendRequest.objects.filter(to_user = "yes").exists())

class SingleFieldFriendRequest_From(TestCase):
    def setUp(self):
        FriendRequest.objects.update_or_create(from_user = "James")
    def test_from_only(self):
        self.assertTrue(FriendRequest.objects.filter(from_user = "James").exists())
        self.assertFalse(FriendRequest.objects.filter(to_user = "James").exists())