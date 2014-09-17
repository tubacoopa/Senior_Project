from django.conf.urls import patterns, url

from Site_App import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index')
)