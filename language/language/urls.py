from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'language.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^main/', include('main.urls', namespace='main')),
    url(r'^wiki/', include('wiki.urls', namespace='wiki')),
    url(r'^.*', include('main.urls')),
)
