from django.shortcuts import render_to_response
from django.template import RequestContext
from django.conf import settings
from django.views.decorators.gzip import gzip_page

usernames = settings.USERNAMES

@gzip_page
def home(request):
    # the main homepage view!
    context = RequestContext(request)
    context.update({'settings':settings})
    return render_to_response('home.html', context)


def login(request):
    # the login view!
    if request.is_secure():
        if 'u' and 'p' in request.POST:
            user = request.POST.get('u')
            password = request.POST.get('p')
            if user in usernames.keys() and password == usernames.get(user):
                response = render_to_response("client_login.html", RequestContext(request))
                response.set_cookie(key="authenticated",value="player",max_age=6000)
                return response
    return render_to_response('login_error.html',RequestContext(request))



