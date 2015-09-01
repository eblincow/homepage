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





