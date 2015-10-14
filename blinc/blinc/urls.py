from django.conf.urls import patterns, url

urlpatterns = patterns('',
                       # Examples:
                       url(r'^$', 'blinc.views.home', name='home'),

                       # /resume -- the resume without references
                       # /resume?references -- the resume with references
                       url(r'^resume', 'blinc.views.resume', name='resume'),
                       url(r'^pp$', 'blinc.views.pp', name='pp'),
                       url(r'^ppfull', 'blinc.views.ppfull', name='ppfull'),
                       url(r'^blog', 'blinc.views.blog', name='blog'),
)

