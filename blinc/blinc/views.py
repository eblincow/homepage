from django.shortcuts import render_to_response
from django.template import RequestContext
from django.conf import settings
from django.http import HttpResponse, HttpResponseBadRequest
import json
import os.path
import datetime


def home(request):
    return render_to_response('home.html')
