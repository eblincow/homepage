from django.shortcuts import render_to_response, render
from django.template import RequestContext
from django.conf import settings
from django.http import HttpResponse, HttpResponseBadRequest


def test(request):
    if request.is_secure():
        if request.COOKIES.get('authenticated')=='player':
            return render_to_response("client_app.html", RequestContext(request))
    render_to_response("login_error.html", RequestContext(request))
