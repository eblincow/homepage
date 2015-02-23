from django.shortcuts import render_to_response, render
from django.template import RequestContext
from django.conf import settings
from django.http import HttpResponse, HttpResponseBadRequest
import json
import os.path
import datetime


from django.core.context_processors import csrf
from django.views.decorators.csrf import ensure_csrf_cookie

from django.core.context_processors import csrf


def home(request):

    context = RequestContext(request)
    context.update(settings.USERNAMES)
    return render_to_response('home.html', context)

def login(request):
    return render_to_response("client_login.html", RequestContext(request))

    #if 'user' and 'pass' in request.POST:
    #    return render_to_response('client_login.html', {}, context_instance=RequestContext(request))

def toh(request):
    return render_to_response("toh.html", RequestContext(request))