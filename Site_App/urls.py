from django.conf.urls import patterns, url

from Site_App import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^login/$', views.login, name='login'),
	url(r'^register/$', views.register, name='register'),
	url(r'^register_submit/$', views.register_submit, name='register_submit'),
	url(r'^profile/$', views.profile, name='profile'),
	url(r'^profile_edit/$', views.profile_edit, name='profile_edit'),
	url(r'^profile_submit/$', views.profile_submit, name='profile_submit'),
	url(r'^search/$', views.search, name='search')
)