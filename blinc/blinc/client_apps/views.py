from django.shortcuts import render_to_response
from django.template import RequestContext


def client_app(request):
    # If authenticated, show the private client app
    if request.COOKIES.get('authenticated')=='player':
        return render_to_response("client_app.html", RequestContext(request))
    else:
        return render_to_response("login_error.html", RequestContext(request))


