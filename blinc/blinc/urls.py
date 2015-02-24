from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'blinc.views.home', name='home'),
    url(r'^login', 'blinc.views.login', name='login'),
    url(r'^client_apps/', 'blinc.client_apps.views.test', name='test'),
)
