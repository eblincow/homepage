# -*- coding: utf-8 -*-
from blinc.views import *
from django.test import TestCase
import django
from django.conf import settings


key_content_words = ["past work", "contact", "Vectorform", "Tic-tac-toe", "user"]


class View_Tests(TestCase):
    def setUp(self):
        pass

    def home_test(self):
        request = django.http.HttpRequest()
        response = home(request)
        self.assertEqual(response.status_code, 200, "Homepage load failed")
        for key_word in key_content_words:
            self.assertTrue(key_word in response.content, "Missing a key word in the homepage html!")

    def resume_test(self):
        request = django.http.HttpRequest()
        response = resume(request)
        self.assertEqual(response.status_code, 200, "Resume load failed")
        self.assertFalse("References" in response.content, "References showing in absence of GET param")

    def resume_with_references_test(self):
        request = django.http.HttpRequest()
        request.GET['references'] = 'Yay'
        response = resume(request)
        self.assertEqual(response.status_code, 200, "Resume load failed")
        self.assertTrue("References" in response.content, "References not contained when GET param supplied")

    def login_test(self):
        request = django.http.HttpRequest()
        request.POST['u'] = 'eb'
        request.POST['p'] = 'arcolight'
        response = login(request)
        self.assertEqual(response.status_code, 200, "Login failed!")

    def login_false_credentials_test(self):
        request = django.http.HttpRequest()
        request.POST['u'] = 'leon zundinger'
        request.POST['p'] = 'vego the carpathian'
        response = login(request)
        self.assertTrue(settings.UNAUTHORIZED_MESSAGE in response.content)
        self.assertEqual(response.status_code, 401, "Login worked when it shouldn't have!")





