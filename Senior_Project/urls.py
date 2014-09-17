from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
	url(r'^$', include('Site_App.urls')),
	url(r'^site/', include('Site_App.urls')),
)
