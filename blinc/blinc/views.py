from django.shortcuts import render_to_response
from django.template import RequestContext
from django.conf import settings
from django.views.decorators.gzip import gzip_page
from django.http import HttpResponse
import os
import codecs

usernames = settings.USERNAMES

@gzip_page
def home(request):
    # the main homepage view!
    context = RequestContext(request)
    context.update({'settings':settings})
    return render_to_response('home.html', context)


def login(request):
    # the login view!
    if 'u' and 'p' in request.POST:
        user = request.POST.get('u')
        password = request.POST.get('p')
        if user in usernames.keys() and password == usernames.get(user):
            response = render_to_response("client_login.html", RequestContext(request))
            response.set_cookie(key="authenticated",value="player",max_age=6000)
            return response
    return render_to_response('login_error.html',RequestContext(request))


def resume(request):
    file1 = os.path.join(settings.DIR_2, 'BlincowResume.txt')
    with codecs.open(file1, 'r', encoding='utf8') as f:
        content = f.read()
    # Censor the references section to not expose friends details
    if "references" not in request.GET:
        content_final = content.split("References")[0]
    else:
        # If they include ?references in the url
        content_final = content
    return HttpResponse(content_final, content_type='text/plain; charset=utf-8')

