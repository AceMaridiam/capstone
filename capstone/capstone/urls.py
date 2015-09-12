from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'capstone.views.home', name='home'),
    url(r'', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^media/(.*)$', 'django.views.static.serve', {'document_root' : settings.MEDIA_ROOT}),
) 

