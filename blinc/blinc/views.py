from django.shortcuts import render_to_response, render
from django.template import RequestContext
from django.conf import settings
from django.http import HttpResponse, HttpResponseBadRequest
from django.conf.urls import patterns
from blinc.blinc.urls import urlpatterns

def home(request):

    context = RequestContext(request)
    context.update(settings.USERNAMES)
    return render_to_response('home.html', context)

def login(request):

    if request.is_secure():
        if 'u' and 'p' in request.POST:
            user = request.POST.get('u')
            password = request.POST.get('p')
            if user in settings.USERNAMES.keys() and password==settings.USERNAMES.get(user):

                urlpatterns += patterns('',
                    url(r'^/client_apps/', 'blinc.client_apps.views.test', name='test'),)

                return render_to_response("client_login.html", RequestContext(request))
    return HttpResponse("<html><h2>Those login credentials are not valid, friend.</h1></html>")




def toh(request):
    return render_to_response("toh.html", RequestContext(request))