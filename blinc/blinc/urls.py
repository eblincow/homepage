from django.conf.urls import patterns, url

urlpatterns = patterns('',
                       # Examples:
                       url(r'^$', 'blinc.views.home', name='home'),

                       # /resume -- the resume without references
                       # /resume?references -- the resume with references
                       url(r'^resume', 'blinc.views.resume', name='resume'),
                       url(r'^portal', 'blinc.views.portal', name='portal'),
                       url(r'^pp', 'blinc.views.pp', name='pp'),
                       )

