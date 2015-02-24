from django.shortcuts import render_to_response, render
from django.template import RequestContext
from django.conf import settings
from django.http import HttpResponse, HttpResponseBadRequest


def test(request):
    if request.is_secure():

        return render_to_response("client_app.html", RequestContext(request))
    else:
        return HttpResponseBadRequest


