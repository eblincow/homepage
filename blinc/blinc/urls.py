from django.conf.urls import patterns, url

urlpatterns = patterns('',
                       # Examples:
                       url(r'^$', 'blinc.views.home', name='home'),
                       url(r'^login', 'blinc.views.login', name='login'),

                       # /resume -- the resume without references
                       # /resume?references -- the resume with references
                       url(r'^resume', 'blinc.views.resume', name='resume'),

                       # hidden area to debut client apps
                       url(r'^client_apps/', 'blinc.client_apps.views.client_app', name='test'),
)
