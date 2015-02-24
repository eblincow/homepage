from django.shortcuts import render_to_response, render
from django.template import RequestContext
from django.conf import settings
from django.http import HttpResponse, HttpResponseBadRequest



usernames = settings.USERNAMES


def home(request):
    context = RequestContext(request)
    return render_to_response('home.html', context)







def login(request):
    if request.is_secure():
        if 'u' and 'p' in request.POST:
            user = request.POST.get('u')
            password = request.POST.get('p')
            if user in usernames.keys() and password == usernames.get(user):
                response = render_to_response("client_login.html", RequestContext(request))
                response.set_cookie(key="authenticated",value="player",max_age=6000)
                return response
    return render_to_response('login_error.html',RequestContext(request))



