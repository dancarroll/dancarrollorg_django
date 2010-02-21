from django.conf.urls.defaults import *
from django.conf import settings
from mysite.settings import MEDIA_ROOT
from mysite.blog.feeds import LatestEntries

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

feeds = {
	'latest': LatestEntries,
}

urlpatterns = patterns('',
    # Example:
    # (r'^mysite/', include('mysite.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/(.*)', admin.site.root),
    (r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': '/home/erunama/erunama.com/public/media/', 'show_indexes': True}),
    (r'^polls/', include('mysite.polls.urls')),
    url(r'^activity/$', view='mysite.views.activity', name='main_activity'),
    (r'^blog/', include('mysite.blog.urls')),
    url(r'^shared/$', view='mysite.views.shared_items', name='main_shared_items'),
	(r'^feeds/(?P<url>.*)/$', 'django.contrib.syndication.views.feed', {'feed_dict': feeds}),
    #url(r'^$', view='mysite.views.index', name='main_index'),
    url(r'^test/$', view='mysite.views.index', name='main_index'),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^site-media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': MEDIA_ROOT,
             'show_indexes': True}),
        (r'^admin-media/(?P<path>.*)$', 'django.views.static.serve',
             {'document_root': 'E:/code/python/erunamadotcom/trunk/admin-media/', 'show_indexes': True}),
    )
