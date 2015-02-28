from django.shortcuts import render_to_response
from django.template import RequestContext
from django.conf import settings


def client_app(request):
    # If authenticated, show the private client app
    context = RequestContext(request).update({'settings': settings})
    if request.COOKIES.get('authenticated') == 'player':
        return render_to_response("client_app.html", context)
    else:
        return render_to_response("login_error.html", context)


